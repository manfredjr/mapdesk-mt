# Verificação jurídica: privacidade no cliente MapDesk

Data: 05/10/2026. Projeto MAPDESK-MT. Feita com a skill `legal-br`.

Cobre só o que é próprio do cliente MapDesk: que dados o programa trata, quem é controlador e operador na sessão de suporte, e o que precisa aparecer na tela e na página de download. O servidor já foi analisado no projeto VPS-MT e aqui só é referenciado.

Licença e marcas ficam em `verificacao-licenca-agpl-e-marcas-2026-10-05.md`. Pontos que dependem de parecer ficam em `CONSULTA-ADVOGADO-mapdesk-agpl-marca-2026-10-05.md`.

## 1. Contexto e premissas

### 1.1. Fatos

| Fato | Fonte |
|---|---|
| O MapDesk é fork do RustDesk 1.5.0, distribuído gratuitamente pela MANFRED TECNOLOGIA LTDA, CNPJ 21.075.901/0001-12, aos clientes do suporte remoto | `AGENTS-MT.md`; pedido do Manfred |
| O cliente fala só com o servidor de ID e repasse da MT (`rustdesk.manfred.com.br`), com a chave pública da MT embutida | pedido do Manfred; briefing do projeto, seção 4 |
| Servidor de API desligado: o cliente não envia dados a nenhum servidor de API | pedido do Manfred; `.superpowers/rascunho/achados-codigo-1.5.0.md`, seção "O que o register-device = N desliga" |
| Aprovação por clique como padrão (`approve-mode` = "click") | pedido do Manfred; `achados-codigo-1.5.0.md`, seção "Aprovação por clique" |
| O servidor registra ID, IP e horário das máquinas e guarda por 6 meses; não grava conteúdo de sessão | `C:\COWORK\CODE\VPS-MT\docs\legal\verificacao-servidor-rustdesk-2026-10-04.md`, itens 3.3 e 4 |
| Clientes: empresas e pessoas físicas, cerca de 150 a 200 máquinas Windows | mesma verificação do VPS-MT, item 1 |

### 1.2. Premissas de incidência

| Premissa | O que aciona | Fundamento |
|---|---|---|
| Há tratamento de dados pessoais | LGPD | ID, identificador único do aparelho e IP ligados à máquina de uma pessoa física, ou de um empregado identificável de cliente empresa, são "informação relacionada a pessoa natural identificada ou identificável" (art. 5º, I). A imagem da tela durante a sessão também pode conter dados pessoais |
| O tratamento ocorre no Brasil | LGPD, art. 3º, I | Art. 3º: a lei se aplica "desde que: I - a operação de tratamento seja realizada no território nacional;". Máquinas, técnico e servidor estão no Brasil |
| Não há público infantil | Afasta a LGPD, art. 14, e o ECA Digital | O programa é para clientes do suporte técnico da MT, empresas e adultos. Se o técnico atender máquina de uso de criança, é caso de atendimento, não de desenho do produto |
| Dado sensível pode aparecer por acaso na tela | Atenção à LGPD, art. 11, sem incidência direta no programa | O programa não coleta dado sensível. A tela do cliente pode mostrar, por exemplo, exames ou dados de saúde. Ver item 4.5 |

### 1.3. Fontes consultadas em 05/10/2026

| Fonte | Onde |
|---|---|
| LGPD (Lei nº 13.709/2018), arts. 3º, 5º, 6º, 7º, 9º, 18, 39 e 46 | https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709compilado.htm; cópia em `.superpowers/rascunho/lgpd.html`, SHA-256 `7064d53d3e5e66f7d5fbc2d2eb2ffc031192154960bfcc7561d00aa1420c21ba` |
| Marco Civil da Internet (Lei nº 12.965/2014), arts. 5º e 7º | https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2014/lei/l12965.htm; cópia em `.superpowers/rascunho/mci.html`, SHA-256 `1b9620b920927b6f29ed2033bf4f75a111fa4b0fe6e56eb938dba1e5b9b33199` |
| Código do RustDesk 1.5.0: `src/common.rs` (`check_software_update`, linha 1020; `is_custom_client`, linha 2560) | https://github.com/rustdesk/rustdesk/blob/1.5.0/src/common.rs |
| `hbb_common`, commit `229b904...`: `src/lib.rs` (`version_check_request`, linha 510) e `protos/rendezvous.proto` (`RegisterPeer`, linha 15; `RegisterPk`, linha 112) | https://github.com/rustdesk/hbb_common |
| Tela "Sobre" do RustDesk 1.5.0 | `flutter/lib/desktop/pages/desktop_setting_page.dart`, classe `_About`, tag `1.5.0` |
| Verificação do servidor no VPS-MT, de 04/10/2026 | `C:\COWORK\CODE\VPS-MT\docs\legal\verificacao-servidor-rustdesk-2026-10-04.md` |
| Briefing da página de download, de 05/10/2026 | `C:\COWORK\CODE\VPS-MT\.superpowers\rascunho\briefing-site-mt-pagina-acesso.md`, seção "PRIVACIDADE" |

A biblioteca local da `legal-br` não tem `STATUS-FONTES.md`; por isso a LGPD e o Marco Civil foram conferidos no Planalto em 05/10/2026. O texto da LGPD no Planalto traz nova redação do art. 5º, VIII, dada pela Lei nº 15.352/2026; o inciso não é usado aqui.

### 1.4. O que já está resolvido no VPS-MT e não se refaz

| Tema | Onde | Situação |
|---|---|---|
| Base legal do tratamento no servidor | VPS-MT, item 3.1 | Interpretação registrada: art. 7º, V, para pessoa física; para empregado de cliente empresa, depende do papel da MT |
| Transferência internacional (Hostinger) | VPS-MT, item 3.2 | Risco aceito pelo Manfred em 04/10/2026 |
| Guarda de 6 meses dos registros (Marco Civil, art. 15) | VPS-MT, item 3.3 | Adotada por cautela; enquadramento em risco aceito |
| Medidas de segurança do servidor (LGPD, art. 46) | VPS-MT, item 4 | Requisitos do servidor |
| Sessão de suporte como tratamento do serviço, não do servidor | VPS-MT, item 3.5 | Ficou como pendência fora daquele projeto; retomada aqui no item 4.3 |

## 2. Texto legal usado

**LGPD, art. 5º:** "Para os fins desta Lei, considera-se:" "I - dado pessoal: informação relacionada a pessoa natural identificada ou identificável;" "II - dado pessoal sensível: dado pessoal sobre origem racial ou étnica, convicção religiosa, opinião política, filiação a sindicato ou a organização de caráter religioso, filosófico ou político, dado referente à saúde ou à vida sexual, dado genético ou biométrico, quando vinculado a uma pessoa natural;" "VI - controlador: pessoa natural ou jurídica, de direito público ou privado, a quem competem as decisões referentes ao tratamento de dados pessoais;" "VII - operador: pessoa natural ou jurídica, de direito público ou privado, que realiza o tratamento de dados pessoais em nome do controlador;" "X - tratamento: toda operação realizada com dados pessoais, como as que se referem a coleta, produção, recepção, classificação, utilização, acesso, reprodução, transmissão, distribuição, processamento, arquivamento, armazenamento, eliminação, avaliação ou controle da informação, modificação, comunicação, transferência, difusão ou extração;"

**LGPD, art. 6º:** "As atividades de tratamento de dados pessoais deverão observar a boa-fé e os seguintes princípios:" "III - necessidade: limitação do tratamento ao mínimo necessário para a realização de suas finalidades, com abrangência dos dados pertinentes, proporcionais e não excessivos em relação às finalidades do tratamento de dados;" "VI - transparência: garantia, aos titulares, de informações claras, precisas e facilmente acessíveis sobre a realização do tratamento e os respectivos agentes de tratamento, observados os segredos comercial e industrial;"

**LGPD, art. 9º, caput e incisos:** "O titular tem direito ao acesso facilitado às informações sobre o tratamento de seus dados, que deverão ser disponibilizadas de forma clara, adequada e ostensiva acerca de, entre outras características previstas em regulamentação para o atendimento do princípio do livre acesso:" "I - finalidade específica do tratamento;" "II - forma e duração do tratamento, observados os segredos comercial e industrial;" "III - identificação do controlador;" "IV - informações de contato do controlador;" "V - informações acerca do uso compartilhado de dados pelo controlador e a finalidade;" "VI - responsabilidades dos agentes que realizarão o tratamento; e" "VII - direitos do titular, com menção explícita aos direitos contidos no art. 18 desta Lei."

**LGPD, art. 39:** "O operador deverá realizar o tratamento segundo as instruções fornecidas pelo controlador, que verificará a observância das próprias instruções e das normas sobre a matéria."

**LGPD, art. 46, caput:** "Os agentes de tratamento devem adotar medidas de segurança, técnicas e administrativas aptas a proteger os dados pessoais de acessos não autorizados e de situações acidentais ou ilícitas de destruição, perda, alteração, comunicação ou qualquer forma de tratamento inadequado ou ilícito."

**Marco Civil, art. 7º, caput, VIII e IX:** "O acesso à internet é essencial ao exercício da cidadania, e ao usuário são assegurados os seguintes direitos:" "VIII - informações claras e completas sobre coleta, uso, armazenamento, tratamento e proteção de seus dados pessoais, que somente poderão ser utilizados para finalidades que: a) justifiquem sua coleta; b) não sejam vedadas pela legislação; e c) estejam especificadas nos contratos de prestação de serviços ou em termos de uso de aplicações de internet;" "IX - consentimento expresso sobre coleta, uso, armazenamento e tratamento de dados pessoais, que deverá ocorrer de forma destacada das demais cláusulas contratuais;"

## 3. O que o MapDesk trata

### 3.1. Dados enviados ao servidor da MT

**FATO (código).** No `hbb_common` (commit `229b904...`, `protos/rendezvous.proto`), as mensagens de registro do cliente no servidor de ID são:

- `RegisterPeer`: `string id`, `int32 serial`;
- `RegisterPk`: `string id`, `bytes uuid`, `bytes pk`, `string old_id`, `bool no_register_device`.

O IP de origem chega ao servidor pela própria conexão.

**FATO (código).** No mesmo arquivo, as mensagens de montagem da conexão levam também a versão do programa (`PunchHoleRequest`, `LocalAddr`), o tipo de NAT, endereços de socket IPv4 e IPv6 e, em `LocalAddr`, o campo `bytes local_addr` (endereço na rede local). Há ainda a mensagem `PeerDiscovery`, com `mac`, `id`, `username`, `hostname` e `platform`.

**INTERPRETAÇÃO.** O cliente envia ao servidor da MT o ID, um identificador único do aparelho (`uuid`), a chave pública do aparelho (`pk`), a versão do programa, o tipo de NAT e os endereços pública e local da máquina, e o servidor vê o IP e o horário. As mensagens de registro e de conexão não têm campo de nome da máquina nem de nome do usuário. Pelos campos e pelo nome, `PeerDiscovery` serve à descoberta de máquinas na rede local, e não ao servidor, mas o código que a envia não foi lido. O que o servidor guarda e por quanto tempo está na verificação do VPS-MT (ID, IP e horário, 6 meses). Que o nome da máquina chegue ao servidor, como dizia o pedido, não se confirmou nas mensagens. Fica para o teste do item 6, junto com o destino da `PeerDiscovery`.

### 3.2. Dados da sessão de suporte

**INTERPRETAÇÃO.** Durante a sessão, aceita por clique, o técnico recebe a imagem da tela e controla teclado e mouse. Conforme o uso, também transfere arquivos e troca mensagens. Os dados passam diretamente entre as máquinas ou pelo repasse (`hbbr`) da MT, que não grava o conteúdo (verificação do VPS-MT, item 4). Na abertura da sessão, a máquina do cliente também informa ao técnico dados do aparelho. Quais exatamente (nome da máquina, nome do usuário do Windows, sistema operacional) não foi conferido no código e fica para o teste do item 6. Tudo isso é "tratamento" (art. 5º, X: "acesso", "transmissão", "utilização"), mesmo sem gravação.

### 3.3. Dados que ficam na máquina

**INTERPRETAÇÃO.** Configuração, registros locais (logs) e a senha do aparelho, se houver, ficam na própria máquina do cliente. A MT não recebe esses dados, salvo o que o técnico vir durante a sessão. Distribuir o programa não faz da MT agente de tratamento do que o programa guarda localmente sem enviar a ela.

### 3.4. O que o MapDesk não pode enviar a terceiros

**FATO (código).** Em `src/common.rs` (tag `1.5.0`), `check_software_update` retorna sem consultar nada quando `is_custom_client()` é verdadeiro, e `is_custom_client()` é `get_app_name() != "RustDesk"`. Sem esse desvio, a consulta de versão envia a `https://api.rustdesk.com/version/latest` o sistema operacional, a versão do sistema, a arquitetura e um `device_id` tirado da impressão digital do aparelho (`hbb_common`, `src/lib.rs`, `version_check_request`).

**FATO (código).** Pelo levantamento do projeto (`achados-codigo-1.5.0.md`), sem servidor de API configurado o cliente usa o servidor de ID na porta 21114, e sem servidor personalizado cai em `https://admin.rustdesk.com`; `register-device` = "N" deixa o servidor de API vazio.

**FATO (código).** A tela "Sobre" do RustDesk 1.5.0 abre `https://rustdesk.com/privacy.html` no link "Privacy Statement".

**INTERPRETAÇÃO.** Com o nome "MapDesk" (diferente de "RustDesk") e `register-device` = "N", o cliente não manda dados à RustDesk. Esse resultado depende de dois detalhes de implementação. Se algum deles falhar, o programa passa a enviar identificador do aparelho a terceiro no exterior, e isso mudaria a análise inteira (compartilhamento, transferência internacional e aviso). Daí o teste obrigatório do item 6. O link de privacidade da RustDesk, por sua vez, informaria ao titular um controlador errado (art. 9º, III).

## 4. Análise

### 4.1. Finalidade e necessidade

**INTERPRETAÇÃO.** A finalidade é uma só: permitir o suporte remoto que o cliente pediu. ID, `uuid`, chave pública, IP e horário servem para localizar a máquina e montar a conexão. Desligar o servidor de API e a consulta de versão atende ao princípio da necessidade (art. 6º, III): o programa não manda nada além do que a conexão exige.

### 4.2. Base legal

**INTERPRETAÇÃO.** Vale o que o VPS-MT registrou no item 3.1 para o servidor. Na sessão, o mesmo raciocínio se aplica. Para o cliente pessoa física, o tratamento é necessário à execução do contrato de suporte de que ele é parte (art. 7º, V). Para o empregado de cliente empresa, o empregado não é parte do contrato, e a base depende do papel da MT (item 4.3). Nenhuma das hipóteses depende de consentimento. O clique de aprovação é controle de acesso e transparência, não base legal.

### 4.3. Controlador e operador na sessão

**INTERPRETAÇÃO.** Cenários:

| Cenário | Quem decide o tratamento | Papel provável da MT |
|---|---|---|
| Cliente pessoa física pede suporte no próprio computador | A própria pessoa e a MT, para prestar o serviço contratado | Controladora dos dados do cliente que trata para o suporte |
| Cliente empresa contrata suporte para máquinas usadas por empregados | A empresa decide que suas máquinas recebem suporte e o que se faz nelas | Operadora (art. 5º, VII), tratando "em nome do controlador" e "segundo as instruções" dele (art. 39) |
| Servidor da MT (ID, IP, horário) | A MT, que define o servidor e a guarda | Controladora (VPS-MT, item 2) |

No cenário da empresa, a MT trata por conta do cliente o que aparece na tela: dados dos empregados, de clientes do cliente e de terceiros. Ser operadora pede instruções do controlador por escrito, ou seja, um contrato de suporte com cláusula de tratamento de dados. Hoje esse contrato não existe por escrito (VPS-MT, item 3.5). Para os registros do servidor, a MT continua controladora mesmo atendendo a empresa. Ela pode ter papéis diferentes para finalidades diferentes.

**PENDÊNCIA DE VALIDAÇÃO 6.** Confirmar o papel da MT na sessão de suporte a cliente empresa, a base legal aplicável aos empregados e o conteúdo mínimo da cláusula de dados no contrato de suporte. Vem do item 3.5 do VPS-MT e é a questão 4 da consulta.

### 4.4. Transparência: o que o titular precisa saber

**FATO LEGAL.** LGPD, art. 9º (transcrito no item 2). Incidência: o art. 9º é direito do titular frente a quem trata. Para os registros do servidor, a MT é controladora (VPS-MT, item 2), e o aviso cabe a ela. Para o conteúdo da sessão de cliente empresa, se a MT for operadora, o dever de informar é da empresa controladora, mas o aviso da MT ajuda a empresa a cumpri-lo.

**INTERPRETAÇÃO.** O titular típico é quem está na frente da máquina: o próprio cliente ou o empregado. Ele vê o MapDesk e, talvez, a página de download. Os lugares em que o aviso alcança essa pessoa são a página de download, a tela "Sobre" e a janela de aprovação da conexão.

**FATO LEGAL.** Marco Civil, art. 7º, VIII e IX (transcritos no item 2). Incidência: o art. 7º assegura direitos "ao usuário" de internet. O inciso VIII alcança quem coleta dados pessoais do usuário na internet, como o servidor da MT faz.

**INTERPRETAÇÃO.** O inciso VIII se cumpre com o aviso do item 5. O inciso IX fala em "consentimento expresso" sobre coleta e tratamento. A LGPD, posterior e específica, admite tratamento sem consentimento (art. 7º, II a X). Há uma leitura de que o inciso IX convive com a LGPD e exige consentimento destacado em aplicação de internet. Há outra de que a LGPD rege as bases legais e o inciso IX só vale quando o consentimento for a base escolhida. A verificação do VPS-MT não tratou o ponto. Se valer a primeira leitura, o MapDesk ou a página de download precisariam de um aceite destacado antes do primeiro uso.

**PENDÊNCIA DE VALIDAÇÃO 5.** Alcance do Marco Civil, art. 7º, IX, depois da LGPD, para o registro de ID, IP e horário no servidor da MT. É a questão 3 da consulta. Até a resposta, a recomendação é o aviso do item 5 sem caixa de consentimento: um consentimento colhido sem necessidade cria a expectativa de que, retirado, o serviço para, e o suporte não funciona sem os registros.

### 4.5. Segurança e controle do titular

**FATO LEGAL.** LGPD, art. 46, caput (transcrito no item 2). Incidência: a MT é agente de tratamento nos dois papéis possíveis (item 4.3).

**INTERPRETAÇÃO.** No cliente, as medidas que pesam são:

- aprovação por clique como padrão: ninguém vê a tela sem que a pessoa na frente da máquina aceite;
- só o servidor e a chave da MT embutidos: o programa não se liga a outro servidor sem mudança de configuração;
- nenhuma senha permanente definida de fábrica: acesso sem a pessoa presente só se o cliente configurar;
- dado sensível na tela: o programa não o coleta, mas o técnico pode vê-lo. A regra operacional é pedir que a pessoa feche o que não tem relação com o atendimento antes de aceitar.

**RECOMENDAÇÃO.** Para o padrão "click", usar `DEFAULT_SETTINGS`, que o usuário pode mudar, e não `OVERWRITE_SETTINGS`, que trava a opção (`achados-codigo-1.5.0.md`). Clientes empresa que queiram acesso sem presença (por senha) passam a decidir isso por escrito. Travar a opção é escolha de produto, não exigência legal.

## 5. Aviso de privacidade: conteúdo mínimo

**RECOMENDAÇÃO.** Um texto curto, igual na página de download e no link "Aviso de privacidade" da tela "Sobre" (no lugar do link da RustDesk). O texto passa pela `humanizar-ptbr` antes de publicar. Itens, com a base de cada um:

| Item | Conteúdo | Base |
|---|---|---|
| Quem trata | MANFRED TECNOLOGIA LTDA (MT - Manfred Tecnologia), CNPJ 21.075.901/0001-12 | Art. 9º, III |
| Contato | [PREENCHER: e-mail para titulares de dados] e encarregado [PREENCHER: nome ou canal do encarregado] | Art. 9º, IV |
| Para quê | Permitir o suporte remoto pedido pelo cliente | Art. 9º, I |
| O que o servidor registra | ID do computador, endereço IP e horário de cada conexão; acrescentar o identificador do aparelho e o endereço local se o teste do item 6 mostrar que o servidor os guarda | Art. 9º, II; item 3.1 |
| Por quanto tempo | 6 meses, com acesso restrito | Art. 9º, II; VPS-MT, item 3.3 |
| O que não é gravado | A tela e o conteúdo da sessão não são gravados no servidor | Art. 6º, VI |
| Controle de quem está na máquina | O técnico só vê a tela depois que a pessoa clica em "Aceitar"; a sessão pode ser encerrada a qualquer momento | Art. 6º, VI |
| Compartilhamento | O programa não envia dados à RustDesk nem a outros terceiros. O servidor fica em provedor de hospedagem contratado pela MT | Art. 9º, V; VPS-MT, item 3.2 |
| Cliente empresa | Quando o computador é da empresa, a MT atende por conta dela, e as dúvidas sobre o uso do equipamento podem ser levadas também à empresa | Art. 9º, VI; item 4.3 (depende da pendência 6) |
| Direitos | Direitos do art. 18 da LGPD, com o canal de contato | Art. 9º, VII |
| Política completa | [PREENCHER: endereço da política de privacidade da MT] | Art. 6º, VI |

O briefing da página de download (VPS-MT, seção "PRIVACIDADE") já previa os itens "o que o servidor registra", "6 meses" e "não grava a tela". Este quadro completa com os itens do art. 9º. O texto final da página é verificado na sessão do site-mt, com arquivo em `docs/legal/` daquele projeto.

## 6. Requisitos para implementação

Programa:

- [ ] Nome do aplicativo diferente de "RustDesk" (desliga a consulta de versão em `api.rustdesk.com`).
- [ ] `register-device` = "N" em `BUILTIN_SETTINGS` (servidor de API vazio).
- [ ] Teste de rede antes da primeira versão: instalar, abrir, ficar ocioso, fazer uma sessão e abrir a tela "Sobre", registrando todas as conexões de saída. Critério: nenhuma conexão a `*.rustdesk.com` nem a outro destino que não `rustdesk.manfred.com.br` (portas 21115 a 21117) e a outra ponta da sessão. Guardar o resultado no repositório.
- [ ] No mesmo teste, anotar o que o técnico recebe da máquina na abertura da sessão (nome da máquina, usuário do Windows, sistema), o que o servidor guarda (em especial `uuid` e endereço local) e para onde vai a mensagem `PeerDiscovery`. Atualizar o item 3 e o aviso do item 5 se algo diferir.
- [ ] Aprovação por clique como padrão, em `DEFAULT_SETTINGS`.
- [ ] Nenhuma senha permanente definida de fábrica.
- [ ] Tela "Sobre": trocar `https://rustdesk.com/privacy.html` pelo aviso de privacidade da MT.
- [ ] Repetir o teste de rede a cada versão que juntar mudanças do RustDesk oficial.

Página de download e textos:

- [ ] Publicar o aviso do item 5 na página de download, perto do botão.
- [ ] Preencher os campos [PREENCHER] do item 5 (e-mail para titulares, encarregado, endereço da política).
- [ ] Não colocar caixa de consentimento até a resposta da pendência 5.

Contrato e operação:

- [ ] Cláusula de tratamento de dados no contrato de suporte com clientes empresa (pendência 6).
- [ ] Orientação do técnico: pedir ao usuário que feche o que não tem relação com o atendimento antes de aceitar a sessão.

## 7. Pendências de validação

O total do projeto é 6, com a mesma numeração na verificação de licença e marcas e na consulta ao advogado. Neste arquivo estão as pendências 5 e 6. As pendências 1 a 4 estão em `verificacao-licenca-agpl-e-marcas-2026-10-05.md`, seção 5.

## 8. Pontos pendentes de parecer jurídico

Esta verificação tem **2 pontos** que não foi possível validar em fonte oficial (pendências 5 e 6 do total de 6 do projeto). Os demais foram verificados e estão nas fontes da seção 1.3.

Encaminhado para parecer em `CONSULTA-ADVOGADO-mapdesk-agpl-marca-2026-10-05.md`, questões 3 e 4.

| # | Ponto | Onde aparece | Por que não foi possível concluir |
|---|---|---|---|
| 5 | Marco Civil, art. 7º, IX, depois da LGPD | item 4.4 | Há duas leituras plausíveis, com impacto no aceite |
| 6 | Papel da MT na sessão de cliente empresa e base legal para empregados | item 4.3 | Depende do contrato de suporte, que não existe por escrito |

**Não utilize esta verificação nesses pontos específicos antes do parecer.** O restante está verificado.
