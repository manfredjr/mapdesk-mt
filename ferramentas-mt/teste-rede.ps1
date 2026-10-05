# Teste de rede do MapDesk-MT.
#
# Mostra se o MapDesk-MT se conecta a algum servidor do RustDesk oficial
# (*.rustdesk.com). Roda no PowerShell 5.1 do Windows, sem instalar nada.
#
# Modo de usar:
#   1. Feche o RustDesk oficial, se estiver instalado, e abra o MapDesk-MT.
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
#   - no início, fotografa o cache de DNS do Windows, sem resolver nenhum nome;
#   - a cada 2 segundos, lista as conexões TCP e as portas UDP dos processos
#     MapDesk-MT;
#   - no fim, lê o cache de DNS de novo: todo nome do RustDesk oficial que
#     entrou ou foi renovado durante o teste conta como alerta;
#   - só depois disso resolve os nomes do RustDesk oficial, para casar os IPs
#     com as conexões TCP gravadas.
#
# Limites:
#   - o cache de DNS é da máquina inteira: um alerta de DNS quer dizer que
#     algum programa nesta máquina consultou o nome, não necessariamente o
#     MapDesk-MT. Por isso, feche o RustDesk oficial durante o teste;
#   - conexões TCP que duram menos de 2 segundos podem escapar da amostragem;
#   - o Windows não informa o destino de UDP; o registro no servidor de ID usa
#     UDP e aparece só pelo DNS.

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
$padraoOficial = "(^|\.)rustdesk\.com$"

$inicio = Get-Date
$arquivo = Join-Path (Get-Location) ("teste-rede-" + $inicio.ToString("yyyyMMdd-HHmmss") + ".txt")
$linhas = New-Object System.Collections.Generic.List[string]
$alertas = New-Object System.Collections.Generic.List[string]

function Escrever([string]$texto) {
    $linhas.Add($texto)
    Write-Host $texto
}

function Limpar-Endereco([string]$endereco) {
    if ($endereco.StartsWith("::ffff:")) {
        return $endereco.Substring(7)
    }
    return $endereco
}

function Ler-CacheRustdesk {
    $tabela = @{}
    $entradas = @(Get-DnsClientCache -ErrorAction SilentlyContinue | Where-Object { [string]$_.Entry -match $padraoOficial })
    foreach ($e in $entradas) {
        $nome = ([string]$e.Entry).ToLower()
        $ttl = [int]$e.TimeToLive
        if (-not $tabela.ContainsKey($nome) -or $tabela[$nome] -lt $ttl) {
            $tabela[$nome] = $ttl
        }
    }
    return $tabela
}

Escrever ("Teste de rede do MapDesk-MT, início em " + $inicio.ToString("dd/MM/yyyy HH:mm:ss"))
Escrever ("Duração: " + $Duracao + " segundos. Processo observado: " + $processo + ".exe")
Escrever ""

# Fotografia inicial do cache de DNS, antes de qualquer consulta
$cacheInicial = Ler-CacheRustdesk
$momentoInicial = Get-Date

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
            $remoto = Limpar-Endereco ([string]$c.RemoteAddress)
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
            $local = Limpar-Endereco ([string]$u.LocalAddress)
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

# Cache de DNS no fim, ainda sem nenhuma consulta do roteiro
$cacheFinal = Ler-CacheRustdesk
$decorrido = [int]((Get-Date) - $momentoInicial).TotalSeconds

Escrever ""
Escrever "Cache de DNS com nomes do RustDesk oficial:"
if ($cacheInicial.Count -eq 0 -and $cacheFinal.Count -eq 0) {
    Escrever "  nenhuma entrada, nem no início nem no fim"
}
foreach ($nome in ($cacheFinal.Keys | Sort-Object)) {
    $ttlFinal = $cacheFinal[$nome]
    if (-not $cacheInicial.ContainsKey($nome)) {
        Escrever ("  " + $nome + "  <CONSULTADO DURANTE O TESTE>")
        $alertas.Add("Algum programa nesta máquina consultou " + $nome + " durante o teste")
    } elseif ($ttlFinal -gt ($cacheInicial[$nome] - $decorrido + $intervalo)) {
        Escrever ("  " + $nome + "  <RENOVADO DURANTE O TESTE>")
        $alertas.Add("Algum programa nesta máquina consultou " + $nome + " de novo durante o teste")
    } else {
        Escrever ("  " + $nome + "  (já estava no cache antes do teste e não foi renovado)")
    }
}
foreach ($nome in ($cacheInicial.Keys | Sort-Object)) {
    if (-not $cacheFinal.ContainsKey($nome)) {
        Escrever ("  " + $nome + "  (estava no cache no início e expirou)")
    }
}
if ($cacheInicial.Count -gt 0) {
    Escrever "  Nomes que já estavam no cache no início não são conclusivos: uma consulta durante o teste pode ter sido respondida pelo cache. Para um resultado limpo, rode ipconfig /flushdns antes do teste ou espere alguns minutos e rode de novo."
}

# Só agora resolve os nomes oficiais, para casar com as conexões TCP
$ipsOficiais = @{}
Escrever ""
Escrever "Nomes do RustDesk oficial resolvidos no fim, depois da leitura do cache:"
foreach ($nome in $nomesOficiais) {
    try {
        $enderecos = [System.Net.Dns]::GetHostAddresses($nome)
        $lista = @()
        foreach ($endereco in $enderecos) {
            $ip = Limpar-Endereco $endereco.IPAddressToString
            $ipsOficiais[$ip] = $nome
            $lista += $ip
        }
        Escrever ("  " + $nome + ": " + ($lista -join ", "))
    } catch {
        Escrever ("  " + $nome + ": não resolveu")
    }
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

# Resumo
Escrever ""
if ($alertas.Count -eq 0 -and -not $achouProcesso) {
    Escrever "SEM RESULTADO: o MapDesk-MT não estava aberto"
} elseif ($alertas.Count -eq 0) {
    Escrever "OK: nenhuma conexão TCP ao RustDesk e nenhum nome do RustDesk consultado durante o teste"
} else {
    Escrever "ATENÇÃO: houve contato com o RustDesk oficial durante o teste:"
    foreach ($a in $alertas) {
        Escrever ("  " + $a)
    }
    Escrever "  O cache de DNS é da máquina inteira. Se o RustDesk oficial estava aberto, feche-o e rode o teste de novo."
}

try {
    $linhas | Out-File -FilePath $arquivo -Encoding utf8
    Write-Host ""
    Write-Host ("Relatório gravado em " + $arquivo)
} catch {
    Write-Host ("Não consegui gravar o relatório em " + $arquivo + ": " + $_.Exception.Message)
}
