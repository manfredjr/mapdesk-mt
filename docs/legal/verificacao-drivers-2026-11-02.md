# Parecer técnico e jurídico: monitor virtual e impressora remota

Data: 02/11/2026. Projeto MAPDESK-MT. Feito com a skill `legal-br`. Decisão do Manfred em 02/11/2026: manter o monitor virtual, com o crédito à Amyuni, e deixar a impressora remota fora. Sobre o pedido à Amyuni, ele disse: "Eles nem vão me responder isso, eu só vou perder tempo. Tá? Se não tem nada lá dentro, seguimos como está a questão do Rust Desk, da mesma forma." Depois, com os riscos explicados, escolheu no mesmo dia a opção "Publicar com o driver da Amyuni, com você assumindo a dúvida da permissão e a do código, e deixar a troca para a `1.5.0-mt.2`". Corrige `licencas-binarios-terceiros-2026-11-02.md`, itens 3.1 e 3.2, escritos sem abrir os pacotes.

## 1. Monitor virtual (`usbmmidd_v2`)

**FATO, conferido nos arquivos.**

- O pacote tem `License.txt`, com "Copyright 2014-2021 Amyuni Technologies Inc.".
- SHA-256 do `usbmmidd_v2.zip`: `629b51e9944762bae73948171c65d09a79595cf4c771a82ebc003fbba5b24f51`. É o mesmo do arquivo baixado de https://www.amyuni.com/downloads/usbmmidd_v2.zip em 02/11/2026.
- Os binários do driver trazem a Amyuni como autora e têm a assinatura de driver da Microsoft válida.
- A licença diz: "Permission is granted to anyone to use this software for any purpose subject to the following restrictions".

Restrições numeradas da licença:

1. Não atribuir a si a autoria. Em produto, "an acknowledgment in the product documentation would be required".
2. Versão alterada precisa ser marcada como tal.
3. O aviso não pode ser removido nem alterado da distribuição.

Em parágrafo separado, a licença diz que quem usa aceita "to be prompted with an advertisement page which is not always under the control of the author", e que existe uma versão comercial para quem não quer esses anúncios.

**O que falta no texto.** A licença segue o modelo da zlib, conferido em https://zlib.net/zlib_license.html em 02/11/2026, que diz: "for any purpose, including commercial applications, and to alter it and redistribute it freely". O texto da Amyuni não traz "including commercial applications" nem "redistribute it freely". O direito de usar é expresso. O de distribuir não é.

**TEXTO LEGAL.** Lei nº 9.610/1998, art. 4º: "Interpretam-se restritivamente os negócios jurídicos sobre os direitos autorais". O art. 29 diz que depende de "autorização prévia e expressa do autor" a utilização da obra, e o inciso VI inclui "a distribuição, quando não intrínseca ao contrato firmado pelo autor com terceiros para uso ou exploração da obra". A Lei nº 9.609/1998, art. 2º, liga o programa de computador a esse regime: "é o conferido às obras literárias pela legislação de direitos autorais". O inciso VII do art. 29 trata de "qualquer outro sistema que permita ao usuário realizar a seleção da obra" e não traz a ressalva do VI. O art. 12 da Lei nº 9.609/1998 tipifica "Violar direitos de autor de programa de computador". Verificado em `fontes/leis` da `legal-br`, em dia no relatório de 02/11/2026. Incidência: o driver é programa de computador da Amyuni, e a MT o entregaria dentro do `.exe`, pela versão publicada na conta do projeto, a quem baixar.

**INTERPRETAÇÃO.**

- **Leitura favorável:** "for any purpose", "If you use this software in a product" e "from any distribution" supõem que o programa seja entregue dentro de produtos e distribuído. A licença seria uma permissão implícita de distribuir, e a ressalva do inciso VI ("quando não intrínseca ao contrato") ajuda essa leitura.
- **Leitura contrária:** a Amyuni partiu de um modelo que autoriza redistribuir e não repetiu essas palavras, ainda que não se saiba o motivo. Com o art. 4º e a exigência de autorização expressa do art. 29, a distribuição pode ficar sem permissão. O inciso VII, sem a ressalva do VI, pode alcançar o download, e isso fica para o advogado. As duas leituras são defensáveis, e esta verificação não escolhe entre elas.
- **Retirada de arquivos:** sair do pacote `Win32`, `deviceinstaller` e o `.bat` não mexe nos arquivos de 64 bits do driver, e o `License.txt` continua intacto na pasta empacotada. A licença não diz se um subconjunto conta como versão alterada, então o aviso de modificação declara a retirada, para atender à restrição 2 de qualquer forma.
- **AGPL:** a seção 5 define "aggregate" como obras "separate and independent", "not by their nature extensions" e "not combined with it such as to form a larger program". O driver é programa de outro autor, instalado no Windows, mas vai dentro do `.exe` único, e o programa tem o nome e o caminho dele fixos (`src/virtual_display_manager.rs`). A seção 1 inclui no código correspondente "the source code for shared libraries and dynamically linked subprograms that the work is specifically designed to require, such as by intimate data communication or control flow between those subprograms and other parts of the work", e exclui "generally available free programs which are used unmodified in performing those activities but which are not part of the work". O nome fixo pesa contra a MT. O fato de ser programa de outro autor, sem alteração, pesa a favor. O driver é gratuito e fechado, e o preâmbulo da AGPL diz sobre "free software": "we are referring to freedom, not price". A exclusão de "free programs" pode não alcançá-lo. Se essas leituras não vingarem, a MT não tem o código do driver para oferecer. É a pergunta 7 do complemento à consulta.

**RISCO.** Médio, em duas dúvidas separadas: a permissão de distribuir e o dever de oferecer o código. As duas foram assumidas pelo Manfred, conforme a decisão no topo, e só mudam com a resposta do advogado à pergunta 7 ou com a troca do driver. A leitura anterior desta verificação, de risco baixo, tratava só das restrições numeradas.

**Caminhos para reduzir o risco.** Nenhum foi adotado na `1.5.0-mt.1`, por decisão do Manfred.

- **Pedir à Amyuni autorização escrita para distribuir.** Resolve a permissão e pode resolver o anúncio, conforme a resposta. Não resolve a dúvida da AGPL sobre o código. É mensagem em nome da MT e sai só com a frase do Manfred.
- **Comprar a versão comercial.** A licença a cita só por causa dos anúncios. Se resolve a permissão, depende dos termos. Preço e termos: `[FONTE?]`. Pelo que se sabe, não resolve a dúvida da AGPL.
- **Fazer o programa baixar o driver do site da Amyuni, na máquina de quem usa.** A MT deixaria de entregar o arquivo, o que pode resolver a permissão de distribuir, mas o anúncio e a dúvida da AGPL sobre o código continuam. O programa teria de conferir o SHA-256 por conta própria, dependeria do site dela, cuja página inicial respondeu 503 nesta consulta, e a máquina do cliente passaria a falar com um terceiro, o que exige rever a página de privacidade. Não testado.
- **Usar o `RustDeskIddDriver`, com licença MS-PL no GitHub.** Resolveria a permissão da Amyuni e o anúncio, mas a troca vai além da constante `IDD_IMPL`: o código carrega `dylib_virtual_display.dll` (`libs/virtual_display`), e o workflow da MT não baixa esse driver. Falta conferir a assinatura no Windows. A lista da FSF (https://www.gnu.org/licenses/license-list.html, consulta em 02/11/2026) diz que a Ms-PL é "incompatible with the GNU GPL" e não trata da AGPL nesse trecho, então a compatibilidade fica para o advogado. Não testado.
- **Usar o `Virtual-Display-Driver`, com licença MIT no GitHub.** É a candidata à troca na `1.5.0-mt.2`. Avaliação em `verificacao-driver-mit-2026-11-02.md`. Faltam o teste de instalação, a origem MS-PL e a leitura da AGPL.

**Engenharia reversa.** O Manfred perguntou se daria para refazer o driver assim, e escolheu não seguir esse caminho em 02/11/2026. Um driver novo ainda precisaria de certificado, e o feito a partir do binário pode ser visto como derivado.

**O que falta conferir.** Se o anúncio aparece. Buscas de textos no `usbmmIdd.dll` de 64 bits não acharam endereço de anúncio nem bibliotecas de rede, o que não prova que ele não exista. Um teste sem anúncio vale só para aquele teste, porque a licença diz que a página nem sempre depende do autor. O anúncio prende quem usa, ou seja, o cliente, e os textos do produto ainda não falam dele. O site da Amyuni devolveu 503 na página inicial e no fórum nesta consulta, e uma busca na internet não achou outros termos para esse driver. Pode haver texto da Amyuni que autorize a redistribuição.

## 2. Impressora remota (driver e adaptador)

**FATO, conferido nos arquivos.**

- O `.inf` do driver diz "Copyright (c) 2024 RustDesk". Os pacotes foram enviados pela conta `rustdesk` e nenhum traz arquivo de licença.
- O filtro de impressão tem assinatura de driver da Microsoft válida e metadados de exemplo do kit de desenvolvimento da Microsoft. O caminho gravado nele é `D:\Projects\rust\RustDeskPrinterDriver\...`.
- O adaptador não tem assinatura. Ele traz textos de código Rust do RustDesk, como `src\ipc.rs` e `custom.txt`.
- O código-fonte do pacote não foi localizado. Os repositórios `rustdesk-org/RustDeskPrinterDriver` e `rustdesk/RustDeskPrinterDriver` devolvem 404. Pode existir repositório privado.
- Existe uma reimplementação aberta do adaptador, sem relação conferida com o pacote: a pasta `printer-adapter` de `bryangerlach/rdgen`, em repositório GPL-3.0 segundo a API do GitHub.
- O adaptador traz os textos `WinVerifyTrust`, `CertGetNameStringW`, `codesign-verify-rs` e `PURSLANEHUABINGRUSTDESK`. Isso sugere que ele confere a assinatura do programa, mas nada foi executado.

**INTERPRETAÇÃO.**

- O RustDesk não parece estar irregular só por isso: quem é dono do próprio código pode distribuí-lo como quiser, e a AGPL obriga quem recebe a licença, não o titular.
- A MT está em outra posição. Ela é licenciada e, ao transmitir o programa, precisa oferecer o código correspondente. A AGPL inclui nele "the source code for shared libraries and dynamically linked subprograms that the work is specifically designed to require, such as by intimate data communication or control flow between those subprograms and other parts of the work". O adaptador é carregado pelo programa e foi feito para ele, então a MT provavelmente precisaria do código dele e não o tem.
- O driver instalado à parte pode ser lido como "aggregate" pelos mesmos critérios do item 1. O nome dele também é fixo no programa (`libs/remote_printer`), e os autores são os do RustDesk, não um terceiro. Segue sem licença escrita.

**RISCO.** Médio a alto para a MT, enquanto faltar a licença e o código. O recurso só imprime do lado do técnico.

**Caminho para mantê-lo.** Pedir ao RustDesk a licença e o código, o que é mensagem em nome da MT e sai só com a frase do Manfred. Isso pode não bastar, se o adaptador recusar programa sem a assinatura do RustDesk. A reimplementação aberta fica como pendência, sem avaliação.

## 3. Princípio: "se o RustDesk usa, por que eu não posso?"

**INTERPRETAÇÃO.**

- A AGPL não é uma licença geral sobre tudo o que o RustDesk distribui. Ela cobre o programa, e cada componente de terceiro tem a sua.
- Para o monitor virtual, o que vale é a licença da Amyuni: uso expresso, distribuição por leitura, como no item 1.
- Para a impressora, a MT não recebe a mesma liberdade do dono do código, porque precisa cumprir a AGPL como licenciada.
- Nada do que foi conferido mostra ilegalidade do RustDesk. Esta análise não sabe se ele tem acordo com a Amyuni (`[FONTE?]`), e um acordo dele não passaria à MT.

## 4. O que não foi coberto

- Os programas não foram executados: só leitura de arquivos, metadados e textos.
- O texto da Amyuni é de licença estrangeira, sem lei ou foro indicados. Eficácia no Brasil e a leitura de "aggregate" ficam para o advogado.
- Fontes da web: busca de 02/11/2026. Os contratos da Amyuni encontrados tratam dos produtos de PDF, não deste driver.

## 5. Requisitos

- [x] Manter o `usbmmidd_v2` e fixar o SHA-256 acima no workflow, que também falha se o `License.txt` sair do pacote.
- [x] Citar a Amyuni em `AVISO-DE-MODIFICACAO.md` e nas notas da versão, e declarar os arquivos retirados.
- [ ] Levar o texto da licença ao arquivo de avisos de terceiros, que acompanha o programa.
- [ ] Testar se aparece anúncio numa máquina com o monitor virtual ativo, de preferência com captura de rede, e definir como o cliente fica sabendo dessa cláusula.
- [x] Decidir a permissão de distribuir e o dever de código: dúvidas assumidas pelo Manfred em 02/11/2026, sem pedido à Amyuni.
- [ ] Testar a troca pelo driver MIT e decidir na `1.5.0-mt.2`.
- [x] Ajustar a frase "O código completo desta versão, sob a mesma licença" de `public/index.html`, porque o pacote leva o driver da Amyuni sem código e sob outra licença.
- [x] Manter a impressora fora, até haver licença e código.

Autor: Manfred Heil Junior
