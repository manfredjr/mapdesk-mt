# Parecer técnico e jurídico: monitor virtual e impressora remota

Data: 02/11/2026. Projeto MAPDESK-MT. Feito com a skill `legal-br`. Decisão do Manfred em 02/11/2026, depois deste parecer: manter o monitor virtual, com o crédito à Amyuni, e deixar a impressora remota fora. Corrige `licencas-binarios-terceiros-2026-11-02.md`, itens 3.1 e 3.2, escritos sem abrir os pacotes.

## 1. Monitor virtual (`usbmmidd_v2`)

**FATO, conferido nos arquivos.**

- O pacote tem `License.txt`, com "Copyright 2014-2021 Amyuni Technologies Inc.".
- SHA-256 do `usbmmidd_v2.zip`: `629b51e9944762bae73948171c65d09a79595cf4c771a82ebc003fbba5b24f51`. É o mesmo do arquivo baixado de https://www.amyuni.com/downloads/usbmmidd_v2.zip em 02/11/2026.
- Os binários do driver trazem a Amyuni como autora e têm a assinatura de driver da Microsoft válida.
- A licença diz: "Permission is granted to anyone to use this software for any purpose subject to the following restrictions".

Condições da licença:

1. Não atribuir a si a autoria. Em produto, "an acknowledgment in the product documentation would be required".
2. Versão alterada precisa ser marcada como tal.
3. O aviso não pode ser removido nem alterado da distribuição.
4. Quem usa aceita "to be prompted with an advertisement page", e existe uma versão comercial para quem não quer esses anúncios.

**INTERPRETAÇÃO.**

- A MT pode distribuir o driver, inclusive em uso comercial, cumprindo essas condições. A licença é da Amyuni, e o RustDesk não aparece nela.
- Sair do pacote `Win32`, `deviceinstaller` e o `.bat` não altera o driver, e o `License.txt` continua na pasta empacotada pelo workflow.
- O driver é programa à parte, instalado no Windows, e pode ser tratado como "aggregate" (AGPL-3.0, seção 5). Nesse caso, a AGPL não alcança o driver. Essa leitura é a pergunta 7 do complemento à consulta.

**RISCO.** Baixo, depois de cumprir as condições. Hoje falta o reconhecimento na documentação do produto. A busca nos arquivos do projeto não achou menção à Amyuni fora do código.

**O que falta conferir.** Se o anúncio aparece. Uma busca de textos no `usbmmIdd.dll` de 64 bits não achou endereço de anúncio, o que não prova que ele não exista. O site da Amyuni devolveu 503 na página inicial e no fórum nesta consulta, e uma busca na internet não achou outros termos para esse driver.

## 2. Impressora remota (driver e adaptador)

**FATO, conferido nos arquivos.**

- O `.inf` do driver diz "Copyright (c) 2024 RustDesk". Os pacotes foram enviados pela conta `rustdesk` e nenhum traz arquivo de licença.
- O filtro de impressão tem assinatura de driver da Microsoft válida e metadados de exemplo do kit de desenvolvimento da Microsoft. O caminho gravado nele é `D:\Projects\rust\RustDeskPrinterDriver\...`.
- O adaptador não tem assinatura. Ele traz textos de código Rust do RustDesk, como `src\ipc.rs` e `custom.txt`.
- O código-fonte não foi localizado. A busca no GitHub só achou referências em `rustdesk/rustdesk`. Os repositórios `rustdesk-org/RustDeskPrinterDriver` e `rustdesk/RustDeskPrinterDriver` devolvem 404. Pode existir repositório privado.

**INTERPRETAÇÃO.**

- O RustDesk não parece estar irregular só por isso: quem é dono do próprio código pode distribuí-lo como quiser, e a AGPL obriga quem recebe a licença, não o titular.
- A MT está em outra posição. Ela é licenciada e, ao transmitir o programa, precisa oferecer o código correspondente. A AGPL inclui nele "the source code for shared libraries and dynamically linked subprograms that the work is specifically designed to require". O adaptador é carregado pelo programa e foi feito para ele, então a MT provavelmente precisaria do código dele e não o tem.
- O driver instalado à parte tem leitura melhor como "aggregate", mas segue sem licença escrita.

**RISCO.** Médio a alto para a MT, enquanto faltar a licença e o código. O recurso só imprime do lado do técnico.

**Caminho para mantê-lo.** Pedir ao RustDesk a licença e o código. É mensagem em nome da MT e sai só com a frase do Manfred.

## 3. Princípio: "se o RustDesk usa, por que eu não posso?"

- A AGPL não é uma licença geral sobre tudo o que o RustDesk distribui. Ela cobre o programa, e cada componente de terceiro tem a sua.
- Para o monitor virtual, a MT pode pela licença da própria Amyuni.
- Para a impressora, a MT não recebe a mesma liberdade do dono do código, porque precisa cumprir a AGPL como licenciada.
- Nada do que foi conferido mostra ilegalidade do RustDesk. Esta análise não examina se ele cumpre as condições da Amyuni.

## 4. O que não foi coberto

- Os programas não foram executados: só leitura de arquivos, metadados e textos.
- O texto da Amyuni é de licença estrangeira, sem lei ou foro indicados. Eficácia no Brasil e a leitura de "aggregate" ficam para o advogado.
- Fontes da web: busca de 02/11/2026. Os contratos da Amyuni encontrados tratam dos produtos de PDF, não deste driver.

## 5. Requisitos

- [x] Manter o `usbmmidd_v2` e fixar o SHA-256 acima no workflow, que também falha se o `License.txt` sair do pacote.
- [x] Citar a Amyuni em `AVISO-DE-MODIFICACAO.md` e nas notas da versão.
- [ ] Levar o texto da licença ao arquivo de avisos de terceiros.
- [ ] Testar se aparece anúncio numa máquina com o monitor virtual ativo.
- [x] Manter a impressora fora, até haver licença e código.

Autor: Manfred Heil Junior
