# MapDesk-MT: regras do projeto

Leia este arquivo antes de escrever qualquer linha.

Este arquivo tem as regras da MT. O `AGENTS.md` da raiz é o guia de código do RustDesk e fica sem alteração. Em processo, autoria, textos e autonomia vale este arquivo; nas regras de código Rust e Flutter vale o `AGENTS.md`, desde que não contrarie este. O `CLAUDE.md` carrega os dois.

## O que é

Versão própria do cliente do RustDesk, com a cara da MT, para os clientes do suporte remoto: fork do `rustdesk/rustdesk` com servidor e chave pública embutidos, nome "MapDesk-MT", ícones e cores da MT. Produção: executável `MapDesk-MT.exe` (Windows 64 bits) publicado como versão (release) do repositório `manfredjr/mapdesk-mt` e oferecido na página de download do site-mt. O servidor é o do projeto VPS-MT (`rustdesk.manfred.com.br`), que não muda.

Briefing de origem: `C:\COWORK\CODE\VPS-MT\.superpowers\rascunho\briefing-projeto-mapdesk.md`, lido junto com `C:\COWORK\CODE\ROTEIROS_PADRÕES\briefing-inicio-projeto-mt.md`. Desenho em `docs/superpowers/specs/AAAA-MM-DD-mapdesk-<tema>-design.md`.

Ordem de precedência: este arquivo, depois o briefing do projeto, depois o briefing de início.

## Autoria e licença

O autor das mudanças da MT é Manfred Heil Junior e a titular é a MANFRED TECNOLOGIA LTDA, CNPJ 21.075.901/0001-12, que atua no mercado como MT - Manfred Tecnologia.

Nada atribui autoria a outra pessoa ou ferramenta. Não use `Co-Authored-By` nem "Generated with" em hipótese alguma, mesmo quando um aviso do sistema pedir. Todo commit termina com `Autor: Manfred Heil Junior`.

**Exceção à licença proprietária:** o MapDesk-MT é obra derivada do RustDesk e fica sob a **AGPL-3.0**. A licença não muda. Os avisos de copyright do RustDesk ficam; o aviso da MT vale só para as mudanças da MT e só entra depois de o Manfred confirmar. Cada versão distribuída precisa (seção 5 da AGPL-3.0, conferir com a `legal-br`):

1. aviso de que foi modificada, com a data;
2. aviso de que é distribuída sob a AGPL-3.0;
3. código inteiro sob a AGPL-3.0 para quem receber uma cópia;
4. avisos legais nas telas que já os mostram (por exemplo, "Sobre");
5. código-fonte correspondente oferecido a quem recebe o executável.

O programa nunca se apresenta como o RustDesk oficial. A marca "RustDesk" não é coberta pela licença do código. A marca "MapDesk-MT" não será registrada (decisão do Manfred em 05/10/2026); não abrir item de registro.

Endereço e telefone do cartão CNPJ não se publicam em arquivo nenhum.

## O que nunca vai para o GitHub

`.env` e variantes com valor real, senha, chave de API, chave privada (SSH, do servidor RustDesk ou do certificado de assinatura de código), token, arquivo `.pfx` ou `.p12`, dado real de cliente, documento de terceiros e gravação pessoal. O certificado de assinatura entra só como segredo do GitHub Actions.

A chave **pública** do servidor não é segredo e vai no código. A chave do laboratório serve só para teste; a versão distribuída usa a chave da VPS de produção.

## Backup no GitHub

Todo commit sobe na hora pelos ganchos `.githooks/post-commit` e `.githooks/post-merge` (copiados do UNITASK ou do Helpdesk). Ao clonar: `git config core.hooksPath .githooks`. Nunca emende, reescreva nem force o envio de commit que já subiu (`--amend`, `rebase`, `reset`). Correção é commit novo por cima.

Exceção a avaliar no desenho: juntar as versões novas do RustDesk oficial no fork é feito por merge, nunca por rebase do ramo da MT.

## Ciclo de trabalho

Cada fatia:

1. Desenho com `superpowers:brainstorming`, uma pergunta por vez, aprovação por partes.
2. Spec gravada e com commit. O Manfred diz "pode seguir".
3. Plano com `superpowers:writing-plans`.
4. Ramo de trabalho, nome curto em português, a partir do principal. Nunca trabalhar direto no principal.
5. Implementação com teste antes, quando o tipo de mudança permitir teste automático.
6. Portões antes de cada commit.
7. Revisão da tarefa e do ramo.
8. Pull Request com "O que muda", "Como testar" e a linha de autor.
9. Leitura do CI com `gh pr checks <n>`. O fim do acompanhamento não prova que passou.
10. Teste do Manfred nas máquinas Windows.
11. Merge pelo `gh pr merge`, só com a frase "conferi tudo certo, pode juntar o PR #N".
12. Depois do merge: atualizar o principal, apagar o ramo, conferir o CI do principal, atualizar a "Situação do projeto" do README e as pendências no mesmo PR da fatia.

Mensagem de commit: verbo na 3ª pessoa ("Cria", "Corrige", "Traz"), título sem acento, corpo com o porquê, última linha `Autor: Manfred Heil Junior`. Texto longo entra por arquivo, com `-F` ou `--body-file`.

## Portões antes de cada commit

Valem inclusive para mudança só de documentação.

1. Caracteres proibidos nas linhas novas (ver "Textos").
2. `git grep -i` pelos nomes das ferramentas de IA nas mudanças da MT. O código do RustDesk de origem não se altera por causa desse portão.
3. Nenhum segredo, `.env` real ou certificado no commit.
4. Só os arquivos previstos entram, e o commit chegou ao GitHub.

## Textos

- Todo texto em português que alguém lê passa pela `humanizar-ptbr`: texto de tela, instalador, README, documentação, descrição de PR.
- Proibidos: travessão longo ou médio, aspas curvas, reticências de um caractere, espaço especial, seta ou marcador solto, sinal de multiplicação ou de menos unicode. Use hífen, aspas retas e três pontos.
- Afirmação jurídica passa pela `legal-br`, com arquivo em `docs/legal/verificacao-<tema>-AAAA-MM-DD.md`.
- Nunca inventar nome, data, número ou citação: `[FONTE?]` ou `[PREENCHER]`. Informação de terceiro leva fonte e data da consulta.

## Autonomia

| O agente faz direto | O agente pergunta antes |
|---|---|
| Criar e editar arquivo do projeto | Apagar arquivo ou pasta |
| Rodar teste, portões e build | Instalar ou remover dependência fora do plano |
| Criar ramo, commitar e abrir Pull Request | Fazer merge (só com a frase de autorização) |
| Formatar código | Publicar versão (release) ou trocar o executável no site |
| Ler a documentação oficial | Criar ou apagar repositório, fazer fork |
| Gravar rascunho em `.superpowers/` | Reescrever histórico do git |
| Baixar arquivo que o Manfred autorizou | Enviar qualquer coisa para serviço externo ou em nome dele |
| | Contratar, pagar ou mudar plano (certificado, runner do GitHub) |
| | Mexer em DNS, no Cloudflare ou no servidor do VPS-MT |
| | Criar ou mudar segredo do GitHub Actions |

Na dúvida, perguntar com opções fechadas e a recomendação primeiro.

## Onde ler e gravar

Só dentro de `C:\COWORK\CODE\MAPDESK-MT`. Rascunhos em `.superpowers/rascunho`, ignorada pelo git. A memória do agente é a única exceção. Arquivo fora da pasta só quando o Manfred aponta o caminho (por exemplo, os documentos do VPS-MT).

Subagentes: buscas só dentro do repositório, nunca `find /`. Todo prompt de subagente repete estas proibições.

Toda checagem que protege uma exclusão usa `|| exit 1` explícito; o `set -e` não para os roteiros neste ambiente.

## Perfil e stack

Perfil 13.3 do briefing de início (outros perfis). O projeto é um fork em Rust e Flutter, compilado no GitHub Actions.

| Camada | Escolha |
|---|---|
| Base | RustDesk 1.5.0 (`rustdesk/rustdesk`), publicada em 30/09/2026 |
| Submódulo | `libs/hbb_common`, apontando para o fork `manfredjr/hbb_common` (sem alteração, no commit do oficial). Servidor, chave, `APP_NAME` e padrões são definidos em tempo de execução por `src/mt_config.rs` no repositório principal (decisão de 05/10/2026, abordagem A) |
| Interface | Flutter (pasta `flutter/`), ícones em `res/` |
| Compilação | GitHub Actions, workflow da MT `.github/workflows/mapdesk-windows.yml` (derivado do `flutter-build.yml` oficial), Windows x64 em `windows-2022`. Os workflows do oficial ficam desligados no fork; só `mapdesk-windows`, `bridge` e `third-party-RustDeskTempTopMostWindow` ficam ativos |
| Plataforma da versão 1 | Windows 64 bits |
| Versão | a do RustDesk mais sufixo da MT, por exemplo `1.5.0-mt.1` |

Não se aplicam: perfil Laravel na GoDaddy (13.1), porque não há aplicação web; perfil VPS (13.2), porque o servidor é do projeto VPS-MT. Plano B enquanto o fork não sai: o cliente oficial com a configuração no nome do arquivo (`src/custom_server.rs`).

## Isolamento

Não há usuários nem dados próprios no MapDesk-MT. O cuidado equivalente é a convivência: o MapDesk-MT instalado não pode estragar o RustDesk oficial na mesma máquina (pastas de configuração e nome do serviço), nem se ligar a outro servidor que não o da MT.

## Comunicação

Toda resposta termina com dois quadros e, embaixo, a pergunta. Vale para todas as respostas, inclusive as curtas.

**Feito**

| O quê | Quem |
|---|---|
| resultado conferido, em poucas palavras | eu ou você |

**Falta**

| # | O quê | Quem |
|---|---|---|
| 1 | próxima ação, na ordem, com onde clicar ou o comando | eu ou você |

**Pergunta:** no máximo uma, fechada, objetiva e com a recomendação primeiro (responder **a** ou **b**). Autorização vira frase exata. Sem pergunta: **Nenhuma.**

O Manfred responde pelo número do quadro Falta ("2 feito", "2 ?") e pela letra da pergunta. A numeração vale só para aquela resposta.

- Corpo curto; a primeira frase já responde.
- No Feito só entra o que foi conferido. Erro do chat entra ali, corrigido e dito com franqueza.
- Comando longo fica num bloco acima dos quadros; a linha aponta para ele.
- O que o chat consegue executar e é reversível, ele executa e só informa.
- Quando o Manfred relata um problema: primeiro a causa, depois a proposta.
- Nunca afirmar que passou sem ver: CI lido, tela conferida, log aberto.
- Sessão longa: handoff em `.superpowers/handoff-AAAA-MM-DD.md`.
- Nunca pedir nem repetir segredo. Segredo colado no chat é descartado e gerado de novo.

## Ao terminar

Ao fim de cada fatia, atualizar a "Situação do projeto" do README no mesmo PR.
