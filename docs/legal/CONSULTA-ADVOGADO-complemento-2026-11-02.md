# Complemento à consulta ao advogado: licenças de terceiros e titularidade

Data: 02/11/2026. Projeto MAPDESK-MT. Vai junto com `CONSULTA-ADVOGADO-mapdesk-agpl-marca-2026-10-05.md`. A numeração continua a da consulta, em que a questão 5 trata das consultas STUN.

O envio é decisão do Manfred. Os fatos e as leituras estão em `licencas-binarios-terceiros-2026-11-02.md`, em `verificacao-drivers-2026-11-02.md` e em `verificacao-publicacao-sem-cessao-2026-11-02.md`.

## Questão 6: componente sem licença localizada

**Pergunta.** A MT pode distribuir o driver de impressora, o adaptador, o `hwcodec` e o `hbb_common` compilado sem licença expressa, pelo fato de virem no build oficial de um programa AGPL?

**Leituras possíveis.** (a) Não pode sem autorização, o que é o risco maior. (b) No caso dos autores do RustDesk, a seção 5(c) da AGPL-3.0 cobre as partes da obra. Correção de 02/11/2026: o `usbmmidd_v2` saiu desta pergunta e foi para a questão 7, porque o pacote traz uma licença da Amyuni (`verificacao-drivers-2026-11-02.md`).

**Impacto prático.** Tirar os componentes do build ou mantê-los. O driver de impressora e o adaptador saíram do build em 02/11/2026, e a resposta define se podem voltar.

**Urgência.** Antes da primeira tag, salvo decisão escrita do Manfred.

## Questão 7: driver como agregado e licença da Amyuni

**Pergunta.** Um driver instalado à parte pelo programa, como o `usbmmidd_v2` da Amyuni, conta como "aggregate" (AGPL-3.0, seção 5) ou como parte da obra? A exclusão de "generally available free programs" da seção 1 alcança um driver gratuito e fechado, se a AGPL diz que "free" se refere a liberdade? A licença da Amyuni, estrangeira e sem lei ou foro indicados, diz "Permission is granted to anyone to use this software for any purpose". Ela segue o modelo da zlib, sem as palavras "including commercial applications" e "redistribute it freely", e fala em "product" e "any distribution" nas restrições. Diante dos arts. 4º e 29, VI ("quando não intrínseca ao contrato") e VII, da Lei nº 9.610/1998, esse texto autoriza a MT a distribuir o driver dentro do executável? A cláusula em que quem usa aceita uma página de anúncio cria algum dever da MT perante o cliente?

**Impacto prático.** Define o dever de oferecer o código do driver e se ele pode ficar no build sem autorização escrita da Amyuni.

**Urgência.** A tag não espera esta resposta: em 02/11/2026 o Manfred decidiu manter o `usbmmidd_v2` e assumir a dúvida da permissão e a do código. Para a impressora, só se ela voltar ao build.

## Questão 8: patentes de H.264 e HEVC

**Pergunta.** A distribuição gratuita pela MT, no Brasil, gera obrigação de licença ou de royalties?

**Impacto prático.** Manter ou desligar esses codecs.

**Urgência.** Antes da primeira tag, salvo decisão escrita do Manfred.

## Questão 9: titularidade e licença das mudanças antes da cessão

**Pergunta.** Sem contrato específico, o art. 4º da Lei nº 9.609/1998 alcança as mudanças feitas por quem é sócio ou administrador da MT? Se não alcançar, quem concede a AGPL-3.0 sobre essas mudanças, e uma autorização escrita curta do autor à MT resolve o período até a cessão? O art. 49, III, da Lei nº 9.610/1998 limita essa autorização?

**Leituras possíveis.** (a) Os direitos ficam com a pessoa física até a cessão, e a MT precisa de autorização dela para distribuir. (b) O art. 4º alcança as mudanças, se houver vínculo de serviço com esse objeto, e a cessão só confirma a situação.

**Impacto prático.** Define quem assina o quê e como a minuta descreve as mudanças já feitas.

**Urgência.** Antes da primeira venda.

## Resumo

| Questão | Tema | Urgência |
|---|---|---|
| 6 | Componente sem licença localizada | Antes da primeira tag, salvo decisão escrita |
| 7 | Driver como agregado e licença da Amyuni | Não segura a tag, por decisão do Manfred em 02/11/2026 |
| 8 | Patentes de H.264 e HEVC | Antes da primeira tag, salvo decisão escrita |
| 9 | Titularidade e licença antes da cessão | Antes da primeira venda |
