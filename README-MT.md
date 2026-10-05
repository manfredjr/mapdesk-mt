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

## Situação do projeto

| Fatia | O quê | Situação |
|---|---|---|
| 1 | Fundação: forks, ramos e compilação do oficial | pronta para teste, PR #1 |
| 2 | Servidor embutido | a fazer |
| 3 | Marca e avisos | a fazer |
| 4 | Assinatura | a fazer |
| 5 | Publicação | a fazer |

## Antes de publicar

- Buscas no INPI e respostas do advogado (`docs/legal/`).
- Executável assinado (fatia 4).
- Teste de rede: nenhuma conexão a `*.rustdesk.com`.

## Depois de publicar

- Avisar a sessão do site-mt para trocar o executável da página de download.

## A confirmar com

Nada por enquanto.
