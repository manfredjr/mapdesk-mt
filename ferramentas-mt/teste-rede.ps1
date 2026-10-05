# Teste de rede do MapDesk-MT.
#
# Mostra se o MapDesk-MT se conecta a algum servidor do RustDesk oficial
# (*.rustdesk.com). Roda no PowerShell 5.1 do Windows, sem instalar nada.
#
# Modo de usar:
#   1. Abra o MapDesk-MT.
#   2. Abra o PowerShell na pasta onde quer o relatório e rode:
#        powershell -ExecutionPolicy Bypass -File teste-rede.ps1
#      ou, com outra duração em segundos (padrão 120):
#        powershell -ExecutionPolicy Bypass -File teste-rede.ps1 -Duracao 300
#   3. Durante o teste, use o MapDesk-MT normalmente (conectar, aceitar,
#      transferir arquivo).
#   4. No fim, leia o resumo na tela. O relatório completo fica na pasta
#      atual, com o nome teste-rede-AAAAMMDD-HHMMSS.txt.
#
# Como funciona:
#   - no início, resolve os nomes do RustDesk oficial e guarda os IPs;
#   - a cada 2 segundos, lista as conexões TCP e as portas UDP dos processos
#     MapDesk-MT;
#   - marca qualquer conexão a um IP do RustDesk oficial;
#   - no fim, lê o cache de DNS do Windows e lista toda entrada com "rustdesk".
#
# Observação: o próprio roteiro resolve os nomes do RustDesk oficial no
# início, então esses nomes aparecem no cache de DNS por causa dele. Eles
# entram no relatório como informação, não como alerta. O alerta vale para
# conexões a esses IPs e para outros nomes de rustdesk.com no cache.

param(
    [int]$Duracao = 120
)

$processo = "MapDesk-MT"
$intervalo = 2
$nomesOficiais = @(
    "rs-ny.rustdesk.com",
    "rs-sg.rustdesk.com",
    "rs-cn.rustdesk.com",
    "api.rustdesk.com",
    "admin.rustdesk.com",
    "rustdesk.com"
)

$inicio = Get-Date
$arquivo = Join-Path (Get-Location) ("teste-rede-" + $inicio.ToString("yyyyMMdd-HHmmss") + ".txt")
$linhas = New-Object System.Collections.Generic.List[string]
$alertas = New-Object System.Collections.Generic.List[string]

function Escrever([string]$texto) {
    $linhas.Add($texto)
    Write-Host $texto
}

Escrever ("Teste de rede do MapDesk-MT, início em " + $inicio.ToString("dd/MM/yyyy HH:mm:ss"))
Escrever ("Duração: " + $Duracao + " segundos. Processo observado: " + $processo + ".exe")
Escrever ""

# IPs do RustDesk oficial
$ipsOficiais = @{}
Escrever "Nomes do RustDesk oficial resolvidos no início:"
foreach ($nome in $nomesOficiais) {
    try {
        $enderecos = [System.Net.Dns]::GetHostAddresses($nome)
        $lista = @()
        foreach ($endereco in $enderecos) {
            $ip = $endereco.IPAddressToString
            $ipsOficiais[$ip] = $nome
            $lista += $ip
        }
        Escrever ("  " + $nome + ": " + ($lista -join ", "))
    } catch {
        Escrever ("  " + $nome + ": não resolveu")
    }
}
Escrever ""

# Coleta das conexões
$vistas = @{}
$achouProcesso = $false
$fim = $inicio.AddSeconds($Duracao)
Write-Host "Observando as conexões. Aguarde..."
while ((Get-Date) -lt $fim) {
    $agora = (Get-Date).ToString("HH:mm:ss")
    $procs = @(Get-Process -Name $processo -ErrorAction SilentlyContinue)
    if ($procs.Count -gt 0) {
        $achouProcesso = $true
        $pids = @($procs | ForEach-Object { [uint32]$_.Id })

        $tcp = @(Get-NetTCPConnection -OwningProcess $pids -ErrorAction SilentlyContinue)
        foreach ($c in $tcp) {
            $remoto = [string]$c.RemoteAddress
            if ($remoto -eq "0.0.0.0" -or $remoto -eq "::") {
                continue
            }
            $chave = "TCP|" + $remoto + "|" + $c.RemotePort
            if (-not $vistas.ContainsKey($chave)) {
                $vistas[$chave] = [pscustomobject]@{
                    Protocolo = "TCP"
                    Endereco  = $remoto
                    Porta     = $c.RemotePort
                    Estado    = [string]$c.State
                    Primeira  = $agora
                    Ultima    = $agora
                }
            } else {
                $vistas[$chave].Ultima = $agora
                $vistas[$chave].Estado = [string]$c.State
            }
        }

        $udp = @(Get-NetUDPEndpoint -OwningProcess $pids -ErrorAction SilentlyContinue)
        foreach ($u in $udp) {
            $local = [string]$u.LocalAddress
            $chave = "UDP|" + $local + "|" + $u.LocalPort
            if (-not $vistas.ContainsKey($chave)) {
                $vistas[$chave] = [pscustomobject]@{
                    Protocolo = "UDP"
                    Endereco  = $local
                    Porta     = $u.LocalPort
                    Estado    = "porta local aberta"
                    Primeira  = $agora
                    Ultima    = $agora
                }
            } else {
                $vistas[$chave].Ultima = $agora
            }
        }
    }
    Start-Sleep -Seconds $intervalo
}

# Conexões encontradas
Escrever ""
if (-not $achouProcesso) {
    Escrever ("Não achei o processo " + $processo + ".exe durante o teste. Abra o MapDesk-MT e rode de novo.")
} elseif ($vistas.Count -eq 0) {
    Escrever ("O processo " + $processo + ".exe rodou, mas não abriu nenhuma conexão durante o teste.")
} else {
    Escrever "Conexões do MapDesk-MT (protocolo, endereço, porta, estado, primeira e última vez vista):"
    foreach ($v in ($vistas.Values | Sort-Object Protocolo, Endereco, Porta)) {
        $marca = ""
        if ($v.Protocolo -eq "TCP" -and $ipsOficiais.ContainsKey($v.Endereco)) {
            $marca = "  <RUSTDESK OFICIAL: " + $ipsOficiais[$v.Endereco] + ">"
            $alertas.Add("Conexão " + $v.Protocolo + " a " + $v.Endereco + ":" + $v.Porta + " (" + $ipsOficiais[$v.Endereco] + ")")
        }
        Escrever ("  " + $v.Protocolo + "  " + $v.Endereco + "  " + $v.Porta + "  " + $v.Estado + "  " + $v.Primeira + " a " + $v.Ultima + $marca)
    }
    Escrever "  As linhas UDP mostram a porta local; o Windows não informa o destino de UDP."
}

# Cache de DNS
Escrever ""
Escrever "Cache de DNS com ""rustdesk"":"
$cache = @(Get-DnsClientCache -ErrorAction SilentlyContinue | Where-Object { $_.Entry -like "*rustdesk*" -or $_.Name -like "*rustdesk*" })
if ($cache.Count -eq 0) {
    Escrever "  nenhuma entrada"
} else {
    $nomesVistos = @{}
    foreach ($e in $cache) {
        $nome = [string]$e.Entry
        $dado = [string]$e.Data
        $chave = $nome + "|" + $dado
        if ($nomesVistos.ContainsKey($chave)) {
            continue
        }
        $nomesVistos[$chave] = $true
        $nota = ""
        $ehOficial = $nome -match "(^|\.)rustdesk\.com$"
        if ($ehOficial -and ($nomesOficiais -contains $nome)) {
            $nota = "  (consultado pelo próprio roteiro)"
        } elseif ($ehOficial) {
            $nota = "  <RUSTDESK OFICIAL>"
            $alertas.Add("Nome no cache de DNS: " + $nome)
        }
        Escrever ("  " + $nome + "  " + $dado + $nota)
    }
}

# Resumo
Escrever ""
if ($alertas.Count -eq 0 -and -not $achouProcesso) {
    Escrever "SEM RESULTADO: o MapDesk-MT não estava aberto"
} elseif ($alertas.Count -eq 0) {
    Escrever "OK: nenhuma conexão ao RustDesk"
} else {
    Escrever "ATENÇÃO: o MapDesk-MT falou com o RustDesk oficial:"
    foreach ($a in $alertas) {
        Escrever ("  " + $a)
    }
}

try {
    $linhas | Out-File -FilePath $arquivo -Encoding utf8
    Write-Host ""
    Write-Host ("Relatório gravado em " + $arquivo)
} catch {
    Write-Host ("Não consegui gravar o relatório em " + $arquivo + ": " + $_.Exception.Message)
}
