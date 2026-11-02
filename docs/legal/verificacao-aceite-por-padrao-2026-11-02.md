# Verificação jurídica: aceite e contatos de rede nas páginas do MapDesk - MT

Data: 02/11/2026. Projeto MAPDESK-MT. Feita com a skill `legal-br`.

Objeto: as frases sobre o aceite e sobre o que o programa contata em `public/index.html` e `public/privacidade.html`, e esta resposta, que a sessão do site da MT usa na página do MapDesk (PR 68 de `manfred-tecnologia-site`):

> Como ele vem, não: a aprovação é por clique, e o técnico só vê o computador depois que alguém clica em Aceitar. O atendimento sem ninguém na frente da máquina existe, mas exige mudar essa configuração naquele computador. A partir daí, quem tem uma senha válida, a definida ali ou a temporária do programa, entra sem o Aceitar.

## Contexto e premissas

- **Partes:** MANFRED TECNOLOGIA LTDA, que distribui o programa e presta o suporte; quem baixa o programa ou recebe o atendimento.
- **Relação de consumo:** premissa tratada como hipótese, como na verificação de 01/11/2026. O CDC, art. 2º, define consumidor como quem "adquire ou utiliza produto ou serviço como destinatário final", e o art. 3º, § 2º, define serviço como atividade fornecida "mediante remuneração". O download é gratuito, mas o programa é usado no suporte da MT, que pode ser remunerado. Se o cliente for empresa que não seja destinatária final, o CDC pode não incidir.
- **Dados pessoais:** há tratamento, porque o técnico vê a tela e usa o teclado e o mouse (verificação de privacidade de 05/10/2026, item 3.2).

## Fontes

| Norma | Onde foi verificada | Data |
|---|---|---|
| Lei nº 8.078/1990 (CDC), arts. 2º, 3º, § 2º, 30 e 37, § 1º | A cópia local está marcada como MUDOU no `STATUS-FONTES.md` de 02/11/2026. Texto confirmado em https://www.planalto.gov.br/ccivil_03/leis/l8078compilado.htm | 02/11/2026 |
| Lei nº 13.709/2018 (LGPD), arts. 5º, I, e 6º, VI | `legal-br/fontes-md/leis/03-lgpd-lei-13709-2018-compilado.md`, EM DIA no `STATUS-FONTES.md` de 02/11/2026 | 02/11/2026 |

## Como o programa funciona

Conferido por leitura do código, sem executar o programa nem capturar o tráfego:

- `src/mt_config.rs` grava `approve-mode` = `click` em `DEFAULT_SETTINGS`. É um padrão, não uma trava.
- `src/server/connection.rs`, linhas 2994 a 3012: no modo `click`, um pedido com senha não é autenticado e fica à espera do aceite. A exceção é a opção `allow-logon-screen-password`, que o `mt_config.rs` não liga.
- Fora do modo `click`, a senha válida autoriza a entrada sem o clique (mesmo arquivo, linhas 3031 a 3041, e `password_security.rs` do submódulo `hbb_common`).
- O gatilho é mudar o modo, e não definir uma senha. A senha temporária vale nesses modos porque o método padrão é `UseBothPasswords` (`connection.rs`, linhas 2555 a 2566). Ela depende de alguém lê-la na tela.
- O técnico controla o teclado e o mouse num atendimento aceito, então pode chegar à tela dessa configuração. A mudança por sessão remota não foi testada.
- A conexão pode ir direto entre os dois computadores, sem passar pelo repasse do servidor.
- Ao iniciar, o programa consulta servidores STUN públicos: `start_all` chama `test_nat_type`, que chega a `test_ipv6` (`src/common.rs`, linhas 662 e 2654). Os servidores são `stun.cloudflare.com`, `stun.l.google.com`, `stun.antisip.com` e `stun.nextcloud.com` (`webrtc.rs` do `hbb_common`, commit 229b904). Nada em `mt_config.rs` desliga isso. Numa máquina sem IPv6, só deve haver a resolução dos nomes.

Por isso, as páginas deixam de dizer que o programa "só se liga" ao servidor da MT. Não houve inventário completo das saídas de rede, e nenhuma frase pública pode voltar a dizer "só" sem esse inventário e uma captura de tráfego.

## Análise

**FATO LEGAL.** CDC, art. 30: "Toda informação ou publicidade, suficientemente precisa, veiculada por qualquer forma ou meio de comunicação com relação a produtos e serviços oferecidos ou apresentados, obriga o fornecedor que a fizer veicular ou dela se utilizar e integra o contrato que vier a ser celebrado."

**FATO LEGAL.** CDC, art. 37, § 1º: "É enganosa qualquer modalidade de informação ou comunicação de caráter publicitário, inteira ou parcialmente falsa, ou, por qualquer outro modo, mesmo por omissão, capaz de induzir em erro o consumidor a respeito da natureza, características, qualidade, quantidade, propriedades, origem, preço e quaisquer outros dados sobre produtos e serviços."

**FATO LEGAL.** LGPD, art. 6º, VI: transparência é a "garantia, aos titulares, de informações claras, precisas e facilmente acessíveis sobre a realização do tratamento e os respectivos agentes de tratamento". O art. 5º, I, define dado pessoal como "informação relacionada a pessoa natural identificada ou identificável".

**INTERPRETAÇÃO.** A página apresenta o programa e o suporte da MT, e por isso é tratada aqui como comunicação de caráter publicitário. Se a relação for de consumo, uma frase sem ressalva sobre o aceite ou sobre o que o programa contata é precisa e nem sempre verdadeira. Ela poderia obrigar a MT pelo art. 30 e ser questionada pelo art. 37, § 1º. As frases novas descrevem o que o código faz.

**INTERPRETAÇÃO.** Quem está na frente da máquina precisa saber que, depois de mudada a configuração, o acesso com senha não pede aceite, e que o técnico também pode fazer essa mudança. Por isso, a página de privacidade recebeu o aviso, em linha com o art. 6º, VI, da LGPD. O IP visto pelos servidores STUN pode ser dado pessoal, conforme o caso, e por isso também é informado.

**RISCO.** Em computador de empresa, o titular pode ser um empregado que não participou da decisão de mudar a configuração, e o aviso na página pode não alcançá-lo.

**REVISÃO PROFISSIONAL.** Este documento não fecha o tema do acesso sem aceite. Seguem abertas as questões 3 (Marco Civil, art. 7º, IX, depois da LGPD) e 4 (papel da MT e base legal para empregados) da consulta de 05/10/2026, e a recomendação daquela verificação de que o cliente empresa decida por escrito o acesso sem presença. A consulta também precisa da pergunta nova: as consultas STUN a empresas de fora, feitas com o IP do cliente, exigem base legal própria ou tratamento de transferência internacional?

## Resultado

Com a ressalva acima, o texto das páginas e a resposta do site da MT descrevem o funcionamento lido no código. A resposta do site só trata do aceite. Se aquela página afirmar que o programa usa "só" o servidor da MT, a afirmação precisa sair.

Limites: nada foi testado em execução, e o texto muda se o Manfred decidir bloquear o STUN no código.

Autor: Manfred Heil Junior
