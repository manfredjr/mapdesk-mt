# Verificação jurídica: painel de gestão, licença AGPL-3.0 e venda como serviço

Data: 06/10/2026. Projeto MAPDESK-MT. Feita com a skill `legal-br`.

Cobre: (1) se o painel de gestão da MT (servidor de API e interface web) precisa ser AGPL-3.0; (2) o que a seção 13 exige se a MT modificar o `hbbs`/`hbbr`; (3) o que já está cumprido e o que falta na distribuição do MapDesk-MT; (4) o efeito do painel no enquadramento LGPD, só apontado; (5) a venda do painel, com o nome MapHub-MT, como serviço (SaaS) a outras empresas, inclusive com o MapDesk-MT em versão com a marca do cliente (white label).

Base reaproveitada, sem refazer: `docs/legal/verificacao-licenca-agpl-e-marcas-2026-10-05.md` (citada aqui como "verificação de 05/10"). Privacidade: `docs/legal/verificacao-privacidade-cliente-2026-10-05.md` e `docs/legal/rascunho-aviso-privacidade-mapdesk-mt-2026-10-05.md`.

## 1. Contexto e premissas

### 1.1. Fatos

| Fato | Fonte |
|---|---|
| O MapDesk-MT é fork AGPL-3.0 do cliente RustDesk 1.5.0, com código em `github.com/manfredjr/mapdesk-mt` | `AGENTS-MT.md`; verificação de 05/10, item 1.1 |
| O servidor de ID e repasse é o RustDesk Server OSS (`hbbs`/`hbbr`), sem modificação, numa VPS da MT | pedido; verificação de 05/10, item 1.1 |
| O painel seria: (a) servidor de API novo, escrito do zero pela MT, que recebe por HTTP as chamadas que o cliente já faz; (b) interface web integrada ao Inventário e ao Helpdesk da MT, com botão que abre o MapDesk-MT pelo endereço `mapdesk-mt://` | pedido |
| Nenhum código do RustDesk seria copiado para o painel; a MT pode ler o código do cliente para entender o protocolo | pedido |
| Pergunta 5: a MT quer vender o painel, com o nome MapHub-MT, como SaaS a empresas, inclusive empresas de TI que dariam suporte aos clientes delas; a MT hospeda o MapHub-MT e o `hbbs`/`hbbr`; as empresas recebem o MapDesk-MT, talvez com a marca delas | pedido do coordenador, 06/10/2026 |

**FATO (código, lido em 06/10/2026).** O protocolo que o painel teria de atender está no cliente:

- `src/hbbs_http/sync.rs`, `heartbeat_url()`: monta `{servidor de API}/api/heartbeat`; o envio de dados do aparelho usa a mesma URL trocando `heartbeat` por `sysinfo` e `sysinfo_ver`.
- Batimento (heartbeat): JSON com `id`, `uuid`, `ver`, `conns` (quando há conexões) e `modified_at`. A resposta pode trazer `sysinfo` (pede novo envio), `disconnect` (lista de conexões a derrubar), `modified_at` e `strategy` (opções de configuração que o cliente aplica em `handle_config_options`).
- Dados do aparelho (sysinfo): `src/common.rs`, `get_sysinfo()`, com `cpu`, `memory`, `os`, `hostname` e `username`, mais `version`, `id` e `uuid` acrescentados em `sync.rs`.
- Hoje o envio está desligado no MapDesk-MT: `src/mt_config.rs` grava `register-device` = "N", e `get_api_server` (`src/common.rs`) devolve vazio nesse caso. Ligar o painel exige mudar o cliente.

**FATO (código, 06/10/2026).** No `rustdesk/rustdesk-server`, ramo `master`, o arquivo `src/rendezvous_server.rs` não tem rota `heartbeat`, `sysinfo` nem `/api/` (busca no arquivo baixado; cópia em `.superpowers/rascunho/rustdesk-server-rendezvous_server.rs`). Não se leu o restante do repositório.

**INTERPRETAÇÃO.** O servidor OSS não atende essas chamadas. Quem as atende hoje é o produto pago da RustDesk (Server Pro), cujos termos já foram lidos na verificação de 05/10, item 3.1. O painel da MT seria uma implementação própria e independente dessa interface. Os termos da RustDesk alcançam só o "Software" ali definido (Server Pro e serviços da RustDesk); o painel não usa nenhum deles.

### 1.2. Premissas de incidência

| Premissa | O que aciona | Fundamento |
|---|---|---|
| O MapDesk-MT e o `hbbs`/`hbbr` são obras sob a AGPL-3.0 | Texto da AGPL-3.0 | `LICENCE` do RustDesk (verificação de 05/10, item 1.3); `LICENSE` do `rustdesk/rustdesk-server` baixado em 06/10/2026, igual ao texto oficial salvo a quebra de linha do apêndice; API do GitHub informa `"spdx_id": "AGPL-3.0"` |
| O painel é programa de computador da MT | Lei nº 9.609/1998 e, no que couber, Lei nº 9.610/1998 | Lei nº 9.610/1998, art. 7º, § 1º: "Os programas de computador são objeto de legislação específica, observadas as disposições desta Lei que lhes sejam aplicáveis." |
| Há tratamento de dados pessoais pelo painel (nome da máquina, nome do usuário do Windows, ID, IP) | LGPD | Só apontado no item 5; análise na verificação de privacidade |
| Na pergunta 5, a relação MT e empresa cliente é entre empresas | Regime civil, a conferir; CDC a conferir | Só apontado no item 6.4 |

### 1.3. Fontes

| Fonte | Onde | Data | Observação |
|---|---|---|---|
| GNU AGPL-3.0, texto oficial | https://www.gnu.org/licenses/agpl-3.0.txt; cópia em `.superpowers/rascunho/agpl-3.0.txt`, SHA-256 `0d96a4ff68ad6d4b6f1f30f713b18d5184912ba8dd389f86aa7710db079abcb0` | Cópia de 05/10/2026, conferida pelo hash em 06/10/2026 | Em 06/10/2026 o `gnu.org` não respondeu (falha de conexão); o hash da cópia é o registrado na verificação de 05/10 |
| `LICENSE` do `rustdesk/rustdesk-server` | https://raw.githubusercontent.com/rustdesk/rustdesk-server/master/LICENSE; cópia em `.superpowers/rascunho/rustdesk-server-LICENSE.txt`, SHA-256 `8486a10c4393cee1c25392769ddd3b2d6c242d6ec7928e1414efff7dfb2f07ef` | 06/10/2026 | Comparado com a cópia acima: só difere a quebra de duas linhas do apêndice "How to Apply" |
| Repositório `rustdesk/rustdesk-server` | API do GitHub, `repos/rustdesk/rustdesk-server` | 06/10/2026 | `"spdx_id": "AGPL-3.0"`, descrição "RustDesk Server Program" |
| FAQ da FSF sobre a GPL | https://www.gnu.org/licenses/gpl-faq.html, lida pela captura do Internet Archive de 05/10/2026 (`web.archive.org/web/20261005011241id_/http://www.gnu.org/licenses/gpl-faq.html`); cópia em `.superpowers/rascunho/gpl-faq-2026-10-05.html`, SHA-256 `6b48c709107e216b22c8415ed5c190c1c10818ac79f792563dfa501ee8dcec14` | Consultada em 06/10/2026 | O `gnu.org` não respondeu em 06/10/2026. As aspas curvas do original foram trocadas por aspas retas na transcrição. A FAQ é a leitura da FSF, autora da licença, e não texto da licença |
| Lei nº 9.609/1998, art. 6º | Cópia do Planalto de 05/10/2026, `.superpowers/rascunho/lei9609.html` (SHA-256 na verificação de 05/10); biblioteca `legal-br`, `fontes-md/leis/06-lei-software-9609-1998.md` | 05/10/2026 (Planalto) | O Planalto não respondeu em 06/10/2026 |
| Lei nº 9.610/1998, arts. 7º, § 1º, e 8º, I | Biblioteca `legal-br`, `fontes-md/leis/07-direitos-autorais-9610-1998.md` (coleta de 21/08/2026) | 06/10/2026 | Planalto fora do ar em 06/10/2026; ver pendência 7 |
| Lei nº 12.965/2014 (Marco Civil), arts. 5º, VII e VIII, e 15 | Biblioteca `legal-br`, `fontes-md/leis/04-marco-civil-internet-lei-12965-2014.md` (coleta de 21/08/2026) | 06/10/2026 | Só para apontar o tema no item 6.4 |
| Arquivos do projeto | `AVISO-DE-MODIFICACAO.md`, `README-MT.md`, `README.md`, `flutter/lib/mt/mt_info.dart`, `flutter/lib/desktop/pages/desktop_setting_page.dart` (classe `_About`), `docs/publicacao.md`, `.gitmodules`, `.github/workflows/mapdesk-windows.yml`, `src/mt_config.rs`, `src/hbbs_http/sync.rs`, `src/common.rs`; `git tag` | 06/10/2026 | Ramo `mt`, commit `85184c32f` |

A biblioteca local da `legal-br` não tem `STATUS-FONTES.md`. Os dispositivos de lei brasileira usados aqui sustentam interpretações, salvo o art. 6º da Lei nº 9.609/1998, conferido no Planalto em 05/10/2026.

## 2. Transcrições

### 2.1. AGPL-3.0

Seção 0:

- "\"The Program\" refers to any copyrightable work licensed under this License."
- "To \"modify\" a work means to copy from or adapt all or part of the work in a fashion requiring copyright permission, other than the making of an exact copy. The resulting work is called a \"modified version\" of the earlier work or a work \"based on\" the earlier work."
- "A \"covered work\" means either the unmodified Program or a work based on the Program."
- "Mere interaction with a user through a computer network, with no transfer of a copy, is not conveying."

Seção 1: "The \"Corresponding Source\" for a work in object code form means all the source code needed to generate, install, and (for an executable work) run the object code and to modify the work, including scripts to control those activities. However, it does not include the work's System Libraries, or general-purpose tools or generally available free programs which are used unmodified in performing those activities but which are not part of the work."

Seção 2: "This License explicitly affirms your unlimited permission to run the unmodified Program." E: "You may make, run and propagate covered works that you do not convey, without conditions so long as your license otherwise remains in force."

Seção 5, último parágrafo: "A compilation of a covered work with other separate and independent works, which are not by their nature extensions of the covered work, and which are not combined with it such as to form a larger program, in or on a volume of a storage or distribution medium, is called an \"aggregate\" if the compilation and its resulting copyright are not used to limit the access or legal rights of the compilation's users beyond what the individual works permit. Inclusion of a covered work in an aggregate does not cause this License to apply to the other parts of the aggregate."

Seção 10: "Each time you convey a covered work, the recipient automatically receives a license from the original licensors, to run, modify and propagate that work, subject to this License. You are not responsible for enforcing compliance by third parties with this License." E: "You may not impose any further restrictions on the exercise of the rights granted or affirmed under this License. For example, you may not impose a license fee, royalty, or other charge for exercise of rights granted under this License, [...]"

Seção 13, primeiro parágrafo: "Notwithstanding any other provision of this License, if you modify the Program, your modified version must prominently offer all users interacting with it remotely through a computer network (if your version supports such interaction) an opportunity to receive the Corresponding Source of your version by providing access to the Corresponding Source from a network server at no charge, through some standard or customary means of facilitating copying of software."

As seções 4, 5(a) a 5(d), 6(d) e 7 estão transcritas na verificação de 05/10, itens 2.1 a 2.5, e não se repetem aqui.

### 2.2. FAQ da FSF

`#MereAggregation`: "Where's the line between two separate programs, and one program with two parts? This is a legal question, which ultimately judges will decide. We believe that a proper criterion depends both on the mechanism of communication (exec, pipes, rpc, function calls within a shared address space, etc.) and the semantics of the communication (what kinds of information are interchanged)." E: "By contrast, pipes, sockets and command-line arguments are communication mechanisms normally used between two separate programs. So when they are used for communication, the modules normally are separate programs. But if the semantics of the communication are intimate enough, exchanging complex internal data structures, that too could be a basis to consider the two parts as combined into a larger program."

`#GPLAndPlugins`: "A main program that is separate from its plug-ins makes no requirements for the plug-ins."

`#UnreleasedModsAGPL`: "The GNU Affero GPL requires that modified versions of the software offer all users interacting with it over a computer network an opportunity to receive the source. What the company is doing falls under that meaning, so the company must release the modified source code."

`#AGPLv3InteractingRemotely`: "If the program is expressly designed to accept user requests and send responses over a network, then it meets these criteria." E: "If a program is not expressly designed to interact with a user through a network, but is being run in an environment where it happens to do so, then it does not fall into this category."

`#AGPLv3ServerAsUser`: "It doesn't matter if you call the program a \"client\" or a \"server,\" the question you need to ask is whether or not there is a reasonable expectation that a person will be interacting with the program remotely over a network."

`#AGPLProxy`: "For software on a proxy server, you can provide an offer of source through a normal method of delivering messages to users of that kind of proxy. For example, a Web proxy could use a landing page." E: "If you know that a certain user has already been shown the offer, for the current version of the software, you don't have to repeat it to that user again."

`#AGPLv3CorrespondingSource`: "So, if your modified version depends on libraries under other licenses, such as the Expat license or GPLv3, the Corresponding Source should include those libraries (unless they are System Libraries). If you have modified those libraries, you must provide your modified source code for them."

### 2.3. Lei brasileira

Lei nº 9.609/1998, art. 6º: "Não constituem ofensa aos direitos do titular de programa de computador:" [...] "III - a ocorrência de semelhança de programa a outro, preexistente, quando se der por força das características funcionais de sua aplicação, da observância de preceitos normativos e técnicos, ou de limitação de forma alternativa para a sua expressão;"

Lei nº 9.610/1998, art. 8º: "Não são objeto de proteção como direitos autorais de que trata esta Lei:" "I - as idéias, procedimentos normativos, sistemas, métodos, projetos ou conceitos matemáticos como tais;"

## 3. Pergunta 1: o painel precisa ser AGPL e ter o código publicado?

### 3.1. Painel escrito do zero, falando por HTTP

**FATO LEGAL (licença).** A AGPL-3.0 alcança o "Program" e os "covered works", isto é, o programa e as obras "based on" ele, que são as que copiam ou adaptam parte dele "in a fashion requiring copyright permission" (seção 0). Incidência: é a cláusula que define o alcance de toda a licença; o painel só fica sujeito a ela se for obra "based on" o MapDesk-MT ou o `hbbs`/`hbbr`.

**FATO LEGAL (licença).** A seção 13 começa por "if you modify the Program" e obriga "your modified version". Incidência: a obrigação de oferecer o código pela rede recai só sobre a versão modificada do programa sob AGPL.

**INTERPRETAÇÃO.** O painel, escrito do zero, roda em processo próprio e conversa com o cliente por HTTP, em outra máquina ou no mesmo servidor do `hbbs`. Pelo critério da FAQ (`#MereAggregation`), sockets são mecanismo "normally used between two separate programs". A semântica da troca é simples: mensagens JSON curtas com ID, versão, dados do aparelho e algumas opções de resposta. Não há estrutura interna complexa do cliente trafegando. O painel, então, não é obra "based on" o MapDesk-MT, não é "the Program" e não é "modified version". A AGPL não o alcança, e a MT pode mantê-lo com licença fechada e código privado. O botão `mapdesk-mt://` do Inventário e do Helpdesk só chama outro programa com argumentos, que a mesma FAQ também põe entre os mecanismos de programas separados.

**INTERPRETAÇÃO.** A resposta `strategy`, que empurra opções de configuração para o cliente, ainda é troca de pares chave e valor que o cliente já sabe ler. Não muda a conclusão, desde que o painel não passe a depender de estruturas internas do cliente (por exemplo, serializar tipos Rust do cliente).

**RISCO (baixo).** A FAQ diz que a fronteira entre programas separados e um programa só é "a legal question, which ultimately judges will decide". Não se achou decisão brasileira sobre o ponto, e a busca não foi feita. O risco fica baixo porque o painel não é distribuído junto com o cliente, roda só nos servidores da MT e troca dados simples.

### 3.2. Ler o código do cliente para implementar o protocolo

**FATO LEGAL (licença).** A seção 2 afirma "unlimited permission to run the unmodified Program", e a licença só condiciona copiar, modificar, transmitir e oferecer pela rede versão modificada. Nenhuma seção condiciona ler o código.

**INTERPRETAÇÃO.** Ler o código não cria obrigação pela AGPL. O que importa é o que vai parar no painel. Nomes de campo e de rota (`/api/heartbeat`, `id`, `uuid`, `hostname`) e o formato das mensagens são a interface funcional que o cliente exige. Implementar a mesma interface por escrita própria se aproxima da "semelhança de programa a outro, preexistente, quando se der por força das características funcionais de sua aplicação" (Lei nº 9.609/1998, art. 6º, III) e da exclusão de "sistemas, métodos" da proteção autoral (Lei nº 9.610/1998, art. 8º, I). É interpretação, não aplicação direta: o art. 6º trata de ofensa aos direitos do titular, e aqui o titular já licenciou tudo pela AGPL; o ponto só pesaria se a MT copiasse expressão protegida.

**RECOMENDAÇÃO.** Separar leitura e escrita: alguém lê o cliente e escreve uma especificação do protocolo em palavras próprias (rotas, campos, tipos, respostas); o painel é escrito a partir dessa especificação, sem colar código. A especificação pode ficar no repositório público do MapDesk-MT, porque é documentação e reforça que o painel nasce dela.

### 3.3. Se a MT copiar código do RustDesk para o painel

**FATO LEGAL (licença).** "To \"modify\" a work means to copy from or adapt all or part of the work in a fashion requiring copyright permission" (seção 0). Incidência: copiar trecho protegido do cliente ou do servidor para o painel faz do painel obra "based on" o programa.

**INTERPRETAÇÃO.** A resposta muda nos casos abaixo:

| O que se copia | Efeito |
|---|---|
| Funções, módulos, `structs` com sua implementação ou trechos de código do RustDesk | O painel vira obra "based on". Se for transmitido a alguém, a seção 5(c) põe a obra inteira sob a AGPL. Se for oferecido pela rede a pessoas de fora da MT, a seção 13 obriga oferecer o código do painel inteiro a elas |
| Arquivos `.proto` do `hbb_common` | Mesmo efeito, e ainda a dúvida de licença do `hbb_common` (pendência 4 da verificação de 05/10). O painel fala JSON por HTTP e não precisa deles |
| Cliente web do RustDesk ou outra interface pronta | Mesmo efeito. A licença do cliente web não foi conferida (pendência 9) |
| Nomes de campos e rotas, reescritos à mão a partir da especificação | Não é cópia de expressão protegida (item 3.2) |
| Biblioteca de terceiros com licença própria (por exemplo, crates do ecossistema Rust) | Segue a licença de cada biblioteca, que precisa ser conferida no desenho do painel |

**RISCO (alto, se ocorrer).** Um único arquivo copiado pode puxar o painel inteiro para a AGPL quando houver usuário externo. A correção depois exige reescrever o trecho ou abrir o código.

**INTERPRETAÇÃO (uso só interno).** Se o painel com código copiado ficasse só com os técnicos da MT, a seção 2 permite "make, run and propagate covered works that you do not convey, without conditions". Mas o painel vai ser integrado ao Helpdesk, que tem acesso de cliente, e a pergunta 5 prevê venda a terceiros. A exceção não serve de apoio.

### 3.4. Mudanças no cliente para ligar o painel

**INTERPRETAÇÃO.** Ligar o envio ao painel exige mudar o MapDesk-MT (`register-device`, endereço do servidor de API e, se for o caso, rotas novas). Essas mudanças entram no repositório público, sob a AGPL, com linha nova no `AVISO-DE-MODIFICACAO.md`. Isso não arrasta o painel: o cliente fica aberto e o servidor que o atende fica fechado, como já acontece com o Server Pro da RustDesk.

## 4. Pergunta 2: se a MT modificar o `hbbs`/`hbbr`

**FATO LEGAL (licença).** Seção 13: a versão modificada "must prominently offer all users interacting with it remotely through a computer network (if your version supports such interaction) an opportunity to receive the Corresponding Source of your version by providing access to the Corresponding Source from a network server at no charge". Incidência: a MT modificaria o programa e o rodaria na VPS, recebendo conexões de terceiros.

**FATO LEGAL (licença).** Seção 0: "Mere interaction with a user through a computer network, with no transfer of a copy, is not conveying." Incidência: rodar o servidor modificado sem entregar cópia não aciona as seções 4 a 6, só a 13.

**INTERPRETAÇÃO (incidência).** O `hbbs` é "expressly designed to accept user requests and send responses over a network" (`#AGPLv3InteractingRemotely`). Quem interage com ele são os programas MapDesk-MT nas máquinas dos clientes, operados por pessoas. Pela FAQ (`#AGPLv3ServerAsUser`), a pergunta é se há "reasonable expectation that a person will be interacting with the program remotely over a network". Há leitura de que o usuário do cliente só interage com o cliente, e não com o servidor. A leitura segura é tratar a seção 13 como aplicável, como a FAQ faz no caso da empresa com site (`#UnreleasedModsAGPL`).

**INTERPRETAÇÃO (o que cumprir).**

1. Publicar o código-fonte correspondente da versão modificada em servidor de rede, de graça: fork público (por exemplo, `manfredjr/rustdesk-server`) com tag para cada versão posta em produção.
2. O código inclui as bibliotecas modificadas e os roteiros de compilação e de imagem (Dockerfile) usados (seção 1; `#AGPLv3CorrespondingSource`).
3. Fazer a oferta de forma "prominent" a quem interage. O `hbbs` não tem tela; a FAQ aceita "a normal method of delivering messages to users" (`#AGPLProxy`). Os lugares naturais são a tela "Sobre" do MapDesk-MT (link "Código do servidor"), a página de download e o aviso de privacidade.
4. Manter o código disponível enquanto aquela versão estiver no ar.
5. Mudar só variáveis de ambiente, arquivos de configuração ou o `docker-compose` não é modificar o programa.

**RECOMENDAÇÃO.** Se a ideia for pôr no `hbbs` alguma função do painel, não fazer: isso leva a função para dentro do programa AGPL e para a seção 13. O painel fica em processo separado (item 3.1). Mexer no servidor do VPS-MT exige autorização prévia do Manfred (`AGENTS-MT.md`, Autonomia).

## 5. Pergunta 3: o repositório público basta? O que está cumprido e o que falta

**INTERPRETAÇÃO.** O repositório público é o meio certo, mas não basta sozinho. A seção 6(d) pede código "for as long as needed" no mesmo lugar do executável, com "clear directions next to the object code" (verificação de 05/10, item 2.3). Isso depende de tag, página da versão e página de download, que ainda não existem, porque nenhuma versão foi distribuída: `git tag` mostra só `1.5.0`, a do oficial.

### 5.1. Já cumprido (conferido nos arquivos em 06/10/2026)

| Requisito | Onde está |
|---|---|
| `LICENCE` do RustDesk na raiz, sem alteração | `LICENCE`; `git diff 1.5.0 -- LICENCE` vazio |
| Aviso de modificação com data e lista de mudanças | `AVISO-DE-MODIFICACAO.md`, tabela de 05/10 e 06/10/2026 |
| Termo da seção 7 sobre nomes e logotipos da MT | `AVISO-DE-MODIFICACAO.md`, "Nomes e logotipos" |
| Esquema de tag por versão e ligação tag e código | `AVISO-DE-MODIFICACAO.md`; `docs/publicacao.md` |
| Regra de nunca apagar tags e versões | `docs/publicacao.md`, "Depois de publicar", passo 3 |
| Tela "Sobre": versão MT e versão base, copyright da Purslane Tech, "Baseado no RustDesk", não oficial, sem garantia, permissão de redistribuir e modificar, link da licença, link do código da versão, link do site da MT | `desktop_setting_page.dart`, classe `_About`; `mt_info.dart` |
| Link de privacidade da RustDesk retirado; o da MT só aparece quando `kMtPrivacidade` tiver endereço | `_About`; `mt_info.dart` |
| Submódulo `hbb_common` apontando para o fork da MT, no commit do oficial | `.gitmodules`; `git submodule status` (`229b904...`) |
| Configuração em tempo de execução, sem alterar o `hbb_common` | `src/mt_config.rs`; isso esvazia a pendência 4 da verificação de 05/10 enquanto não houver mudança no submódulo |
| Fluxo de compilação público, sem segredos | `.github/workflows/mapdesk-windows.yml` |
| Página da versão com link do código da tag e aviso de AGPL e de não ser oficial | `mapdesk-windows.yml`, passo "Publish release", campo `body` |

### 5.2. Ainda falta

| # | O que falta | Base |
|---|---|---|
| 1 | Criar a tag `1.5.0-mt.1` no commit exato do executável distribuído e nunca apagá-la | 6(d) |
| 2 | Linha no `AVISO-DE-MODIFICACAO.md` com a data da versão publicada (passo 4 de `docs/publicacao.md`) | 5(a) |
| 3 | No texto da página da versão: lista de mudanças com data (ou link para o `AVISO-DE-MODIFICACAO.md` da tag) e indicação de que o código do submódulo está no fork `manfredjr/hbb_common`, commit `229b904...`. O pacote `.zip` que o GitHub gera para a tag não traz o conteúdo do submódulo | 5(a); 6(d), "clear directions" |
| 4 | Página de download do site: link do código da mesma versão ao lado do botão, link da licença, aviso de que não há garantia e de que não é produto oficial do RustDesk | 6(d); verificação de 05/10, item 7 |
| 5 | `README.md` da raiz: hoje é o do RustDesk, com o logotipo "RustDesk - Your remote desktop", e é ele que o GitHub mostra na página do repositório. Acrescentar no topo um bloco curto (ou trocar pelo `README-MT.md`) dizendo que é o MapDesk-MT, versão modificada, sob a AGPL-3.0, não oficial | 5(b); LPI, art. 195, verificação de 05/10, item 3.2 |
| 6 | Conferir origem, licença e disponibilidade do código dos binários que o fluxo baixa e empacota: motor Flutter de `rustdesk/engine`, `usbmmidd_v2` de `rustdesk-org/rdev` e driver de impressora de `rustdesk/hbb_common` (releases). Se forem parte da obra, o código precisa continuar disponível; guardar cópia ou fork | Seção 1, "Corresponding Source"; 6(d); pendência 8 |
| 7 | Não entregar a cliente executável de artefato de PR: o link "Código-fonte desta versão" aponta para a tag `kMtVersao`, que só existe depois da publicação | 6(d) |
| 8 | Endereço do aviso de privacidade em `kMtPrivacidade` | Verificação de privacidade; `docs/publicacao.md` |
| 9 | Aviso de copyright da MT, só depois de o Manfred confirmar | `AGENTS-MT.md` |

## 6. Pergunta 4: dados pessoais

**INTERPRETAÇÃO (só apontada).** O painel muda o enquadramento. Hoje o cliente manda ao servidor só o necessário para a conexão, e o envio ao servidor de API está desligado (verificação de privacidade, itens 3.1, 3.4 e 4.1). Com o painel, a MT passa a receber e guardar nome da máquina, nome do usuário do Windows, sistema, CPU, memória e o histórico de conexões, e a cruzar isso com o Inventário e o Helpdesk. Isso pede revisar: finalidade e necessidade (art. 6º, III, da LGPD, já analisado no item 4.1 daquela verificação para o cenário sem painel), papel da MT (controladora ou operadora, pendência 6 da verificação de 05/10), prazo de guarda e o texto do aviso de privacidade (o item 13 da tabela de sustentação do rascunho diz que só se fala com o servidor da MT e o técnico, sem dados do aparelho). A revisão fica para uma verificação de privacidade própria do painel (pendência 10). Esta verificação não a refaz.

## 7. Pergunta 5: venda do MapHub-MT como SaaS

### 7.1. (a) A AGPL impede ou condiciona vender o MapHub-MT fechado?

**FATO LEGAL (licença).** Seção 2: "unlimited permission to run the unmodified Program". Incidência: a MT rodaria o `hbbs`/`hbbr` sem modificação para prestar o serviço.

**FATO LEGAL (licença).** Seção 4: "You may charge any price or no price for each copy that you convey, and you may offer support or warranty protection for a fee." (verificação de 05/10, item 2.1). Seção 10: "you may not impose a license fee, royalty, or other charge for exercise of rights granted under this License". Incidência: a MT entregaria cópias do MapDesk-MT às empresas clientes.

**INTERPRETAÇÃO.**

1. A AGPL não impede vender o MapHub-MT fechado. Ele é programa separado (item 3.1), e o `hbbs`/`hbbr` sem modificação pode rodar, inclusive em serviço pago, sem a seção 13.
2. A condição é o que já vale no item 3: nenhum código do RustDesk dentro do MapHub-MT, e nenhuma função do MapHub-MT dentro do `hbbs`/`hbbr`.
3. O preço tem de recair sobre o serviço (MapHub-MT, hospedagem, suporte), e não sobre o direito de usar, copiar ou redistribuir o MapDesk-MT. A MT pode cobrar pela cópia que entrega, mas não pode, em contrato, proibir a empresa cliente de copiar, modificar ou repassar o MapDesk-MT, nem cobrar licença por máquina sobre ele (seção 10). Pode limitar, isso sim, o acesso ao MapHub-MT e ao servidor da MT.

**RISCO (médio).** Citar "RustDesk" na venda ("compatível com RustDesk") é uso comercial do nome. A LPI, art. 132, IV, só ressalva a citação "sem conotação comercial" (verificação de 05/10, item 3.2). Na venda, a origem aparece só como fato, nos avisos do MapDesk-MT, e não como argumento de venda do MapHub-MT.

### 7.2. (b) Entregar o MapDesk-MT ou uma variante com a marca do cliente

**FATO LEGAL (licença).** Seções 5 e 6 (verificação de 05/10, itens 2.2 e 2.3) e seção 10. Incidência: a MT transmite ("convey") cópia do MapDesk-MT a cada empresa cliente.

**INTERPRETAÇÃO.** O que a MT cumpre a cada entrega:

| Tema | O que fazer |
|---|---|
| Código correspondente | Para cada executável entregue, inclusive cada variante, o código da tag exata, com os recursos de marca do cliente, os roteiros de compilação e o submódulo, disponível a quem recebe, pelo tempo necessário (6(d)) |
| Avisos | `LICENCE`; copyright da Purslane Tech; "Baseado no RustDesk" e "não é produto oficial"; aviso de modificação com data da variante; tela "Sobre" com licença, garantia e link do código da variante |
| Seção 7 | O termo da MT continua valendo para o material da MT. Para o nome e o logotipo da empresa cliente, só ela, como titular, pode autorizar o termo 7(e) sobre o próprio material; pôr no contrato a autorização e a redação |
| Marca RustDesk | Nenhuma variante usa "RustDesk" no nome, ícone ou logotipo (verificação de 05/10, item 7) |
| Marca da MT nas variantes | É decisão da MT. Se quiser crédito, acrescentar termo 7(b) exigindo que o aviso de autoria da MT continue na tela "Sobre" |
| Marca do cliente | O logotipo do cliente que entra no código da variante fica sob a AGPL-3.0 como direito autoral (5(c)) para quem receber a cópia; o direito de marca não é licenciado. O cliente precisa saber disso antes de mandar o logotipo |
| Repasse pelo cliente | Quando a empresa cliente (por exemplo, uma empresa de TI) instala a variante nas máquinas dos clientes dela, é ela quem transmite. As obrigações das seções 4 a 6 passam a ser dela nessa entrega; a MT não responde por isso (seção 10, "You are not responsible for enforcing compliance by third parties"). Convém o contrato dizer isso e indicar onde está o código |

**INTERPRETAÇÃO (repositório por variante).** A licença não exige repositório público próprio para cada variante. A 6(d) exige acesso ao código para quem recebe o executável, do mesmo lugar. Mas quem recebe pode publicar o código (seção 10), então não há como manter a variante em segredo. O caminho mais simples e de menos erro é um só repositório público, com a marca de cada cliente em pasta própria e uma tag por variante e versão (por exemplo, `1.5.0-mt.1-<cliente>`), com o fluxo de compilação escolhendo a pasta. Se a MT preferir entregar o código só a quem recebe, a forma (repositório privado com acesso dado ao cliente, ou pacote do código junto do executável) tem de garantir acesso a todos os destinatários, inclusive os clientes finais da empresa de TI. É mais trabalhoso e não traz sigilo real.

### 7.3. (c) `hbbs`/`hbbr` modificado oferecido como serviço a terceiros

**INTERPRETAÇÃO.** Vale o item 4, agora com incidência mais clara: o serviço é oferecido a empresas e às pessoas que usam o MapDesk-MT nelas, e é o caso típico da seção 13 (`#UnreleasedModsAGPL`). A MT teria de publicar o código do servidor modificado, de graça, para todos os que interagem, e avisar de forma visível (tela "Sobre" do MapDesk-MT e das variantes, página do MapHub-MT, contrato). O MapHub-MT continua fechado se for processo separado. Se a modificação do `hbbs` só existir para servir o MapHub-MT, prefira resolver no MapHub-MT.

### 7.4. (d) Temas fora da licença, para verificações próprias

Só apontados, sem análise:

| Tema | O que verificar | Onde |
|---|---|---|
| LGPD | A MT como operadora de várias controladoras (as empresas clientes), contrato de tratamento com cada uma, a VPS e outros fornecedores como suboperadores, segurança e incidentes, transferência internacional se a VPS estiver fora do Brasil | Nova verificação de privacidade do MapHub-MT (pendência 10) |
| Contrato SaaS | Regime civil entre empresas e afastamento do CDC, a conferir caso a caso (a empresa cliente pode ser destinatária final do serviço); nível de serviço, limitação de responsabilidade, saída e devolução de dados, cláusulas sobre a AGPL do item 7.2 | Verificação de contrato própria (pendência 11) |
| Marco Civil | Se o MapHub-MT for "aplicação de internet" de provedor pessoa jurídica com fins econômicos, o art. 15 prevê guarda de "registros de acesso a aplicações de internet" por 6 meses; a incidência ao MapHub-MT não foi analisada | Mesma verificação do contrato ou de privacidade (pendência 12) |
| Tributação | Enquadramento do SaaS para ISS e demais tributos | Contador (pendência 13) |

Texto de apoio, sem análise de incidência: Lei nº 12.965/2014, art. 15, caput: "O provedor de aplicações de internet constituído na forma de pessoa jurídica e que exerça essa atividade de forma organizada, profissionalmente e com fins econômicos deverá manter os respectivos registros de acesso a aplicações de internet, sob sigilo, em ambiente controlado e de segurança, pelo prazo de 6 (seis) meses, nos termos do regulamento." Art. 5º, VIII: "registros de acesso a aplicações de internet: o conjunto de informações referentes à data e hora de uso de uma determinada aplicação de internet a partir de um determinado endereço IP." Fonte: biblioteca `legal-br`, coleta de 21/08/2026, consultada em 06/10/2026.

## 8. Requisitos para implementação

Painel (MapHub-MT):

- [ ] Escrever o painel do zero, em processo separado do `hbbs`/`hbbr` e do cliente; falar com o cliente só por HTTP e JSON.
- [ ] Escrever primeiro uma especificação do protocolo em palavras próprias, a partir da leitura do cliente; implementar a partir dela, sem colar código do RustDesk, `.proto`, cliente web nem `structs` copiadas.
- [ ] Conferir a licença de cada biblioteca de terceiros do painel no desenho.
- [ ] Não pôr função do painel dentro do `hbbs`/`hbbr`.
- [ ] Não usar "RustDesk" no nome, no logotipo nem na venda do MapHub-MT.
- [ ] Ligar o envio no cliente (`register-device`, servidor de API) por mudança no repositório público, com linha no `AVISO-DE-MODIFICACAO.md`, só depois da verificação de privacidade do painel e do aviso atualizado.

Servidor `hbbs`/`hbbr`, se um dia for modificado:

- [ ] Fork público com tag por versão em produção, com roteiros de compilação e imagem.
- [ ] Link "Código do servidor" na tela "Sobre" do MapDesk-MT e das variantes, na página de download e no aviso de privacidade.
- [ ] Autorização do Manfred antes de mexer no servidor do VPS-MT.

Distribuição do MapDesk-MT (itens do 5.2):

- [ ] Tag `1.5.0-mt.1` no commit do executável, nunca apagada.
- [ ] Linha com a data da versão no `AVISO-DE-MODIFICACAO.md`.
- [ ] Página da versão com mudanças e data (ou link do aviso) e indicação do fork e commit do `hbb_common`.
- [ ] Página de download com link do código ao lado do botão, licença, sem garantia, não oficial.
- [ ] Bloco do MapDesk-MT no topo do `README.md` da raiz (ou troca pelo `README-MT.md`).
- [ ] Conferir e guardar o código dos binários baixados no fluxo (motor Flutter, `usbmmidd_v2`, driver de impressora).
- [ ] Não entregar artefato de PR a cliente.
- [ ] `kMtPrivacidade` preenchido.

Venda a empresas e variantes com marca do cliente:

- [ ] Cobrar pelo serviço, não pelo direito de usar ou repassar o MapDesk-MT; nenhuma cláusula que restrinja direitos da AGPL.
- [ ] Uma tag e o código completo por variante, com a marca do cliente em pasta própria; preferir o repositório público único.
- [ ] Contrato com: autorização e termo 7(e) do cliente sobre a marca dele, ciência de que o logotipo entra sob a AGPL como direito autoral, aviso de que o repasse a terceiros põe nele as obrigações das seções 4 a 6, e onde está o código.
- [ ] Decidir se a MT exige crédito nas variantes (termo 7(b)).

## 9. Pendências de validação

Continuam a numeração do projeto (pendências 1 a 6 na verificação de 05/10).

| # | Pendência | Onde | Quem |
|---|---|---|---|
| 7 | Reconferir no Planalto o texto vigente da Lei nº 9.610/1998, art. 8º, I, e art. 7º, § 1º (lidos na biblioteca local, coleta de 21/08/2026; Planalto fora do ar em 06/10/2026). Não muda a conclusão, que se apoia na licença | itens 1.2 e 3.2 | Agente, próxima consulta |
| 8 | Origem, licença e disponibilidade do código dos binários que o fluxo baixa e empacota (`rustdesk/engine`, `usbmmidd_v2`, driver de impressora) e se fazem parte do código correspondente | item 5.2, linha 6 | Agente, antes da primeira publicação |
| 9 | Licença e origem do cliente web do RustDesk, só se a MT quiser reaproveitá-lo | item 3.3 | Agente, se for o caso |
| 10 | Verificação de privacidade do painel e do MapHub-MT: dados novos, papel da MT perante cada empresa cliente, suboperadores, prazo, aviso | itens 6 e 7.4 | Agente; pode somar à pendência 6 da consulta ao advogado |
| 11 | Verificação do contrato SaaS (regime civil ou CDC, cláusulas da AGPL do item 7.2) | item 7.4 | Agente, depois advogado no resíduo |
| 12 | Incidência do Marco Civil, art. 15, ao MapHub-MT | item 7.4 | Agente |
| 13 | Tributação do SaaS (ISS e outros) | item 7.4 | Contador |

A fronteira entre programas separados (item 3.1) fica registrada como RISCO baixo e não como pendência: a recomendação de escrever o painel do zero, em processo separado, já elimina o efeito prático da dúvida.
