# Verificação jurídica: textos do site do produto MapDesk-MT

Data: 01/11/2026. Projeto MAPDESK-MT. Feita com a skill `legal-br`.

Objeto: três trechos de `public/index.html`, a página de `mapdesk.manfred.com.br`:

1. o parágrafo "Licença e garantias" e a frase sobre nomes e logotipos, na seção "Código aberto";
2. a seção "Uso autorizado", com o aviso de uso do acesso remoto;
3. a cláusula "Conteúdo deste site", contra cópia e raspagem do conteúdo (regra 11, item 5, para site de conteúdo).

Não entram aqui o texto de privacidade, que repete o de `manfred.com.br/acesso` (lido em 01/11/2026) e tem verificação própria em `verificacao-privacidade-cliente-2026-10-05.md`, nem as pendências da consulta ao advogado de 05/10/2026, que continuam abertas no portão antes da tag (spec do site, seção 8).

## Contexto e premissas

- **Partes:** MANFRED TECNOLOGIA LTDA, CNPJ 21.075.901/0001-12 (MT - Manfred Tecnologia), que distribui o programa e mantém o site; quem visita a página e baixa o programa.
- **Produto:** programa de acesso remoto gratuito, obra derivada do RustDesk, sob a AGPL-3.0 (`LICENCE` da raiz e `AVISO-DE-MODIFICACAO.md`).
- **Relação de consumo:** premissa tratada como hipótese. O CDC, art. 3º, § 2º, define serviço como atividade fornecida "mediante remuneração". O download é gratuito, mas o programa é usado no suporte que a MT presta aos clientes, que pode ser remunerado. Como não dá para afastar a incidência do CDC em todos os casos, o texto não exclui responsabilidade e ressalva os direitos do consumidor. INTERPRETAÇÃO.
- **Dados pessoais:** o site não coleta dados nem carrega medição (spec, seção 5). O que o servidor registra está na página de privacidade. Fora do objeto.
- **Menores, pagamento, imagem e premiação:** não há.

## Fontes

| Norma | Onde foi lida | Conferência |
|---|---|---|
| Lei nº 9.610/1998, arts. 7º, 29 e 46 | `legal-br/fontes-md/leis/07-direitos-autorais-9610-1998.md` | Confirmado em https://www.planalto.gov.br/ccivil_03/leis/l9610.htm em 01/11/2026, sem nota de alteração nesses dispositivos |
| Lei nº 8.078/1990 (CDC), arts. 3º, § 2º, e 51, I | `legal-br/fontes-md/leis/02-cdc-lei-8078-1990-compilado.md`, marcada como desatualizada no `STATUS-FONTES.md` de 23/09/2026 | Confirmado em https://www.planalto.gov.br/ccivil_03/leis/l8078compilado.htm em 01/11/2026, sem nota de alteração nesses dispositivos |
| AGPL-3.0, seções 7, 15, 16 e 17 | `LICENCE` da raiz do repositório | Texto da própria licença do projeto |

O `STATUS-FONTES.md` da biblioteca local tem mais de 30 dias, por isso cada dispositivo citado foi conferido no Planalto na data acima.

## 1. Licença e garantias

Texto na página:

> O MapDesk - MT é distribuído de graça sob a AGPL-3.0. A conexão depende da internet dos dois computadores e do servidor da MT no ar, e a licença não inclui promessa de funcionamento em todo computador ou em toda rede. As disposições da AGPL-3.0 sobre garantias e responsabilidade (seções 15 a 17) se aplicam nos limites permitidos pela legislação brasileira e não restringem direitos assegurados ao consumidor por lei.
>
> Os nomes MapDesk-MT e MT - Manfred Tecnologia e os logotipos da MT não fazem parte da licença do código.

**FATO LEGAL.** CDC, art. 51, I: são nulas as cláusulas que "impossibilitem, exonerem ou atenuem a responsabilidade do fornecedor por vícios de qualquer natureza dos produtos e serviços ou impliquem renúncia ou disposição de direitos". Incidência: vale quando houver relação de consumo (premissa acima, tratada como hipótese).

**FATO (texto da licença).** A seção 15 da AGPL-3.0 afasta garantias "to the extent permitted by applicable law"; a seção 16 limita a responsabilidade "unless required by applicable law"; a seção 17 manda aplicar a lei local mais próxima quando as duas não puderem valer como escritas. A própria licença, portanto, cede à lei local.

**INTERPRETAÇÃO.** Reproduzir a exclusão de garantia da AGPL em termos absolutos poderia ser lido como cláusula do art. 51, I, numa relação de consumo. O texto adotado não exclui nada por conta própria: diz que a licença não promete funcionamento universal, aponta as seções 15 a 17 e ressalva a lei brasileira e os direitos do consumidor. É o mesmo desenho do parágrafo aprovado no MapDisk (`manfredjr/mapdisk`, `public/index.html`, lido em 01/11/2026).

**FATO (texto da licença).** A seção 7, alínea "e", da AGPL-3.0 permite recusar direitos sobre marcas e nomes comerciais. O `AVISO-DE-MODIFICACAO.md` já faz essa recusa ("Nomes e logotipos"), e a frase da página só a repete.

**Fica de fora, de propósito:** o aviso de copyright da MT sobre as mudanças, que só entra depois da confirmação do Manfred (`AGENTS-MT.md`, "Autoria e licença").

## 2. Uso autorizado

Texto na página:

> Com o MapDesk - MT aberto e a conexão aceita, outra pessoa vê a tela e usa o teclado e o mouse do computador. Use o programa só em computadores que você tem autorização para usar ou administrar, e aceite a conexão só de quem você conhece, como o técnico do seu suporte.
>
> Se alguém pedir o seu ID por telefone ou mensagem sem que você tenha chamado o suporte, não informe e não aceite a conexão.

**RECOMENDAÇÃO.** O trecho é orientação de uso e de prevenção a golpe, sem afirmação jurídica. Não cita tipo penal nem obrigação legal, porque nenhuma foi conferida para esta verificação e o aviso não depende disso. A descrição do funcionamento (tela, teclado e mouse depois do aceite) vem da verificação de privacidade de 05/10/2026, item 3.2, e da spec da versão 1 (`approve-mode` = `click`).

## 3. Conteúdo deste site

Texto na página:

> Os textos, as imagens e os logotipos deste site são protegidos pela Lei nº 9.610/1998, a lei de direitos autorais. Copiar, reproduzir ou guardar esse conteúdo em base de dados, inclusive por robôs de raspagem ou para treinar sistemas de inteligência artificial, depende de autorização prévia e expressa do titular, salvo nos casos em que a própria lei dispensa a autorização. Pedidos de autorização: manfred@manfred.com.br.
>
> Isso não vale para o código do programa. Ele continua sob a AGPL-3.0, e qualquer pessoa pode copiar, modificar e redistribuir o código nos termos dessa licença.

**FATO LEGAL.** Lei nº 9.610/1998, art. 7º, caput: "São obras intelectuais protegidas as criações do espírito, expressas por qualquer meio ou fixadas em qualquer suporte, tangível ou intangível, conhecido ou que se invente no futuro, tais como: I - os textos de obras literárias, artísticas ou científicas; [...] VIII - as obras de desenho, pintura, gravura, escultura, litografia e arte cinética". Incidência: os textos da página e os logotipos desenhados são criações expressas em suporte intangível.

**FATO LEGAL.** Lei nº 9.610/1998, art. 29, caput: "Depende de autorização prévia e expressa do autor a utilização da obra, por quaisquer modalidades, tais como: I - a reprodução parcial ou integral; [...] IX - a inclusão em base de dados, o armazenamento em computador, a microfilmagem e as demais formas de arquivamento do gênero; X - quaisquer outras modalidades de utilização existentes ou que venham a ser inventadas."

**FATO LEGAL.** Lei nº 9.610/1998, art. 46: lista os usos que "não constitui[em] ofensa aos direitos autorais", como a citação para estudo, crítica ou polêmica com o nome do autor e a origem (inciso III) e a reprodução de pequenos trechos (inciso VIII). Os incisos I a VIII foram lidos, e nenhum trata de raspagem automatizada ou de treino de sistemas. Por isso o texto ressalva "os casos em que a própria lei dispensa a autorização", sem listar.

**INTERPRETAÇÃO.** Raspar o site copia e armazena o conteúdo, o que cabe na reprodução (art. 29, I) e no armazenamento em computador ou na inclusão em base de dados (art. 29, IX). O treino de sistemas de inteligência artificial com o conteúdo pressupõe essa cópia. A cláusula não cria proibição nova: lembra a regra da lei e diz onde pedir autorização.

**INTERPRETAÇÃO.** O texto fala em "titular", e não em "MT". Os direitos sobre o conteúdo passam do Manfred para a MT pela cessão escrita, que ainda está no portão antes da tag (spec do site, seção 8; nota de 02/11/2026: o Manfred moveu a cessão para antes da primeira venda). Até lá, "titular" é exato para os dois cenários.

**INTERPRETAÇÃO.** A página não tem aceite, então a cláusula funciona como aviso da reserva de direitos, e não como contrato com o visitante. A proteção vem da lei, não da adesão. O bloqueio técnico de robôs de IA fica no Cloudflare (spec, seção 8, passo 5).

**FATO (texto da licença).** A ressalva do código evita conflito com a AGPL-3.0, que garante copiar, modificar e redistribuir o programa (seções 4 a 6). A cláusula vale para o conteúdo do site, não para o código.

**RISCO.** A cláusula não impede, por si só, a raspagem por robôs de fora do país. Ela serve como prova da reserva de direitos se for preciso agir depois, junto com o bloqueio no Cloudflare.

## Pendências de validação

Nenhuma. Os três trechos se apoiam em dispositivos conferidos no Planalto em 01/11/2026, no texto da AGPL-3.0 e em fatos do projeto. Seguem abertas, fora deste objeto, as questões da consulta de 05/10/2026, que o portão antes da tag confere.

## Requisitos para implementação

- [x] Parágrafo "Licença e garantias" na seção "Código aberto", com a ressalva da lei brasileira e do consumidor.
- [x] Frase de que nomes e logotipos da MT não fazem parte da licença.
- [x] Seção "Uso autorizado" com o aviso de autorização e o alerta de golpe.
- [x] Cláusula "Conteúdo deste site" com a ressalva do código sob a AGPL-3.0.
- [ ] Bloqueio de robôs de IA no Cloudflare, no subdomínio (Manfred, na publicação).
- [ ] Rever este texto quando a cessão do autor para a MT for assinada, se o Manfred quiser nomear a MT como titular.
