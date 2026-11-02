# MapDesk-MT

Versão do cliente RustDesk feita pela MT - Manfred Tecnologia para os clientes do suporte remoto. Baseado no RustDesk, software livre distribuído sob a AGPL-3.0; não é produto oficial do RustDesk.

O código continua sob a AGPL-3.0 (arquivo `LICENCE`). As regras do projeto estão em `AGENTS-MT.md`, e o desenho, em `docs/superpowers/specs/`.

## Ramos

| Ramo | Para que serve |
|---|---|
| `mt` | Ramo principal, com as mudanças da MT. Toda mudança entra por Pull Request |
| `master` | Espelho do RustDesk oficial. Nunca recebe mudança da MT |

## Como compilar

O GitHub Actions compila o Windows x64 pelo workflow `.github/workflows/mapdesk-windows.yml`:

- em todo Pull Request para `mt`, com o executável como artefato do PR;
- em toda tag `<versão>-mt.<n>` (por exemplo `1.5.0-mt.1`), com o executável publicado na versão (release);
- por acionamento manual, na aba Actions.

A versão MT fica em `flutter/lib/mt/mt_info.dart` (`kMtVersao`) e sobe junto com a tag.

## Situação do projeto

| Fatia | O quê | Situação |
|---|---|---|
| 1 | Fundação: forks, ramos e compilação do oficial | feita, PR #1 |
| 2 | Servidor embutido | feita, PR #3; chave de produção desde 01/11/2026 |
| 3 | Marca e avisos | feita, PR #2 |
| 4 | Assinatura | adiada (sem certificado por enquanto) |
| 5 | Publicação | a fazer |
| Site | Página do produto em `public/`, para `mapdesk.manfred.com.br` | PR #7 aberto; falta o print da janela |

## Site do produto

A página do produto fica em `public/` e é servida em `https://mapdesk.manfred.com.br/` pelo Git do cPanel (`.cpanel.yml`). O teste `ferramentas-mt/testar-site.py` roda no workflow `mapdesk-site.yml` e barra a publicação com marca sem fonte, medição de terceiros ou sem os links da AGPL-3.0. Os passos de publicação estão em `docs/publicacao.md`.

## Antes de publicar

- Buscas no INPI e respostas do advogado (`docs/legal/`).
- Executável assinado (fatia 4).
- Teste de rede: nenhuma conexão a `*.rustdesk.com`.

## Depois de publicar

- Conferir a página do produto no ar (`docs/publicacao.md`, "Site do produto"). Depois da tag, pedir à sessão do site que `manfred.com.br/acesso` tenha o MapDesk-MT como botão principal e o RustDesk oficial como alternativa (decisão do Manfred em 02/11/2026).

## A confirmar com

Nada por enquanto.
