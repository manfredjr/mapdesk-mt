# Rascunho: aviso de privacidade do MapDesk-MT

Data: 05/10/2026. Projeto MAPDESK-MT. Feito com a skill `legal-br`.

**Situação: RASCUNHO. Não publicar.** Destino: página de download do site-mt e link "Aviso de privacidade" da tela Sobre (`kMtPrivacidade` em `flutter/lib/mt/mt_info.dart`, hoje vazio).

Base: `docs/legal/verificacao-privacidade-cliente-2026-10-05.md` (seções 3 a 5), `docs/legal/CONSULTA-ADVOGADO-mapdesk-agpl-marca-2026-10-05.md` (questões 3 e 4), `C:\COWORK\CODE\VPS-MT\docs\legal\verificacao-servidor-rustdesk-2026-10-04.md`, `C:\COWORK\CODE\VPS-MT\docs\contratacao-hostgator.md`, `C:\COWORK\CODE\VPS-MT\docs\superpowers\pendencias.md`, `C:\COWORK\CODE\VPS-MT\servidor\registros\vps-mt.conf` e a biblioteca `legal-br` (`fontes-md/leis/03-lgpd...`, `04-marco-civil...`, `fontes-md/anpd/39-resolucao-anpd-2-2022...`).

### O que impede publicar

| # | Pendência | Onde fecha |
|---|---|---|
| 1 | Questão 3 da consulta: se o Marco Civil, art. 7º, IX, exige aceite destacado. Até a resposta, sem caixa de consentimento | Parecer do advogado |
| 2 | Questão 4 da consulta: papel da MT e base legal no computador de cliente empresa | Parecer do advogado e contrato de suporte |
| 3 | Campos `[PREENCHER]`: contato do titular, encarregado ou canal, provedor, prazo do cadastro, prazo de resposta, versão e data | Manfred |
| 4 | Teste de rede no executável compilado ainda não rodou (só o roteiro foi testado, sem o programa aberto). As frases "não manda dados à RustDesk" e a lista de dados enviados dependem dele | `ferramentas-mt/teste-rede.ps1` com resultado "OK" guardado no repositório |
| 5 | Não se sabe ainda se o servidor guarda o identificador do aparelho e o endereço local, nem o que o técnico recebe do aparelho ao abrir a sessão (`[FONTE?]` no texto) | Mesmo teste, item 6 da verificação de privacidade |
| 6 | O servidor ainda não está em produção. O provedor mudou de Hostinger para HostGator Brasil LTDA (Oracle Cloud, São Paulo), mas a verificação do VPS-MT ainda analisa a Hostinger como operadora e a transferência internacional. O contrato com a HostGator está em disputa, com prazo até 07/10/2026 | Verificação do VPS-MT atualizada para o provedor real |
| 7 | Segurança do servidor: em 04/10/2026 a VPS tinha login por senha e do root ligados, `ufw` inativo e chaves de terceiros (`# keyserv`) no root. As medidas da seção "Segurança" só entram no texto depois de aplicadas e conferidas | `VPS-MT/docs/instalacao.md`, passos D, E e F |
| 8 | Registros de conexão direta (sem repasse) ainda não conferidos; `SystemMaxUse=2G` pode apagar registro antes de 6 meses | Pendências do VPS-MT ("Guarda de registros" e "Uso do journal") |
| 9 | O compromisso "a MT não grava a tela" vale para o servidor (fato) e para o técnico (prática). O lado do técnico no RustDesk tem gravação de sessão; confirmar que fica desligada | Manfred |
| 10 | Texto final passa pela `humanizar-ptbr` | Antes de publicar |

---

## Texto do aviso (para a página)

# Aviso de privacidade do MapDesk-MT

Versão [PREENCHER: número da versão], de [PREENCHER: data].

O MapDesk-MT é o programa de acesso remoto que a MT - Manfred Tecnologia usa no suporte técnico aos seus clientes. Este aviso explica o que o programa e o servidor da MT fazem com os seus dados. Ele não trata do site da MT nem de outros serviços.

## Quem cuida dos seus dados

MANFRED TECNOLOGIA LTDA, CNPJ 21.075.901/0001-12, que atua como MT - Manfred Tecnologia.

Contato para assuntos de dados pessoais: [PREENCHER: e-mail para titulares de dados].

Encarregado: [PREENCHER: nome e contato do encarregado, ou o canal de atendimento ao titular, se a MT se enquadrar como agente de pequeno porte e não indicar encarregado].

## Para que usamos

Só para o suporte remoto que você ou a sua empresa pediu: achar o seu computador, ligar o computador do técnico ao seu e manter a sessão funcionando. Não usamos esses dados para nenhuma outra finalidade.

## Quais dados

**O que o servidor da MT registra:**

- o número de identificação (ID) do computador no MapDesk-MT;
- o endereço IP de onde o computador se conecta;
- a data e o horário em que o computador se cadastra no servidor;
- quando a sessão passa pelo servidor de repasse da MT: os endereços IP, a abertura e o fechamento da sessão.

**O que o programa envia para montar a conexão:** além do ID, um identificador do aparelho, a chave pública do aparelho, a versão do programa, o tipo de rede e o endereço do computador na rede local. [FONTE?: confirmar no teste quais desses dados o servidor guarda.]

**Durante a sessão:** depois que você aceita, o técnico vê a sua tela e pode usar o teclado e o mouse. Quando for preciso, também troca arquivos e mensagens com você. Ao abrir a sessão, o técnico recebe alguns dados do computador. [FONTE?: confirmar no teste quais, por exemplo nome do computador, nome do usuário do Windows e sistema operacional.]

**O que fica só no seu computador:** as configurações, os registros do programa e a senha de acesso, se houver. A MT não recebe esses dados, a não ser o que o técnico vê na tela durante o atendimento.

Antes de aceitar a sessão, feche o que não tem a ver com o atendimento, como e-mails, documentos pessoais ou exames.

## O que não fazemos

- A MT não grava a sua tela nem o conteúdo da sessão. O servidor guarda só os registros listados acima.
- O programa não manda dados à RustDesk nem a outra empresa. Ele só se comunica com o servidor da MT (`rustdesk.manfred.com.br`) e com o computador do técnico.

## Você controla o acesso

- Por padrão, o técnico só vê a sua tela depois que alguém na frente do computador aceita o pedido de conexão.
- Você pode encerrar a sessão a qualquer momento.
- O programa vem sem senha permanente. O acesso sem ninguém na frente do computador só funciona se uma senha for configurada naquele computador.

## Por que podemos tratar esses dados

Quando você é cliente pessoa física, o tratamento é necessário para cumprir o contrato de suporte que você tem com a MT (Lei nº 13.709/2018, a LGPD, art. 7º, V).

[DEPENDE DA CONSULTA, questão 4: base legal quando o computador é de empresa cliente e quem o usa é empregado dela.]

[DEPENDE DA CONSULTA, questão 3: se for preciso aceite destacado pelo Marco Civil da Internet, art. 7º, IX, este trecho e a página de download mudam. Até a resposta, não há caixa de consentimento.]

## Quando o computador é da sua empresa

[DEPENDE DA CONSULTA, questão 4: papel da MT no atendimento a cliente empresa. Rascunho sujeito ao parecer: "Quando o computador é da empresa em que você trabalha, a MT atende a pedido dela. Dúvidas sobre o uso do equipamento também podem ser levadas à empresa."]

## Por quanto tempo guardamos

- Os registros de acesso ao servidor (ID, IP, data e horário) ficam guardados por 6 meses, com acesso restrito, e depois são apagados automaticamente. Eles só ficam mais tempo se uma autoridade pedir a guarda ou se houver ordem judicial.
- O cadastro do computador no servidor (ID e último endereço IP) fica enquanto o computador usar o suporte da MT. [PREENCHER: prazo e forma de exclusão do cadastro depois que o cliente deixa de usar o suporte.]
- A sessão não é gravada, então não há conteúdo de sessão guardado.

## Com quem compartilhamos

- A MT não vende nem repassa os seus dados. Ninguém além da MT usa esses dados.
- O servidor fica numa empresa de hospedagem contratada pela MT ([PREENCHER: nome do provedor de hospedagem]), que mantém a máquina por conta da MT.
- Os registros só são entregues a uma autoridade mediante ordem judicial, nos termos do Marco Civil da Internet.
- Nenhum dado vai para a RustDesk.

## Onde ficam os dados

No servidor da MT, no Brasil, em São Paulo.

## Seus direitos

A LGPD (art. 18) garante a você, mediante pedido:

- saber se a MT trata dados seus;
- ter acesso a esses dados;
- corrigir dados incompletos, errados ou desatualizados;
- pedir a anonimização, o bloqueio ou a eliminação de dados desnecessários, excessivos ou tratados fora da lei;
- pedir a portabilidade dos dados, conforme a regulamentação da ANPD;
- saber com quem a MT compartilhou os seus dados;
- quando algum tratamento depender do seu consentimento: saber que pode não consentir e o que acontece se não consentir, revogar o consentimento e pedir a eliminação dos dados tratados com ele;
- opor-se a um tratamento feito sem consentimento, se ele descumprir a LGPD;
- reclamar à Autoridade Nacional de Proteção de Dados (ANPD).

**Como pedir:** escreva para [PREENCHER: e-mail para titulares de dados]. O atendimento é gratuito. Respondemos em até [PREENCHER: prazo de resposta].

Os registros de acesso podem continuar guardados até o fim dos 6 meses mesmo com pedido de eliminação, se a lei exigir a guarda.

## Segurança

- O programa só se liga ao servidor e à chave da MT, que vêm embutidos nele.
- A conexão depende do seu aceite, por padrão, e o programa vem sem senha permanente.
- [PREENCHER: medidas do servidor, só depois de aplicadas e conferidas na VPS. Previstas no VPS-MT: acesso administrativo só por chave, firewall, atualizações automáticas de segurança e registros com acesso restrito.]

## Mudanças neste aviso

Quando este aviso mudar, a versão nova é publicada nesta página, com número e data. Vale sempre a versão de data mais recente.

Versão [PREENCHER: número da versão], de [PREENCHER: data].

---

## Tabela de sustentação

| # | Afirmação do texto | Fonte | Classificação |
|---|---|---|---|
| 1 | Quem trata: MANFRED TECNOLOGIA LTDA, CNPJ 21.075.901/0001-12, MT - Manfred Tecnologia | `AGENTS-MT.md`, "Autoria e licença"; LGPD, art. 9º, III | FATO (dado da empresa); FATO LEGAL (dever de identificar o controlador) |
| 2 | A MT é quem decide sobre os registros do servidor | LGPD, art. 5º, VI; VPS-MT, verificação, item 2 | INTERPRETAÇÃO |
| 3 | Contato do titular e encarregado | LGPD, art. 9º, IV, e art. 41, § 1º; Resolução CD/ANPD nº 2/2022, Anexo I, art. 11 e § 1º (agente de pequeno porte pode não indicar encarregado, mas deve ter canal). Enquadramento da MT como agente de pequeno porte: [FONTE?] | FATO LEGAL; enquadramento pendente |
| 4 | Finalidade única: suporte remoto pedido | Verificação de privacidade, item 4.1; LGPD, art. 6º, III, e art. 9º, I | INTERPRETAÇÃO |
| 5 | O servidor registra ID, IP e horário do cadastro | VPS-MT, verificação, itens 1 e 4; VPS-MT, pendências, "Guarda de registros" (teste local de 05/10/2026) | FATO (técnico, teste local) |
| 6 | O repasse registra IPs, abertura e fechamento da sessão | VPS-MT, pendências, "Guarda de registros" (teste local de 05/10/2026). Conexão direta ainda não conferida | FATO (técnico, teste local) |
| 7 | Dados enviados para montar a conexão (identificador, chave pública, versão, tipo de rede, endereço local) | Verificação de privacidade, item 3.1 (`protos/rendezvous.proto` do `hbb_common`, commit `229b904`) | FATO (código); o que o servidor guarda é [FONTE?] |
| 8 | Na sessão, o técnico vê a tela, controla teclado e mouse, troca arquivos e mensagens | Verificação de privacidade, item 3.2 | INTERPRETAÇÃO (descrição do funcionamento) |
| 9 | Dados do aparelho recebidos pelo técnico na abertura | Verificação de privacidade, item 3.2 e item 6 (teste pendente) | [FONTE?] |
| 10 | Configuração, registros locais e senha ficam no computador | Verificação de privacidade, item 3.3 | INTERPRETAÇÃO |
| 11 | Orientação de fechar o que não tem a ver com o atendimento | Verificação de privacidade, item 4.5; LGPD, art. 11 (dado sensível pode aparecer na tela) | RECOMENDAÇÃO |
| 12 | A MT não grava a tela nem o conteúdo da sessão | VPS-MT, verificação, item 4 (servidor sem conteúdo de sessão); fatos do produto informados pelo Manfred (fatias 2 e 3). Lado do técnico depende de prática (pendência 9) | FATO (servidor); RECOMENDAÇÃO (compromisso operacional do técnico) |
| 13 | O programa não manda dados à RustDesk; só fala com `rustdesk.manfred.com.br` e com o técnico | Verificação de privacidade, item 3.4 (`check_software_update` e `is_custom_client` em `src/common.rs`; `register-device` = "N"); spec da versão 1, seção do servidor de API | FATO (código), sujeito ao teste de rede (pendência 4) |
| 14 | Aceite por clique como padrão, mudável pelo técnico | Spec da versão 1 (`approve-mode` = `click` em `DEFAULT_SETTINGS`); verificação de privacidade, item 4.5 | FATO (configuração) |
| 15 | A sessão pode ser encerrada a qualquer momento | Verificação de privacidade, item 5, linha "Controle de quem está na máquina" | INTERPRETAÇÃO (funcionamento do programa) |
| 16 | Sem senha permanente de fábrica; acesso sem presença só com senha configurada | Spec da versão 1 ("Nenhuma senha permanente de fábrica"; decisão 4); verificação de privacidade, item 4.5 | FATO (configuração) |
| 17 | Base legal para pessoa física: execução de contrato | LGPD, art. 7º, V; VPS-MT, verificação, item 3.1; verificação de privacidade, item 4.2 | INTERPRETAÇÃO |
| 18 | Base legal para empregado de cliente empresa e papel da MT | LGPD, arts. 5º, VI e VII, e 39; consulta, questão 4 | [DEPENDE DA CONSULTA, questão 4] |
| 19 | Sem caixa de consentimento | Marco Civil, art. 7º, IX; LGPD, art. 7º; consulta, questão 3; verificação de privacidade, item 4.4 | [DEPENDE DA CONSULTA, questão 3]; RECOMENDAÇÃO até a resposta |
| 20 | Registros de acesso guardados por 6 meses, com acesso restrito, e apagados depois | Marco Civil, art. 15, caput; VPS-MT, verificação, item 3.3 (guarda por cautela, risco aceito em 04/10/2026); `VPS-MT/servidor/registros/vps-mt.conf` (`MaxRetentionSec=6month`) | FATO LEGAL (prazo do art. 15); INTERPRETAÇÃO (incidência sobre a MT); FATO (configuração); pendência 8 |
| 21 | Guarda além de 6 meses só por pedido de autoridade ou ordem judicial | Marco Civil, art. 15, §§ 1º e 2º | FATO LEGAL |
| 22 | Cadastro do computador fica enquanto usar o suporte | VPS-MT, verificação, item 1 (o servidor guarda o último contato de cada máquina) e item 3.3; LGPD, arts. 15 e 16 (término e eliminação) | INTERPRETAÇÃO; prazo de exclusão [PREENCHER] |
| 23 | A MT não vende nem repassa; ninguém além da MT usa os dados | Verificação de privacidade, item 5, linha "Compartilhamento"; LGPD, art. 9º, V | RECOMENDAÇÃO (compromisso da MT, a confirmar pelo Manfred) |
| 24 | Provedor de hospedagem guarda a máquina por conta da MT | LGPD, arts. 5º, VII, e 39; `VPS-MT/docs/contratacao-hostgator.md` (HostGator Brasil LTDA, CNPJ 15.754.475/0001-40, sobre Oracle Cloud). A verificação do VPS-MT ainda analisa a Hostinger (pendência 6) | INTERPRETAÇÃO; nome do provedor [PREENCHER] |
| 25 | Registros entregues a autoridade só com ordem judicial | Marco Civil, art. 10, § 1º, e art. 15, § 3º | FATO LEGAL |
| 26 | Dados no Brasil, em São Paulo | `VPS-MT/docs/contratacao-hostgator.md`, seções 1 e 6 (VPS vpsbr-16184648 "em São Paulo"; "Servidores Oracle Cloud no Brasil") | FATO, válido enquanto a VPS da HostGator for mantida (pendência 6) |
| 27 | Lista de direitos | LGPD, art. 18, I a IX, e §§ 1º e 2º | FATO LEGAL |
| 28 | Atendimento gratuito | LGPD, art. 18, § 5º | FATO LEGAL |
| 29 | Registros podem ser mantidos até o fim dos 6 meses mesmo com pedido de eliminação, se a lei exigir | LGPD, art. 16, I; Marco Civil, art. 15 (incidência sobre a MT ficou como risco aceito no VPS-MT, item 3.3) | INTERPRETAÇÃO |
| 30 | Programa só liga ao servidor e à chave da MT embutidos | Spec da versão 1 (servidor e chave em `src/mt_config.rs`); `AGENTS-MT.md`, tabela de stack | FATO (configuração) |
| 31 | Medidas de segurança do servidor | LGPD, art. 46; VPS-MT, verificação, item 4; `VPS-MT/docs/instalacao.md`, passos D, E e F; `contratacao-hostgator.md`, seção 6 (estado em 04/10/2026) | [PREENCHER] até aplicadas (pendência 7) |
| 32 | Mudanças publicadas com versão e data | LGPD, art. 6º, VI (transparência), e art. 9º | RECOMENDAÇÃO |

Não há afirmação sobre criptografia da sessão: nenhuma das fontes lidas a sustenta. Se o Manfred quiser incluir, conferir no código ou na documentação oficial e citar a fonte.

## Pontos pendentes de parecer jurídico

São 2, os mesmos da verificação de privacidade (pendências 5 e 6 do projeto): questão 3 (Marco Civil, art. 7º, IX) e questão 4 (papel da MT no computador de cliente empresa), em `CONSULTA-ADVOGADO-mapdesk-agpl-marca-2026-10-05.md`. **Não publique os trechos marcados com `[DEPENDE DA CONSULTA]` antes do parecer.**
