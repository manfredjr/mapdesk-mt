# Verificação jurídica: promessa de aceite nas páginas do MapDesk - MT

Data: 02/11/2026. Projeto MAPDESK-MT. Feita com a skill `legal-br`.

Objeto: as frases sobre o aceite em `public/index.html` e `public/privacidade.html`, e esta resposta, que a sessão do site da MT usa na página do MapDesk (PR 68 de `manfred-tecnologia-site`):

> Como ele vem, não: a aprovação é por clique, e o técnico só vê o computador depois que alguém clica em Aceitar. O atendimento sem ninguém na frente da máquina existe, mas exige mudar essa configuração naquele computador. A partir daí, quem tem uma senha válida, a definida ali ou a temporária do programa, entra sem o Aceitar.

## Contexto e premissas

- **Partes:** MANFRED TECNOLOGIA LTDA, que distribui o programa e presta o suporte; quem baixa o programa ou recebe o atendimento.
- **Relação de consumo:** premissa tratada como hipótese, como na verificação de 01/11/2026. O CDC, art. 3º, § 2º, define serviço como atividade fornecida "mediante remuneração". O download é gratuito, mas o programa é usado no suporte da MT, que pode ser remunerado. Se o cliente for empresa fora do conceito de destinatário final, o CDC pode não incidir.
- **Dados pessoais:** há tratamento, porque o técnico vê a tela e usa o teclado e o mouse (verificação de privacidade de 05/10/2026, item 3.2).

## Fontes

| Norma | Onde foi verificada | Data |
|---|---|---|
| Lei nº 8.078/1990 (CDC), arts. 3º, § 2º, 30, 31 e 37, § 1º | A cópia local está marcada como MUDOU no `STATUS-FONTES.md` de 02/11/2026. Texto confirmado em https://www.planalto.gov.br/ccivil_03/leis/l8078compilado.htm | 02/11/2026 |
| Lei nº 13.709/2018 (LGPD), art. 6º, VI | `legal-br/fontes-md/leis/03-lgpd-lei-13709-2018-compilado.md`, EM DIA no `STATUS-FONTES.md` de 02/11/2026 | 02/11/2026 |

## Como o programa funciona

Conferido por leitura do código, sem teste em execução com senha configurada:

- `src/mt_config.rs` grava `approve-mode` = `click` em `DEFAULT_SETTINGS`. É um padrão, não uma trava.
- `src/server/connection.rs`, linhas 2994 a 3012: no modo `click`, um pedido com senha não é autenticado e fica à espera do aceite. A exceção é a opção `allow-logon-screen-password`, que o MapDesk - MT não liga.
- Nos outros modos, a senha válida autoriza a entrada sem o clique (mesmo arquivo, linhas 3031 a 3041, e `password_security.rs` do submódulo `hbb_common`).
- A senha temporária vale nesses modos, sem ninguém definir senha, porque o método padrão é `UseBothPasswords` (`connection.rs`, linhas 2555 a 2566). Uma versão anterior deste texto dizia que era preciso definir uma senha, e a correção veio da revisão do site da MT.
- O programa também pode ligar direto ao computador do técnico, sem repasse. Por isso, as páginas dizem que ele usa só o servidor da MT, e não que a conexão passa só por ele.

## Análise

**FATO LEGAL.** CDC, art. 30: "Toda informação ou publicidade, suficientemente precisa, veiculada por qualquer forma ou meio de comunicação com relação a produtos e serviços oferecidos ou apresentados, obriga o fornecedor que a fizer veicular ou dela se utilizar e integra o contrato que vier a ser celebrado."

**FATO LEGAL.** CDC, art. 37, § 1º: é enganosa a informação publicitária "inteira ou parcialmente falsa, ou, por qualquer outro modo, mesmo por omissão, capaz de induzir em erro o consumidor" sobre características do produto ou serviço.

**FATO LEGAL.** LGPD, art. 6º, VI: transparência é a "garantia, aos titulares, de informações claras, precisas e facilmente acessíveis sobre a realização do tratamento".

**INTERPRETAÇÃO.** Se a relação for de consumo, "a conexão só começa quando você aceita", sem ressalva, é uma frase precisa que o programa nem sempre cumpre, porque a configuração pode mudar. Ela poderia obrigar a MT pelo art. 30 e ser questionada pelo art. 37, § 1º. Com "por padrão" e a explicação do atendimento com senha, a frase passa a descrever o que o programa faz.

**INTERPRETAÇÃO.** Quem está na frente da máquina precisa saber que, com senha configurada, o acesso não pede aceite. Por isso, a página de privacidade também recebeu a frase, em linha com o art. 6º, VI, da LGPD. A verificação de 05/10/2026 trata o aceite como padrão, e este texto fica coerente com ela.

**RISCO.** Em computador de empresa, o titular pode ser um empregado que não participou da decisão de configurar a senha. O aviso na página pode não alcançá-lo. A questão não muda o texto das páginas e fica para a orientação de uso quando o atendimento com senha for oferecido.

## Resultado

A resposta usada no site da MT descreve o funcionamento lido no código e não precisa de ajuste jurídico. As frases de `public/index.html` e `public/privacidade.html` foram alinhadas a ela. Nada aqui depende de parecer externo. Limite: o funcionamento foi conferido por leitura do código, e a verificação não testou o programa com senha configurada.

Autor: Manfred Heil Junior
