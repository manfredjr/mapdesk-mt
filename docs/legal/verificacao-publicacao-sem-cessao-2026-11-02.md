# Verificação jurídica: publicação do MapDesk-MT antes da cessão

Data: 02/11/2026. Projeto MAPDESK-MT. Feita com a skill `legal-br`.

Decisão do Manfred em 02/11/2026: a versão pública pode sair antes da assinatura da cessão, porque o programa é gratuito. O contrato precisa estar assinado antes de qualquer venda. Ele está com o grupo do contrato único e depende do contador.

Nota de 05/11/2026: o Manfred confirmou que o programa nunca é cobrado e que serve de ferramenta do serviço de suporte aos clientes. O contrato desse serviço segue fora desta análise, e o "Resultado" abaixo é o de 02/11/2026.

**Resultado:** a publicação gratuita sob a AGPL-3.0 não depende da cessão para acontecer, na leitura abaixo. Enquanto a cessão não sai, a MT não deve se afirmar titular das mudanças. Só um texto faz isso hoje: a linha 17 do `AGENTS-MT.md`, que convém ajustar antes da tag. A tela Sobre, os metadados, a página e os avisos não afirmam a MT como titular.

## 1. Premissas

| Premissa | O que aciona | Fundamento |
|---|---|---|
| As mudanças da MT foram escritas pelo autor pessoa física apontado no projeto | Lei nº 9.610/1998, art. 11 | `AGENTS-MT.md`, seção "Autoria e licença" |
| O programa é de computador | Lei nº 9.609/1998, art. 2º | Regime de direito autoral, "observado o disposto nesta Lei" |
| O programa é obra derivada sob a AGPL-3.0 | Arquivo `LICENCE` | `AVISO-DE-MODIFICACAO.md` |
| A entrega é gratuita, sem venda da licença | Decisão do Manfred | O suporte da MT pode ser pago, e esse contrato não entrou nesta análise |

**Hipótese não confirmada:** este repositório não traz contrato de trabalho, de prestação de serviços ou outro vínculo entre o autor e a MT que trate de desenvolvimento. Existência desse vínculo: `[FONTE?]`. A análise segue sem ele, porque o projeto parte da cessão escrita (`docs/superpowers/pendencias.md`).

Fontes conferidas em 02/11/2026: https://www.planalto.gov.br/ccivil_03/leis/l9610.htm e https://www.planalto.gov.br/ccivil_03/leis/l9609.htm. A conferência foi online. Correção: o clone da `legal-br` usado aqui não tinha `STATUS-FONTES.md`, mas a cópia instalada tem, gerado em 02/11/2026, e as duas leis estão EM DIA nele. A AGPL-3.0 foi lida no arquivo `LICENCE`.

## 2. O que fica em nome de quem

**FATO LEGAL.**

- Lei nº 9.610/1998, art. 11: "Autor é a pessoa física criadora de obra literária, artística ou científica." Parágrafo único: "A proteção concedida ao autor poderá aplicar-se às pessoas jurídicas nos casos previstos nesta Lei."
- Art. 49, II: "somente se admitirá transmissão total e definitiva dos direitos mediante estipulação contratual escrita".
- Art. 49, III: "na hipótese de não haver estipulação contratual escrita, o prazo máximo será de cinco anos".
- Art. 50: "A cessão total ou parcial dos direitos de autor, que se fará sempre por escrito, presume-se onerosa."
- Lei nº 9.609/1998, art. 4º: "Salvo estipulação em contrário, pertencerão exclusivamente ao empregador, contratante de serviços ou órgão público, os direitos relativos ao programa de computador, desenvolvido e elaborado durante a vigência de contrato ou de vínculo estatutário", nas condições que o artigo descreve.
- Art. 4º, § 2º: os direitos ficam com o empregado ou contratado quando o programa é gerado sem relação com o contrato e sem o uso de recursos do empregador ou contratante.
- AGPL-3.0, seção 2: os direitos da licença "are irrevocable provided the stated conditions are met".

**INTERPRETAÇÃO.**

| Parte | Com quem fica enquanto não há cessão |
|---|---|
| Código original do RustDesk | Com os titulares de origem, sob a AGPL-3.0. Nada muda |
| Mudanças da MT no código | Com o autor pessoa física, salvo se existir vínculo que acione o art. 4º da Lei nº 9.609/1998 |
| Textos, imagens e logotipos feitos para o produto | Mesma regra das mudanças, pela Lei nº 9.610/1998. A autoria de cada peça não foi conferida aqui |
| Direito de distribuir | Da MT e de qualquer pessoa, como licenciada da AGPL-3.0, desde que cumpra as condições da licença |

**Quem concede a AGPL-3.0 sobre as mudanças.** Sem a cessão, a licença da MT sobre o código de origem não responde a isso. Sobre as mudanças, quem pode licenciar é o autor pessoa física. O `AVISO-DE-MODIFICACAO.md` declara a AGPL-3.0 em nome da MT, e o repositório e as versões ficam na conta pessoal `manfredjr`, sem documento que ligue um ao outro. A leitura mais segura é o autor deixar por escrito que autoriza a MT a distribuir as mudanças sob a AGPL-3.0, enquanto a cessão não vem. O art. 49, III, indica prazo máximo de cinco anos quando falta contrato escrito, e o alcance disso aqui fica para o advogado (questão 9 do complemento).

O art. 4º depende do vínculo: ser sócio ou administrador não basta para acioná-lo na leitura do texto, que fala em empregado, contratado de serviço e servidor. Essa leitura e o enquadramento do autor ficam para o advogado.

A cessão assinada depois não apaga o que já saiu. Quem recebeu a versão sob a AGPL-3.0 continua com a licença, e a MT recebe os direitos com essa licença já concedida. É preciso que o contrato cite as mudanças já feitas, para não restarem dúvidas, porque o art. 49, VI, manda interpretar o contrato restritivamente quando faltar a modalidade de utilização.

**RISCO.**

- Baixo na publicação gratuita: o autor e a MT agem na mesma direção, e a licença é pública. A base disso ainda não está escrita, e o risco cai mais com a autorização citada acima.
- Médio se a MT agir como dona antes da cessão. Sem o título, ela fica sem base própria para cobrar por licença, dar licença diferente da AGPL-3.0 ou reclamar de cópia das mudanças.
- Médio na fronteira do que é "venda". Vender suporte não é o mesmo que vender o programa, mas pacote em que o programa entra como item cobrado pede a cessão antes (INTERPRETAÇÃO). Na dúvida, o contrato vem primeiro.
- O art. 50 presume a cessão onerosa. Se ela for gratuita, o contrato precisa dizer isso, ponto que o contador deve ver.

## 3. Textos conferidos

| Onde | O que diz | Fato | Precisa de ajuste antes da tag? |
|---|---|---|---|
| `AGENTS-MT.md`, linha 17 | "a titular é a MANFRED TECNOLOGIA LTDA", no presente | Afirma a titularidade e vai na tag | **Sim, recomendado.** Exemplo de sentido: a MT passa a ser titular das mudanças quando a cessão for assinada |
| `flutter/windows/runner/Runner.rc`, linha 96, e `libs/portable/Cargo.toml`, linha 29 | Copyright da Purslane Tech, seguido de "Modificado por MT - Manfred Tecnologia. AGPL-3.0." | Diz quem modificou, sem copyright da MT | Não |
| `Runner.rc`, linha 92, e `Cargo.toml`, linha 33 | `CompanyName` "MT - Manfred Tecnologia" | Identifica quem distribui | Não |
| Tela Sobre, `flutter/lib/desktop/pages/desktop_setting_page.dart`, linhas 2603 e 2608 | Copyright da Purslane Tech e "Versão modificada pela MT - Manfred Tecnologia" | Sem copyright da MT | Não |
| `AVISO-DE-MODIFICACAO.md`, linhas 5 e 23 | "modificado pela MT"; a licença não dá uso dos nomes e dos "logotipos da MT" | Trata de modificação e de sinais, não do código | Não |
| `docs/notas-versao.md`, linha 3 | A MT "mexe no programa desde 05/10/2026" | Sem afirmação de titularidade | Não |
| `public/index.html`, linhas 78 e 81 | "A MT modificou o programa"; nomes e logotipos fora da licença do código | Sem afirmação de titularidade | Não |
| `public/index.html`, linha 88 | Autorização "do titular", sem dizer quem é | Neutro | Não |
| `public/index.html`, linha 97, e `public/privacidade.html`, linhas 43 e 52 | "por MT - Manfred Tecnologia"; a empresa como responsável na privacidade | Identificação, em outro regime | Não |

**INTERPRETAÇÃO.** O art. 13 da Lei nº 9.610/1998 considera autor, "não havendo prova em contrário", quem for indicado como tal na utilização. "Modificado por" não transfere direito nenhum e atende ao aviso de modificação da seção 5(a) da AGPL-3.0, que recai sobre quem transmite o programa.

**RISCO.** Baixo nesses textos. O ponto do `AGENTS-MT.md` é de exatidão: é um arquivo público que afirma como já feito algo que depende de contrato.

## 4. O que esta verificação não cobriu

- Busca feita só nos arquivos da tabela, em `flutter/lib/mt`, `docs/marca`, `README-MT.md`, `docs/publicacao.md` e `ferramentas-mt`, pelas palavras de titularidade. Os documentos antigos de `docs/superpowers/` e `docs/legal/` e as imagens não foram lidos com esse olhar.
- A minuta da cessão não foi lida, porque não está neste repositório.
- O enquadramento do suporte pago e o efeito tributário da cessão ficam fora.

## 5. Requisitos

- [x] Ajustar a linha 17 do `AGENTS-MT.md` antes da tag, com o ok do Manfred. Nota de 05/11/2026: ajustada no PR 11, e o ok vem com a junção dele.
- [ ] Assinar a cessão antes de qualquer venda.
- [ ] Decidir se o autor assina, antes dela, uma autorização curta à MT para distribuir as mudanças sob a AGPL-3.0, com o texto pela `legal-br`.
- [ ] Conferir se a minuta cobre as mudanças já feitas, as versões já publicadas, os textos e os logotipos, e se diz se a cessão é gratuita ou paga.
- [ ] Depois da assinatura, decidir se entra o aviso de copyright da MT sobre as mudanças, como pede o `AGENTS-MT.md`.

## 6. Pendência de validação para o advogado

Esta pergunta está em `CONSULTA-ADVOGADO-complemento-2026-11-02.md`, questão 9.

**Pergunta.** Sem contrato específico, o art. 4º da Lei nº 9.609/1998 alcança as mudanças feitas por quem é sócio ou administrador da MT? Leituras possíveis: (a) não alcança, e os direitos ficam com a pessoa física até a cessão; (b) alcança, se houver vínculo de serviço com esse objeto, e a cessão só confirma a situação. Impacto: define quem assina o quê e como a minuta descreve as mudanças já feitas. Urgência: antes da primeira venda.
