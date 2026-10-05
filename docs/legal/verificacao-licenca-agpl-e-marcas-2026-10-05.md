# Verificação jurídica: licença AGPL-3.0 e marcas do MapDesk

Data: 05/10/2026. Projeto MAPDESK-MT. Feita com a skill `legal-br`.

Cobre: (1) obrigações da AGPL-3.0 na distribuição do executável modificado; (2) uso da marca RustDesk e forma de citar a origem; (3) busca de anterioridade do nome MapDesk.

Privacidade do cliente fica em `verificacao-privacidade-cliente-2026-10-05.md`. Pontos que dependem de parecer ficam em `CONSULTA-ADVOGADO-mapdesk-agpl-marca-2026-10-05.md`.

## 1. Contexto e premissas

### 1.1. Fatos

| Fato | Fonte |
|---|---|
| O MapDesk é fork do RustDesk 1.5.0 (`rustdesk/rustdesk`, tag `1.5.0`) e do submódulo `rustdesk/hbb_common` (commit `229b904508364c8997aad0fb5af57effac859f60`) | `AGENTS-MT.md`; `.superpowers/rascunho/achados-codigo-1.5.0.md` |
| Distribuidora: MANFRED TECNOLOGIA LTDA, CNPJ 21.075.901/0001-12 (MT - Manfred Tecnologia), gratuitamente, aos clientes do suporte remoto | `AGENTS-MT.md`, seção "Autoria e licença"; pedido do Manfred |
| Forma de distribuição: executável Windows em versões (releases) de um repositório público no GitHub, oferecido também na página de download do site da MT | `AGENTS-MT.md`, seção "O que é" |
| Mudanças da MT: servidor de ID e repasse `rustdesk.manfred.com.br` e chave pública embutidos, nome "MapDesk", ícones e cores da MT, aprovação por clique como padrão, servidor de API desligado | pedido do Manfred; `achados-codigo-1.5.0.md` |
| O servidor (RustDesk Server OSS) roda a imagem oficial sem modificação, no projeto VPS-MT | `C:\COWORK\CODE\VPS-MT\docs\legal\verificacao-servidor-rustdesk-2026-10-04.md`, item 3.4 |
| Decisão do Manfred em 05/10/2026: a marca não será registrada; busca exata "mapdesk" no INPI sem resultado (base até 29/09/2026) | `C:\COWORK\CODE\VPS-MT\.superpowers\rascunho\briefing-projeto-mapdesk.md`, seção 1 |

Nome definido: "MapDesk-MT", repositório `manfredjr/mapdesk-mt`, executável `MapDesk-MT.exe` (briefing do projeto, atualizado em 05/10/2026). Uma versão anterior do `AGENTS-MT.md` usava "MapDesk"; já foi corrigida. Em 05/10/2026 o repositório ainda não existia (API do GitHub devolveu 404).

### 1.2. Premissas de incidência

| Premissa | O que aciona | Fundamento |
|---|---|---|
| O MapDesk é "versão modificada" do RustDesk | AGPL-3.0, seções 5 e 6 | Seção 0: "To "modify" a work means to copy from or adapt all or part of the work in a fashion requiring copyright permission, other than the making of an exact copy." Trocar constantes, nome, ícones e padrões no código-fonte é adaptação, não cópia exata |
| A MT "transmite" (convey) o programa | Seções 4 a 6 | Seção 0: "To "convey" a work means any kind of propagation that enables other parties to make or receive copies." O cliente baixa e recebe uma cópia do executável |
| A distribuição é em código objeto (executável) | Seção 6 | Seção 1: ""Object code" means any non-source form of a work." |
| Há uso de sinal distintivo em produto oferecido no Brasil | Lei nº 9.279/1996 (LPI), marcas e concorrência desleal | O programa é oferecido pela MT a clientes no Brasil com um nome e uma identidade visual |
| Não há relação de consumo relevante para esta verificação | O CDC não entra aqui | O programa é gratuito e acessório ao contrato de suporte; o enquadramento do suporte é tema do contrato, não desta verificação |

### 1.3. Fontes consultadas em 05/10/2026

| Fonte | Onde | Observação |
|---|---|---|
| GNU AGPL-3.0, texto oficial | https://www.gnu.org/licenses/agpl-3.0.txt; cópia em `.superpowers/rascunho/agpl-3.0.txt`, SHA-256 `0d96a4ff68ad6d4b6f1f30f713b18d5184912ba8dd389f86aa7710db079abcb0` | Seções 0, 1, 4, 5, 6, 7, 13, 15 e 16 lidas na íntegra |
| Arquivo `LICENCE` do RustDesk 1.5.0 | https://github.com/rustdesk/rustdesk/blob/1.5.0/LICENCE; cópia em `.superpowers/rascunho/rustdesk-1.5.0/LICENCE` | Comparado com o texto oficial: igual, salvo a quebra de linha de duas linhas do apêndice "How to Apply". Sem termos adicionais da seção 7 |
| README do RustDesk 1.5.0 | https://github.com/rustdesk/rustdesk/blob/1.5.0/README.md | Tem só o "Misuse Disclaimer"; nenhuma regra de marca |
| Lista de arquivos da raiz e de `docs/` do RustDesk 1.5.0 | API do GitHub, `repos/rustdesk/rustdesk/contents?ref=1.5.0` | Não há `TRADEMARK`, `TRADEMARKS` nem arquivo de política de marca |
| Tela "Sobre" do RustDesk 1.5.0 | `flutter/lib/desktop/pages/desktop_setting_page.dart`, classe `_About` (linhas 2502 a 2600 na tag `1.5.0`) | Ver item 2.4 |
| `get_license` do RustDesk 1.5.0 | `src/ui_interface.rs`, linha 140, tag `1.5.0` | Ver item 2.4 |
| Repositório `rustdesk/hbb_common` | API do GitHub, `repos/rustdesk/hbb_common` e `Cargo.toml` no commit `229b904...` | Campo `license` nulo; nenhum arquivo de licença na raiz; `Cargo.toml` sem campo `license` |
| Termos do RustDesk, "Effective date: 16 September 2026" | https://rustdesk.com/terms; cópia em `.superpowers/rascunho/rustdesk-1.5.0/terms.html`, SHA-256 `beeb471c1443e4beca144d12ae8d1a71dc4ba4dbba96a842d677c7d28b68cce8` | Ver item 3.1 |
| Discussão `rustdesk/rustdesk` nº 13963, "custom logo and custom name" | https://github.com/rustdesk/rustdesk/discussions/13963 | Respostas do mantenedor em 05/01/2026 só apontam documentação; nada sobre marca |
| Lei nº 9.279/1996 (LPI), arts. 124, XIX, 126, 129, 132, IV, e 195 | https://www.planalto.gov.br/ccivil_03/leis/l9279.htm; cópia em `.superpowers/rascunho/lpi-9279.html`, SHA-256 `6eb9d3a6c90c3de71dd11e5c32c962ff8eb77ddfcb51984a1185727a62bd27c5` | A LPI não está na biblioteca local da `legal-br` |
| Lei nº 9.609/1998 (Lei de Software), art. 2º, § 1º | https://www.planalto.gov.br/ccivil_03/leis/l9609.htm; cópia em `.superpowers/rascunho/lei9609.html`, SHA-256 `cf34d99a5a6728e91fda003e409d18843ade004a21da4f11a0c687e5909e9723` | Conferida online porque a biblioteca local não tem `STATUS-FONTES.md` |
| INPI, "Classificação de produtos e serviços" | https://www.gov.br/inpi/pt-br/servicos/marcas/classificacao-marcas | Página atualizada em 13/01/2026 |
| INPI, "Caputs e notas explicativas NCL 13 2026" | https://www.gov.br/inpi/pt-br/servicos/marcas/classificacao-marcas/Caputs_enotas_NCL_13_2026.pdf; cópia em `.superpowers/rascunho/caputs-ncl13.pdf`, SHA-256 `a41ab2e7bcfc6e37ce08932e445d6f6d63e19b7d507692b330303df05bf47161` | Classes 9 e 42 |
| Buscas na internet e lojas por MapDesk, Map Desk e MapDesc | ver item 4.2 | Buscador e páginas abertas em 05/10/2026 |

A biblioteca local da `legal-br` (coleta de 21/08/2026) não tem `STATUS-FONTES.md`. Por isso toda norma brasileira citada aqui foi conferida no Planalto em 05/10/2026, como indicado acima.

Verificação anterior reaproveitada: `C:\COWORK\CODE\VPS-MT\docs\legal\verificacao-servidor-rustdesk-2026-10-04.md` (04/10/2026), item 3.4, que tratou a AGPL-3.0 do instalador oficial sem modificação. Aquela conclusão (seção 13 não incide porque não há modificação) não vale para o MapDesk, que é modificado. Esta verificação a substitui para o cliente.

## 2. AGPL-3.0

### 2.1. Seção 4: cópias literais do código-fonte

**FATO LEGAL (licença).** Seção 4: "You may convey verbatim copies of the Program's source code as you receive it, in any medium, provided that you conspicuously and appropriately publish on each copy an appropriate copyright notice; keep intact all notices stating that this License and any non-permissive terms added in accord with section 7 apply to the code; keep intact all notices of the absence of any warranty; and give all recipients a copy of this License along with the Program."

E: "You may charge any price or no price for each copy that you convey, and you may offer support or warranty protection for a fee."

Incidência: a seção 5 manda observar a seção 4 ("under the terms of section 4"), e a seção 6 manda observar as seções 4 e 5 ("under the terms of sections 4 and 5"). Logo, as condições da seção 4 alcançam o MapDesk em código-fonte e em executável.

**INTERPRETAÇÃO.** A distribuição gratuita não muda nada nas obrigações. E a MT pode cobrar pelo suporte, como já faz, sem conflito com a licença.

### 2.2. Seção 5: versão modificada

**FATO LEGAL (licença).** Seção 5, caput: "You may convey a work based on the Program, or the modifications to produce it from the Program, in the form of source code under the terms of section 4, provided that you also meet all of these conditions:"

- "a) The work must carry prominent notices stating that you modified it, and giving a relevant date."
- "b) The work must carry prominent notices stating that it is released under this License and any conditions added under section 7. This requirement modifies the requirement in section 4 to "keep intact all notices"."
- "c) You must license the entire work, as a whole, under this License to anyone who comes into possession of a copy. This License will therefore apply, along with any applicable section 7 additional terms, to the whole of the work, and all its parts, regardless of how they are packaged. This License gives no permission to license the work in any other way, but it does not invalidate such permission if you have separately received it."
- "d) If the work has interactive user interfaces, each must display Appropriate Legal Notices; however, if the Program has interactive interfaces that do not display Appropriate Legal Notices, your work need not make them do so."

Definição usada em 5(d), seção 0: "An interactive user interface displays "Appropriate Legal Notices" to the extent that it includes a convenient and prominently visible feature that (1) displays an appropriate copyright notice, and (2) tells the user that there is no warranty for the work (except to the extent that warranties are provided), that licensees may convey the work under this License, and how to view a copy of this License. If the interface presents a list of user commands or options, such as a menu, a prominent item in the list meets this criterion."

**INTERPRETAÇÃO (5a).** O aviso de modificação com data tem de estar "na obra". Para a obra em código-fonte, isso se cumpre com um arquivo na raiz do repositório que diga que o programa é versão modificada do RustDesk, liste as mudanças da MT e dê a data de cada versão. Para a obra em executável, o mesmo aviso na tela "Sobre" e na página da versão (release) torna o aviso "prominent".

**INTERPRETAÇÃO (5c).** Tudo o que entra no MapDesk fica sob a AGPL-3.0 para quem recebe uma cópia, inclusive os ícones, as cores e os textos da MT que estiverem no repositório e forem necessários para gerar o executável. A MT não pode reservar direitos autorais sobre esses arquivos dentro do MapDesk. A proteção do nome e do logotipo da MT, nesse cenário, depende de direito de marca e de concorrência desleal, e não da licença (ver 2.5 e 4.4).

**INTERPRETAÇÃO (5d).** A tela "Sobre" do RustDesk 1.5.0 mostra versão, data de compilação, impressão digital, ID, links "Privacy Statement" e "Website" e o texto "Copyright © [ano] Purslane Tech Pte. Ltd." seguido da variável `$license`. A variável vem de `get_license()`, que devolve chave, host e API da configuração do servidor tirada do nome do executável, e não o texto da licença. A tela original, portanto, mostra o copyright, mas não diz que não há garantia, nem que a obra pode ser redistribuída sob a AGPL-3.0, nem onde ler a licença. Pela parte final de 5(d), o MapDesk não está obrigado a completar esses avisos. Recomenda-se completar mesmo assim (ver 2.7): o custo é baixo, o `AGENTS-MT.md` já pede, e a mesma tela serve para oferecer o código-fonte (seção 13, item 2.6).

**INTERPRETAÇÃO (5b e seção 4).** O aviso "Copyright © ... Purslane Tech Pte. Ltd." da tela "Sobre" e os avisos de copyright e licença do código do RustDesk ficam como estão. O aviso da MT entra ao lado, limitado às mudanças da MT.

**FATO LEGAL.** Lei nº 9.609/1998, art. 2º, § 1º: "Não se aplicam ao programa de computador as disposições relativas aos direitos morais, ressalvado, a qualquer tempo, o direito do autor de reivindicar a paternidade do programa de computador e o direito do autor de opor-se a alterações não-autorizadas, quando estas impliquem deformação, mutilação ou outra modificação do programa de computador, que prejudiquem a sua honra ou a sua reputação." Incidência: o RustDesk é programa de computador e o MapDesk é distribuído no Brasil.

**INTERPRETAÇÃO.** As alterações estão autorizadas pela própria licença, e manter o crédito ao RustDesk e o copyright da Purslane Tech respeita o direito de paternidade. Remover esses créditos seria o ponto fraco, por isso o requisito de mantê-los.

### 2.3. Seção 6: oferta do código-fonte correspondente

**FATO LEGAL (licença).** Seção 6, caput: "You may convey a covered work in object code form under the terms of sections 4 and 5, provided that you also convey the machine-readable Corresponding Source under the terms of this License, in one of these ways:"

Alternativas (a) e (b) tratam de produto físico; (c) só vale "occasionally and noncommercially" e para quem recebeu o executável com oferta escrita; (e) trata de transmissão ponto a ponto. Nenhuma corresponde ao download em servidor. A que se aplica é a (d):

"d) Convey the object code by offering access from a designated place (gratis or for a charge), and offer equivalent access to the Corresponding Source in the same way through the same place at no further charge. You need not require recipients to copy the Corresponding Source along with the object code. If the place to copy the object code is a network server, the Corresponding Source may be on a different server (operated by you or a third party) that supports equivalent copying facilities, provided you maintain clear directions next to the object code saying where to find the Corresponding Source. Regardless of what server hosts the Corresponding Source, you remain obligated to ensure that it is available for as long as needed to satisfy these requirements."

Definição, seção 1: "The "Corresponding Source" for a work in object code form means all the source code needed to generate, install, and (for an executable work) run the object code and to modify the work, including scripts to control those activities."

Formato, seção 6: "Corresponding Source conveyed, and Installation Information provided, in accord with this section must be in a format that is publicly documented (and with an implementation available to the public in source code form), and must require no special password or key for unpacking, reading or copying."

**INTERPRETAÇÃO.** Para cada versão distribuída:

1. O código-fonte correspondente é o conteúdo da tag do MapDesk que gerou o executável, incluindo o submódulo `hbb_common` no commit usado, os ícones e os arquivos de compilação. Os "scripts to control those activities" incluem o fluxo do GitHub Actions da MT.
2. O executável fica na versão (release) do GitHub, e o código da mesma tag fica no mesmo repositório. É o "same place" de 6(d). O GitHub também gera os pacotes `.zip` e `.tar.gz` da tag, em formato público e sem senha.
3. Se a página do site da MT hospedar o executável no próprio servidor, ela passa a ser um "designated place". Então precisa de "clear directions next to the object code": link para o código da mesma versão ao lado do botão de download. Se a página só apontar para a versão do GitHub, o lugar de distribuição é o GitHub. Nos dois casos, pôr o link ao lado do botão resolve.
4. "For as long as needed": não apagar versões antigas nem tags de versões que algum cliente recebeu. Se o submódulo apontar para o repositório da RustDesk, o código dele depende de terceiro. Manter o submódulo apontando para um fork da MT garante a disponibilidade.

**INTERPRETAÇÃO (certificado de assinatura).** O certificado de assinatura de código não entra no código-fonte correspondente. A definição pede o que é preciso para "generate, install, and (for an executable work) run the object code and to modify the work", e o executável roda sem a assinatura da MT. As "Installation Information" só são exigidas quando a transmissão ocorre "in, or with, or specifically for use in, a User Product" e "as part of a transaction in which the right of possession and use of the User Product is transferred to the recipient". A MT não transfere a posse de nenhum computador. Os segredos do GitHub Actions ficam fora do repositório, como já manda o `AGENTS-MT.md`.

### 2.4. Leitura do código da tela "Sobre" do RustDesk 1.5.0

**FATO (código).** Em `desktop_setting_page.dart`, tag `1.5.0`, a classe `_About` monta o título `translate('About RustDesk')`, abre `https://rustdesk.com/privacy.html` no link "Privacy Statement" e `https://rustdesk.com` no link "Website", e mostra `'Copyright © ${DateTime.now().toString().substring(0, 4)} Purslane Tech Pte. Ltd.\n$license'`.

**INTERPRETAÇÃO.** No MapDesk:

- o título deixa de ser "Sobre o RustDesk" e passa a ser "Sobre o MapDesk";
- o link "Privacy Statement" não pode continuar apontando para a política da RustDesk, porque quem trata os dados do servidor do MapDesk é a MT (ver a verificação de privacidade);
- o link "Website" passa a apontar para o site da MT, e a origem RustDesk aparece em linha própria, com link para o projeto original;
- o copyright da Purslane Tech fica.

### 2.5. Seção 7: termos adicionais e marca

**FATO LEGAL (licença).** Seção 7, terceiro parágrafo: "Notwithstanding any other provision of this License, for material you add to a covered work, you may (if authorized by the copyright holders of that material) supplement the terms of this License with terms:" Entre elas:

- "b) Requiring preservation of specified reasonable legal notices or author attributions in that material or in the Appropriate Legal Notices displayed by works containing it; or"
- "c) Prohibiting misrepresentation of the origin of that material, or requiring that modified versions of such material be marked in reasonable ways as different from the original version; or"
- "e) Declining to grant rights under trademark law for use of some trade names, trademarks, or service marks; or"

Forma: "If you add terms to a covered work in accord with this section, you must place, in the relevant source files, a statement of the additional terms that apply to those files, or a notice indicating where to find the applicable terms."

Limite, seção 7: "All other non-permissive additional terms are considered "further restrictions" within the meaning of section 10."

**FATO (licença do RustDesk).** O arquivo `LICENCE` do RustDesk 1.5.0 é o texto da AGPL-3.0 sem termos adicionais da seção 7.

**INTERPRETAÇÃO.** Respostas às perguntas do pedido:

1. A MT pode recusar o uso da marca? Sim, mas só para "material you add". A MT pode declarar, com base em 7(e), que a licença não concede direito de marca sobre "MapDesk", "MT - Manfred Tecnologia" e os logotipos da MT. Também pode, com base em 7(b) e 7(c), exigir que o aviso de autoria da MT seja mantido e que versões modificadas do material da MT sejam marcadas como diferentes.
2. A MT não pode acrescentar termos sobre o código do RustDesk, nem restringir o uso do MapDesk além disso. Qualquer outro termo restritivo é "further restriction" e pode ser removido por quem recebe (seção 7, quarto parágrafo).
3. O termo tem de estar nos arquivos de código da MT, ou ali tem de haver aviso dizendo onde encontrá-lo.

**RISCO (médio).** A recusa da seção 7(e) é uma recusa de licença, e não cria direito de marca. Sem registro (decisão do Manfred), a MT não tem a propriedade da marca que o art. 129 da LPI associa ao registro (item 4.3). Um terceiro que redistribua o MapDesk com o nome e os logotipos da MT só pode ser enfrentado por concorrência desleal ou pela violação do próprio termo da seção 7. É o risco que a decisão de não registrar aceita.

### 2.6. Seção 13: interação remota por rede

**FATO LEGAL (licença).** Seção 13, primeiro parágrafo: "Notwithstanding any other provision of this License, if you modify the Program, your modified version must prominently offer all users interacting with it remotely through a computer network (if your version supports such interaction) an opportunity to receive the Corresponding Source of your version by providing access to the Corresponding Source from a network server at no charge, through some standard or customary means of facilitating copying of software."

E seção 0: "Mere interaction with a user through a computer network, with no transfer of a copy, is not conveying."

**INTERPRETAÇÃO (incidência).** A seção 13 tem cláusula de escopo própria: alcança quem modifica o programa (a MT modifica) e beneficia "users interacting with it remotely through a computer network". É preciso separar quem usa o MapDesk de que forma:

| Quem | Como usa | Regra que alcança |
|---|---|---|
| Cliente, na máquina dele | Executa uma cópia que recebeu | Seção 6 (recebeu cópia). Não é interação remota |
| Técnico da MT | Controla, pela rede, o MapDesk instalado na máquina do cliente | Interação remota com a versão modificada. Mas o técnico é a própria MT, que tem o código |
| Terceiro que se conecte a uma máquina com MapDesk pelo servidor da MT | Interação remota com a versão modificada | Seção 13 pode incidir. A probabilidade é baixa, porque o servidor e a chave são da MT e a aprovação é por clique |
| Servidor `hbbs` e `hbbr` | Imagem oficial sem modificação | Seção 13 não incide (verificação do VPS-MT, item 3.4) |

O caso não é o típico da seção 13, que é o de um serviço de rede modificado e oferecido ao público. O cliente MapDesk não é serviço de rede oferecido pela MT a terceiros: é um programa que a MT entrega em cópia. Mesmo assim, o programa "supports such interaction", porque recebe conexões remotas. A leitura mais segura é tratar a seção 13 como aplicável a quem se conecta remotamente.

**RECOMENDAÇÃO.** Cumprir as duas leituras de uma vez: código público e gratuito no GitHub e link para o código-fonte da versão na tela "Sobre". O link também aparece na página de download e nas notas da versão. Com isso, a dúvida de incidência fica sem efeito prático, e não há pendência a levar ao advogado neste ponto.

### 2.7. Requisitos de AGPL convertidos

| Requisito | Base | Natureza |
|---|---|---|
| Arquivo `LICENCE` do RustDesk mantido sem alteração na raiz do repositório | Seção 4, "give all recipients a copy of this License"; 5(b) | Obrigatório |
| Avisos de copyright e de licença do RustDesk mantidos no código e na tela "Sobre" ("Copyright © ... Purslane Tech Pte. Ltd.") | Seção 4; Lei nº 9.609/1998, art. 2º, § 1º | Obrigatório |
| Arquivo de aviso de modificação na raiz (por exemplo, `AVISO-DE-MODIFICACAO.md`), com origem (RustDesk, versão e tag), lista das mudanças da MT e data de cada versão | Seção 5(a) | Obrigatório |
| Aviso de que o MapDesk é distribuído sob a AGPL-3.0, no README, na página da versão e na tela "Sobre" | Seção 5(b) | Obrigatório |
| Nenhum arquivo do repositório com licença proprietária ou "todos os direitos reservados" sobre o código ou os recursos do MapDesk | Seção 5(c) | Obrigatório |
| Tela "Sobre" com copyright, ausência de garantia, permissão de redistribuir sob a AGPL-3.0 e link para o texto da licença | Seção 5(d) e definição da seção 0 | Recomendação (o original não tem os avisos completos) |
| Link para o código-fonte da mesma versão ao lado de cada executável: na página da versão do GitHub, na página de download do site e na tela "Sobre" | Seção 6(d); seção 13 | Obrigatório (6d) |
| Tag por versão distribuída, versões e tags antigas mantidas, submódulo `hbb_common` apontando para fork da MT | Seção 6(d), "for as long as needed" | Obrigatório (a forma é recomendação) |
| Fluxo do GitHub Actions no repositório público, sem segredos | Seção 1, "scripts to control those activities" | Obrigatório |
| Termo da seção 7 nos arquivos da MT: sem direito de marca sobre "MapDesk", "MT - Manfred Tecnologia" e logotipos; preservação do aviso de autoria da MT | Seção 7(b), (c) e (e) | Recomendação |

## 3. Marca RustDesk

### 3.1. Existe política de marca escrita?

**FATO (consulta em 05/10/2026).** Não foi encontrada política de marca do RustDesk:

- a raiz e a pasta `docs/` do repositório `rustdesk/rustdesk` na tag `1.5.0` não têm arquivo de marca (API do GitHub);
- o README da tag `1.5.0` só tem o "Misuse Disclaimer": "The developers of RustDesk do not condone or support any unethical or illegal use of this software. Misuse, such as unauthorized access, control or invasion of privacy, is strictly against our guidelines. The authors are not responsible for any misuse of the application.";
- a discussão nº 13963, sobre nome e logotipo próprios, teve resposta do mantenedor (05/01/2026) só com links de documentação, sem regra de marca;
- a busca na internet por política de marca do RustDesk não achou documento do titular.

**FATO (termos do RustDesk, vigência 16/09/2026).** Os termos de https://rustdesk.com/terms trazem, entre aspas retas aqui:

- definição: ""Software" means RustDesk Server Pro, the services Company operates at rustdesk.com including the public ID and relay servers, the Company website, and the accounts and licenses Company issues for them. "Software" does not include the RustDesk client or RustDesk Server OSS, which Company releases under their own open source license. This Agreement applies when you use the Software, including when you use the client to connect through the services Company operates."
- titularidade: "The Software and all intellectual property rights in and to the Software, including but not limited to patents, copyrights, trademarks, and trade secrets, are owned by Company and its licensors."
- cliente do Server Pro: "A custom client you build with RustDesk Server Pro does not carry a license to the Software, a right to Company's services, or any right to use Company's name or logos."
- "Company" é a Purslane Tech Pte. Ltd.

**INTERPRETAÇÃO.** Os termos do rustdesk.com não se aplicam ao MapDesk, porque excluem o cliente e o Server OSS da definição de "Software" e só alcançam o uso do cliente quando ele se conecta aos serviços da RustDesk. O MapDesk só fala com o servidor da MT. Isso depende de o cliente não acessar `*.rustdesk.com`, o que se confere na verificação de privacidade (consulta de versão e servidor de API). Os termos também mostram a posição do titular: nem o cliente customizado do produto pago leva direito de usar o nome ou os logotipos. É indício forte de que o titular não aceitaria um fork usando "RustDesk" como nome ou o logotipo do RustDesk.

### 3.2. Lei brasileira

**FATO LEGAL.** LPI, art. 129, caput: "A propriedade da marca adquire-se pelo registro validamente expedido, conforme as disposições desta Lei, sendo assegurado ao titular seu uso exclusivo em todo o território nacional, observado quanto às marcas coletivas e de certificação o disposto nos arts. 147 e 148." Incidência: define o que dá exclusividade de marca no Brasil.

**FATO LEGAL.** LPI, art. 126, caput: "A marca notoriamente conhecida em seu ramo de atividade nos termos do art. 6º bis (I), da Convenção da União de Paris para Proteção da Propriedade Industrial, goza de proteção especial, independentemente de estar previamente depositada ou registrada no Brasil."

**FATO LEGAL.** LPI, art. 132, IV: o titular da marca não poderá "impedir a citação da marca em discurso, obra científica ou literária ou qualquer outra publicação, desde que sem conotação comercial e sem prejuízo para seu caráter distintivo."

**FATO LEGAL.** LPI, art. 195: "Comete crime de concorrência desleal quem:" [...] "III - emprega meio fraudulento, para desviar, em proveito próprio ou alheio, clientela de outrem;" [...] "IV - usa expressão ou sinal de propaganda alheios, ou os imita, de modo a criar confusão entre os produtos ou estabelecimentos;" [...] "VI - substitui, pelo seu próprio nome ou razão social, em produto de outrem, o nome ou razão social deste, sem o seu consentimento;"

Incidência: o art. 195 não depende de registro de marca. Alcança a MT se o MapDesk for apresentado de modo a confundir com o RustDesk ou a apagar a origem.

**PENDÊNCIA DE VALIDAÇÃO 1.** Não foi possível confirmar se "RustDesk" está registrada ou depositada no INPI. A busca no INPI é feita à mão pelo Manfred (pesquisa por marca "rustdesk", exata e por radical). A busca na internet também não achou registro no USPTO, no EUIPO ou na OMPI. Até a confirmação, a análise trata "RustDesk" como sinal de terceiro protegido pelo art. 195 e, se registrado, pelo art. 129. A conclusão prática não muda.

**INTERPRETAÇÃO.** Com ou sem registro, o caminho seguro é o mesmo:

1. Não usar "RustDesk" como nome, parte do nome, ícone ou logotipo do MapDesk.
2. Citar a origem de forma descritiva, como fato e não como selo: "Baseado no RustDesk, software livre da Purslane Tech Pte. Ltd., distribuído sob a licença AGPL-3.0. O MapDesk não é produto oficial do RustDesk nem tem vínculo com seus desenvolvedores."
3. Manter o copyright da Purslane Tech. O que muda é o nome do programa, não a autoria.

**PENDÊNCIA DE VALIDAÇÃO 3.** O art. 195, VI, fala em substituir o nome de outrem "em produto de outrem" "sem o seu consentimento". A AGPL-3.0 autoriza modificar e redistribuir, e a modificação inclui trocar o nome exibido. Resta saber se essa autorização de direito autoral equivale ao "consentimento" do inciso VI, e se manter o copyright da Purslane Tech com a frase "Baseado no RustDesk" afasta o tipo. A leitura do agente é que sim, porque o produto distribuído passa a ser obra derivada da MT, licenciada para isso, e a origem é declarada. Mas é tipo penal, e a resposta pede advogado. É a questão 1 da consulta.

### 3.3. Onde a origem aparece

| Lugar | Texto (proposta, passa pela `humanizar-ptbr`) |
|---|---|
| Tela "Sobre" | "MapDesk [versão]. Baseado no RustDesk [versão base], software livre distribuído sob a licença AGPL-3.0. Copyright © [ano] Purslane Tech Pte. Ltd. Modificações: Copyright © [ano] MANFRED TECNOLOGIA LTDA. Este programa não tem garantia. Você pode redistribuí-lo e modificá-lo nos termos da licença. [Ver licença] [Código-fonte desta versão]" |
| README do repositório | Mesmo conteúdo, com a frase "não é produto oficial do RustDesk" |
| Página da versão (release) | Origem, versão base, lista de mudanças, data, link do código da tag |
| Página de download do site | Origem, licença, link do código, aviso de que não é produto oficial do RustDesk |

O aviso de copyright da MT só entra depois de o Manfred confirmar, como manda o `AGENTS-MT.md`.

## 4. Marca MapDesk

### 4.1. O que já foi feito

**FATO.** Busca exata "mapdesk" no INPI em 05/10/2026, sem resultado, base atualizada até 29/09/2026 (informação do Manfred, registrada no briefing do projeto, seção 1).

### 4.2. Busca na internet (05/10/2026)

| Achado | Onde | Ramo | Relevância |
|---|---|---|---|
| "MapDesk", publicador "Nittu", categoria "Productivity", lançado em 11/05/2026, atualizado em 24/09/2026 | Microsoft Store, https://apps.microsoft.com/detail/9nc8cvrt328c (dados lidos da API pública da loja) | Segundo o resumo do buscador, programa de mapas e GIS para Windows | Mesmo nome, mesma loja, mesma plataforma (Windows). Ramo diferente (mapas, não acesso remoto) |
| "MapDesk Layout", mesmo publicador "Nittu", lançado em 03/08/2026, atualizado em 13/09/2026 | Microsoft Store, https://apps.microsoft.com/detail/9pnmfhgf52n9 | Mapas e diagramação cartográfica | Idem |
| "Stiple Mapdesk", desenvolvedor Stiple Incorporated, categoria "Productivity", versão 1.3 | App Store, https://apps.apple.com/us/app/stiple-mapdesk/id6771081948 | Levantamento topográfico em iPhone e iPad | Nome quase igual, ramo diferente |
| "MapDesk for Mac", desenvolvedor Elonovo, versão 2.1.0, atualizado em 07/09/2026 | https://mapdesk.macupdate.com/ | Gestão de contatos e negócios em mapa | Ramo diferente |
| "MapDesk" do NSW Rural Fire Service (Austrália) | https://www.maps-group.org/mapdesk-info | Extensão do ArcGIS para mapas de incêndio | Uso institucional estrangeiro, ramo diferente |
| "MapDesk", editor do UMN MapServer, post de 10/11/2004 | https://blog.sourcepole.ch/2004/11/10/mapdesk/ | Mapas | Projeto antigo |
| Marca "MAPDESK", número de série 75542590 nos EUA, indicada como abandonada | Resultado do buscador apontando para https://trademarks.justia.com/755/42/mapdesk-75542590.html | Software de banco de dados e cartografia | A página devolveu erro 403 e não foi aberta. Dado não confirmado na fonte |
| Domínio `mapdesk.com` registrado desde 18/11/2017, servidores de nome `ns1.afternic.com` e `ns2.afternic.com` | RDAP da Verisign e DNS | Sem uso identificado | Servidores de nome de plataforma de venda de domínios |
| Domínio `mapdesk.com.br` | RDAP do Registro.br devolveu 404 | Não registrado na data da consulta | Livre na data |
| Google Play, "MapDesk" e "Map Desk" e "MapDesc" em software de acesso remoto | Buscas no buscador | Nenhum resultado | Sem achado |

**INTERPRETAÇÃO.** Nenhum achado é de acesso remoto, suporte técnico ou do Brasil. Todos os "MapDesk" encontrados são de mapas, GIS ou gestão em mapa, que é o sentido literal do nome. O achado mais próximo é o "MapDesk" da Microsoft Store: mesmo nome e mesma loja Windows, mas outro ramo. A busca na internet não substitui a busca no INPI e não alcança marcas de fato não indexadas.

**FATO LEGAL.** LPI, art. 124, XIX: não é registrável como marca a "reprodução ou imitação, no todo ou em parte, ainda que com acréscimo, de marca alheia registrada, para distinguir ou certificar produto ou serviço idêntico, semelhante ou afim, suscetível de causar confusão ou associação com marca alheia;" Incidência: regra de anterioridade que o INPI aplica a pedidos e que define o risco de conflito.

**INTERPRETAÇÃO.** O risco de conflito depende de produto "idêntico, semelhante ou afim". Programa de mapas e programa de acesso remoto são ambos programas de computador (classe 9), e a afinidade entre eles é a dúvida que só a busca por classe resolve. O radical "desk" é comum no ramo de acesso remoto (por exemplo, AnyDesk e o próprio RustDesk). Isso enfraquece a exclusividade do sufixo, mas aumenta a atenção sobre confusão com marcas do ramo.

**PENDÊNCIA DE VALIDAÇÃO 2.** Falta a busca no INPI por radical e semelhança, feita à mão pelo Manfred: "mapdesk", "map desk", "mapdesc" e "mapdesk-mt", nas classes 9 e 42, e uma conferência dos registros com "desk" no ramo de acesso remoto. A pendência não vai ao advogado, salvo se a busca achar algo.

### 4.3. Registro: classes e recomendação

**FATO.** O INPI diz: "O INPI adota a Classificação Internacional de Produtos e Serviços de Nice (NCL, na sigla em inglês)". A 13ª edição (NCL 13) vigora desde 01/01/2026 (página do INPI atualizada em 13/01/2026).

**FATO.** No documento do INPI "Caputs e notas explicativas NCL 13 2026":

- Classe 9, título, inclui "arquivos de multimídia gravados e baixáveis, programas de computador, mídias virgens digitais ou analógicas para gravação e armazenamento;"
- Classe 42, título, inclui "projeto e desenvolvimento de hardware e de software de computador." e, na nota explicativa, "software enquanto serviço (SaaS), plataforma enquanto serviço (PaaS);"

**INTERPRETAÇÃO.** O MapDesk é programa baixável: o enquadramento natural é a classe 9. A classe 42 entraria se a MT quisesse proteger o nome também para serviços de informática ligados ao programa. A especificação exata (o texto do produto ou serviço no pedido) se escolhe nas listas auxiliares do INPI no momento do pedido. Custo e prazo do INPI não foram verificados e não constam aqui.

**RECOMENDAÇÃO (decisão empresarial já tomada).** O Manfred decidiu em 05/10/2026 não registrar a marca, e esta verificação não reabre o item no projeto. Registram-se só os efeitos, para a decisão ficar informada:

- sem registro, a MT não tem a exclusividade do art. 129;
- o direito de precedência do art. 129, § 1º, protege quem "de boa fé, na data da prioridade ou depósito, usava no País, há pelo menos 6 (seis) meses, marca idêntica ou semelhante". Guardar prova de uso desde o lançamento (data da primeira versão pública e da página de download) preserva esse direito se um terceiro depositar o nome;
- o sufixo "-MT", se mantido no nome, liga o programa à MT e reduz a chance de confusão com os "MapDesk" de mapas.

Se a decisão mudar, a classe de partida é a 9, depois da busca da pendência 2.

## 5. Pendências de validação

São 6 pendências no total, numeradas igual nos dois arquivos de verificação e na consulta ao advogado. Quatro vão ao advogado (consulta `CONSULTA-ADVOGADO-mapdesk-agpl-marca-2026-10-05.md`, questões 1 a 4). Duas ficam com o Manfred, no INPI.

| # | Pendência | Onde | Quem |
|---|---|---|---|
| 1 | Se "RustDesk" está registrada ou depositada no INPI | item 3.2 | Manfred, busca no INPI |
| 2 | Busca por radical e semelhança de "MapDesk" nas classes 9 e 42 | item 4.2 | Manfred, busca no INPI |
| 3 | Se a licença AGPL-3.0, com a origem declarada e o copyright mantido, afasta a LPI, art. 195, VI, na troca do nome exibido | item 3.2 | Advogado, questão 1 |
| 4 | Licença do submódulo `hbb_common`, que não tem arquivo de licença, se a MT alterar arquivos dele | item 6.1 | Advogado, questão 2 |
| 5 | Marco Civil, art. 7º, IX, e o aviso de privacidade do cliente | `verificacao-privacidade-cliente-2026-10-05.md`, item 4.4 | Advogado, questão 3 |
| 6 | Papel da MT na sessão de suporte e base legal para empregados de clientes empresa | `verificacao-privacidade-cliente-2026-10-05.md`, item 4.3 | Advogado, questão 4 |

## 6. Ponto adicional encontrado: licença do `hbb_common`

### 6.1. Achado

**FATO (consulta em 05/10/2026).** O repositório `rustdesk/hbb_common` não tem arquivo de licença na raiz no commit `229b904508364c8997aad0fb5af57effac859f60`; a API do GitHub informa `"license": null`; o `Cargo.toml` não tem campo `license` e traz `authors = ["open-trade <info@opentradesolutions.com>"]`.

**INTERPRETAÇÃO.** O `hbb_common` é distribuído dentro do RustDesk, que está sob a AGPL-3.0, e é parte do código-fonte correspondente do executável oficial. Pela seção 5(c), a obra inteira fica sob a AGPL-3.0 para quem recebe uma cópia. A leitura é que quem recebe o RustDesk recebe também o `hbb_common` sob a AGPL-3.0. Mas o repositório isolado não declara licença, e a MT faria um fork público dele com alterações.

**RECOMENDAÇÃO.** O próprio levantamento de código (`achados-codigo-1.5.0.md`, seção "Configuração sem mexer no hbb_common") mostra que servidor, chave, nome e opções podem ser definidos no repositório `rustdesk` em tempo de execução, sem alterar o `hbb_common`. Seguir esse caminho reduz o ponto a distribuir o `hbb_common` sem modificação, como já faz o executável oficial. O fork sem alteração continua útil para garantir a disponibilidade (item 2.3). **PENDÊNCIA DE VALIDAÇÃO 4.** Se for preciso alterar o `hbb_common`, a licença para alterar e publicar o fork vai ao advogado antes da primeira versão. É a questão 2 da consulta.

## 7. Requisitos para implementação

Licença (AGPL-3.0):

- [ ] Manter o `LICENCE` do RustDesk sem alteração na raiz do repositório.
- [ ] Manter todos os avisos de copyright e de licença do RustDesk no código e o "Copyright © [ano] Purslane Tech Pte. Ltd." na tela "Sobre".
- [ ] Criar na raiz o arquivo de aviso de modificação: origem (RustDesk, versão e tag), lista das mudanças da MT e data de cada versão. Atualizar a cada versão.
- [ ] Dizer no README, na página da versão e na tela "Sobre" que o MapDesk é distribuído sob a AGPL-3.0.
- [ ] Nenhum arquivo do repositório com licença proprietária; ícones e cores da MT entram sob a AGPL-3.0.
- [ ] Tela "Sobre" com: título "Sobre o MapDesk", versão do MapDesk e versão base do RustDesk, copyright da Purslane Tech e da MT (este só depois da confirmação do Manfred), aviso de ausência de garantia, permissão de redistribuir sob a AGPL-3.0, link para o texto da licença, link para o código-fonte da versão.
- [ ] Trocar o link "Privacy Statement" (hoje `https://rustdesk.com/privacy.html`) pelo aviso de privacidade da MT, e o link "Website" pelo site da MT.
- [ ] Cada versão distribuída com tag própria; página da versão com o executável, o link do código da tag e a lista de mudanças com data.
- [ ] Nunca apagar versões nem tags já distribuídas.
- [ ] Submódulo `hbb_common` apontando para um fork da MT no commit usado.
- [ ] Fluxo do GitHub Actions no repositório público; certificado de assinatura e demais segredos fora do repositório.
- [ ] Página de download do site: link para o código-fonte da mesma versão ao lado do botão, link para a licença, aviso de que não há garantia e de que não é produto oficial do RustDesk.
- [ ] Termo da seção 7 nos arquivos da MT (ou aviso de onde está): a licença não concede direito de marca sobre "MapDesk", "MT - Manfred Tecnologia" e logotipos da MT; o aviso de autoria da MT deve ser mantido.

Marca RustDesk:

- [ ] Não usar "RustDesk" no nome, no ícone, no logotipo, no nome do executável, do serviço do Windows ou do instalador.
- [ ] Citar a origem com a frase descritiva do item 3.2 na tela "Sobre", no README, na página da versão e na página de download.
- [ ] Conferir que nenhuma tela, texto de tradução ou recurso visual mostra o logotipo do RustDesk.
- [ ] Preferir a configuração em tempo de execução, sem alterar o `hbb_common` (item 6.1).

Marca MapDesk:

- [x] Nome final definido: "MapDesk-MT", repositório `manfredjr/mapdesk-mt` (05/10/2026).
- [ ] Busca no INPI por radical e semelhança nas classes 9 e 42 (pendência 2).
- [ ] Guardar prova da data da primeira versão pública e da página de download (precedência do art. 129, § 1º, da LPI).

## 8. Pontos pendentes de parecer jurídico

O projeto tem **6 pontos** que não foi possível validar em fonte oficial: 4 analisados neste arquivo (pendências 1 a 4) e 2 em `verificacao-privacidade-cliente-2026-10-05.md` (pendências 5 e 6), listados aqui para a contagem bater. Os demais foram verificados e estão nas fontes da seção 1.3.

Encaminhado para parecer em `CONSULTA-ADVOGADO-mapdesk-agpl-marca-2026-10-05.md` (pendências 3 a 6). As pendências 1 e 2 dependem da busca do Manfred no INPI.

| # | Ponto | Onde aparece | Por que não foi possível concluir |
|---|---|---|---|
| 1 | Registro de "RustDesk" no INPI | item 3.2 | A busca no INPI é manual; a internet não mostrou registro |
| 2 | Anterioridade de "MapDesk" por radical | item 4.2 | Só a busca no INPI por classe responde |
| 3 | LPI, art. 195, VI, e a troca do nome | item 3.2 | Tipo penal; o alcance do "consentimento" pede advogado |
| 4 | Licença do `hbb_common` | item 6.1 | O repositório não declara licença |
| 5 | Marco Civil, art. 7º, IX | verificação de privacidade, item 4.4 | Relação com a LGPD é interpretação controversa |
| 6 | Papel da MT na sessão de suporte | verificação de privacidade, item 4.3 | Depende do contrato de suporte, que não existe por escrito |

**Não utilize esta verificação nesses pontos específicos antes do parecer ou da busca.** O restante está verificado.
