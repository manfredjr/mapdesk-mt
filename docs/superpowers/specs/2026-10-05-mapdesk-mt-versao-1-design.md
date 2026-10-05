# MapDesk-MT: desenho da versão 1

Data: 05/10/2026. Autor: Manfred Heil Junior.
Briefing de origem: `C:\COWORK\CODE\VPS-MT\.superpowers\rascunho\briefing-projeto-mapdesk.md`.
Verificações jurídicas: `docs/legal/verificacao-licenca-agpl-e-marcas-2026-10-05.md` e `docs/legal/verificacao-privacidade-cliente-2026-10-05.md`.
Levantamento do código: `.superpowers/rascunho/achados-codigo-1.5.0.md`.

## 1. O que é

O MapDesk-MT é a versão do cliente RustDesk feita pela MT para os clientes do suporte remoto. Ele já vem ligado ao servidor da MT, com o nome e a identidade visual da MT. Não precisa de nenhuma configuração manual nem de um nome de arquivo comprido.

| Item | Valor |
|---|---|
| Programa | MapDesk-MT |
| Executável | `MapDesk-MT.exe` (Windows 64 bits) |
| Repositório | `manfredjr/mapdesk-mt`, público, fork de `rustdesk/rustdesk` |
| Base | RustDesk 1.5.0 (tag `1.5.0`), submódulo `hbb_common` no commit `229b904508364c8997aad0fb5af57effac859f60` |
| Licença | AGPL-3.0, a mesma do RustDesk (exceção à licença proprietária da MT) |
| Servidor | `rustdesk.manfred.com.br` (projeto VPS-MT, RustDesk Server OSS 1.1.16) |
| Marca | não será registrada (decisão do Manfred, 05/10/2026) |

## 2. Decisões tomadas

| # | Decisão | Motivo |
|---|---|---|
| 1 | Pasta `C:\COWORK\CODE\MAPDESK-MT` e nome MapDesk-MT | Briefing do projeto |
| 2 | Repositório público desde o início, como fork de verdade | A AGPL exige o código de cada versão; Actions gratuito em repositório público (docs.github.com, 05/10/2026); merge do oficial mais simples |
| 3 | Fatias 1 a 3 sem assinatura, só para teste interno; nenhum cliente recebe executável sem assinatura | O certificado demora e não deve travar o desenvolvimento |
| 4 | Aprovação por clique como padrão, não travada | O técnico pode configurar senha permanente numa máquina instalada para acesso sem ninguém na frente |
| 5 | Abordagem A: um único fork alterado; configuração em tempo de execução por `src/mt_config.rs` | Mudança pequena e concentrada; `hbb_common` sem alteração, o que também evita a pendência de licença dele |
| 6 | Ramos `master` (espelho do oficial) e `mt` (principal) e fork do `hbb_common` sem alteração | Separar o oficial das mudanças da MT; manter o código de cada versão disponível (AGPL, seção 6) |
| 7 | Servidor e chave travados | O MapDesk-MT só fala com o servidor da MT |
| 8 | Correção de segurança do RustDesk em até 7 dias; demais versões a cada 3 meses ou a pedido | Risco de programa de acesso remoto desatualizado |

## 3. Repositório e ramos

- `manfredjr/mapdesk-mt`: fork público de `rustdesk/rustdesk`.
- `manfredjr/hbb_common`: fork de `rustdesk/hbb_common`, **sem nenhuma alteração**. O `.gitmodules` do ramo `mt` aponta para ele. Assim o código de cada versão continua disponível mesmo que o oficial apague commits.
- Ramo `master`: espelho do oficial. Nunca recebe mudança da MT.
- Ramo `mt`: ramo principal do repositório no GitHub. Toda fatia sai de `mt` e volta por PR.
- Versão nova do oficial: a tag nova (por exemplo `1.5.1`) entra em `mt` por merge, num PR próprio, nunca por rebase. O PR sobe também o submódulo, depois de sincronizar o fork do `hbb_common`.
- Pasta local: `C:\COWORK\CODE\MAPDESK-MT` vira o clone do fork. As regras da MT ficam em `AGENTS-MT.md`; o `AGENTS.md` do RustDesk (guia do código) fica intacto, e o `CLAUDE.md` do RustDesk passa a carregar os dois (`@AGENTS-MT.md` e `@AGENTS.md`). `AGENTS-MT.md` vale mais em processo, autoria e textos; o `AGENTS.md` vale para as regras de código. `docs/legal/` e `docs/superpowers/` entram no ramo `mt` no primeiro commit da MT. `.superpowers/` fica no `.gitignore`.
- Os workflows do oficial ficam desligados no fork. Só roda o da MT.

## 4. Configuração embutida (`src/mt_config.rs`)

A função `aplicar()` roda no início de `load_custom_client` (`src/common.rs`, linha 2360 na 1.5.0). É a única linha alterada em arquivo do RustDesk para esta parte.

| O quê | Valor | Onde | Efeito |
|---|---|---|---|
| Nome | `MapDesk-MT` | `APP_NAME` | Pastas de configuração e serviço do Windows próprios; a consulta de versão a `api.rustdesk.com` não roda para nome diferente de "RustDesk" |
| Servidor de ID | `rustdesk.manfred.com.br` | `custom-rendezvous-server` em `OVERWRITE_SETTINGS` | Travado; o repasse (21117) vem do mesmo endereço |
| Chave pública | laboratório nas fatias 2 e 3; produção na fatia 5 | `key` em `OVERWRITE_SETTINGS` | Travada. Chave pública não é segredo |
| Servidor de API | desligado | `register-device` = "N" em `BUILTIN_SETTINGS` | `get_api_server` devolve vazio: nenhuma chamada à porta 21114 nem a `admin.rustdesk.com` |
| Aprovação | `click` | `approve-mode` em `DEFAULT_SETTINGS` | Padrão que o técnico pode mudar |

Nenhuma senha permanente de fábrica.

O `register-device` = "N" desliga também os comandos `--assign` e `--deploy` e o `deploy_device`, que são do Server Pro e ficam fora do escopo.

A configuração pelo nome do arquivo (`src/custom_server.rs`) continua ativa e tem precedência. Ela fica como está: é o plano B e não abre risco novo, porque o RustDesk oficial já aceita o mesmo método.

Valores das chaves: vêm da `docs/instalacao.md` do VPS-MT (passo G4). A chave do laboratório só é usada até a fatia 3.

## 5. Compilação

- Workflow da MT: `.github/workflows/mapdesk-windows.yml`, derivado do `flutter-build.yml` do oficial, só com o Windows x64 (`windows-2022`).
- Em todo PR para `mt`: compila e publica o `.exe` como artefato do PR para o teste do Manfred.
- Em tag `1.5.0-mt.N`: compila e cria a release com o `.exe` e o link do código da tag.
- Versão: a do RustDesk mais o sufixo da MT (`1.5.0-mt.1`).
- Assinatura (fatia 4): o certificado entra só como segredo do GitHub Actions. Nunca no Git, no chat ou em log.

## 6. Marca e avisos (fatia 3)

- Ícones do Windows em `res/` (programa, bandeja e instalador) e cor principal do tema Flutter trocados pelos da MT. Arquivos de logotipo e cor: [PREENCHER: onde estão o logotipo e a cor da MT].
- Nome "MapDesk-MT" na janela, na bandeja, no serviço e no instalador. "RustDesk" não aparece no nome, no ícone, no executável, no serviço nem no instalador.
- Tela "Sobre":
  - título "Sobre o MapDesk-MT";
  - versão do MapDesk-MT e versão base do RustDesk;
  - copyright do RustDesk mantido ("Purslane Tech Pte. Ltd.");
  - frase de origem: "Baseado no RustDesk, software livre distribuído sob a AGPL-3.0; não é produto oficial do RustDesk";
  - aviso de que é distribuído sob a AGPL-3.0, sem garantia, com link para a licença;
  - link para o código-fonte da versão (a tag);
  - link de privacidade trocado pelo aviso da MT, e o link "Website" pelo site da MT.
- `LICENCE` do RustDesk mantido sem mudança.
- `AVISO-DE-MODIFICACAO.md` na raiz: origem, lista das mudanças da MT e data de cada versão (AGPL, seção 5a).
- README em português, com a licença, a origem e o termo da seção 7 da AGPL: a licença não dá direito de uso dos nomes "MapDesk-MT" e "MT - Manfred Tecnologia" nem dos logotipos da MT.

## 7. Privacidade

O programa trata dados pessoais na sessão de suporte. Ao servidor da MT vão ID, identificador do aparelho, chave pública, versão, tipo de NAT e endereços público e local. O servidor guarda ID, IP e horário por 6 meses (VPS-MT). A tela não é gravada.

- O aviso de privacidade fica na página de download do site-mt (outro projeto), com os itens do art. 9º da LGPD listados na verificação de privacidade. Aqui entra só o link: [PREENCHER: endereço do aviso].
- Não há caixa de consentimento até a resposta da questão 3 da consulta ao advogado.
- Nada vai para servidor da RustDesk. O teste de rede confere isso a cada versão.

## 8. Segredos

| Segredo | Onde fica |
|---|---|
| Certificado de assinatura e senha | Segredo do GitHub Actions, criado pelo Manfred |
| Chave privada do servidor | Só na VPS (VPS-MT) |

A chave pública do servidor não é segredo e fica no código.

## 9. Fatias

| # | Fatia | Termina quando |
|---|---|---|
| 1 | Fundação: forks, ramos, workflow Windows, compilação do oficial sem mudança | O `.exe` da compilação abre na máquina do Manfred |
| 2 | Servidor embutido: `mt_config.rs` com a chave do laboratório | Testes 1 e 2 do briefing e teste de rede passam contra o laboratório |
| 3 | Marca e avisos: nome, ícones, cor, "Sobre", aviso de modificação, README | Testes 3, 4 e 5 passam e a tela "Sobre" é conferida pelo Manfred |
| 4 | Assinatura: certificado e assinatura no Actions | Teste 6 passa com o executável assinado |
| 5 | Publicação: chave de produção, tag `1.5.0-mt.1`, release | Teste de rede e teste 7 passam; a sessão do site-mt é avisada |

## 10. Testes

Automático (fatia 2): depois de `aplicar()`, o servidor de ID e a chave são os da MT, o servidor de API é vazio e a aprovação é por clique.

Manuais, do briefing (seção 9), feitos pelo Manfred:

1. Duas máquinas em redes diferentes (uma no 4G), sem configuração manual: conexão e aceite pelo botão verde.
2. Repasse forçado (porta 21117).
3. Instalação no sistema, com tela de administrador do Windows durante a sessão.
4. Convivência com o RustDesk oficial instalado na mesma máquina.
5. Reinstalação por cima de uma versão anterior.
6. Windows Defender e SmartScreen, com e sem assinatura.
7. Registro no servidor: o `hbbs` e o `hbbr` registram ID, IP e horário.

Teste de rede, antes de cada versão: durante a abertura e uma sessão completa, nenhuma conexão a `*.rustdesk.com`. Também se anota o que o técnico e o servidor recebem e para onde vai a mensagem `PeerDiscovery`.

## 11. Manutenção

- O Manfred recebe o aviso das versões novas pelo "Watch > Releases" de `rustdesk/rustdesk` no GitHub.
- Correção de segurança: entra em até 7 dias. As demais versões, a cada 3 meses ou quando o Manfred pedir.
- Cada versão nova passa por merge em PR, compilação, testes 1, 2 e de rede, e uma nova tag `<versão>-mt.N`, com o aviso de modificação atualizado.

## 12. Fora da versão 1

Ficam em `docs/superpowers/pendencias.md`: Mac, Linux, Android, iOS e cliente web; atualização automática própria; recursos do Server Pro; cessão do autor para a MT.

## 13. Pendências jurídicas (de `docs/legal/`)

1. Busca de "RustDesk" no INPI (Manfred).
2. Busca de "mapdesk", "map desk" e "mapdesc" por radical nas classes 9 e 42, só para evitar conflito (Manfred).
3. Troca do nome exibido em produto de terceiro e a LPI, art. 195, VI (advogado, questão 1).
4. Licença do `hbb_common`: arquivada, porque o `hbb_common` não é alterado (advogado, questão 2).
5. Consentimento do Marco Civil, art. 7º, IX, para os registros do servidor (advogado, questão 3).
6. Papel da MT na sessão de suporte a empresa cliente e a base legal para os empregados (advogado, questão 4).

O envio da consulta ao advogado é decisão do Manfred. As pendências 3, 5 e 6 precisam de resposta antes da fatia 5.
