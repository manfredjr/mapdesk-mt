# Consulta ao advogado: MapDesk (licença, marca e privacidade)

Data: 05/10/2026. Consulente: MANFRED TECNOLOGIA LTDA (MT - Manfred Tecnologia), CNPJ 21.075.901/0001-12.

Situação: não enviada. O envio depende de decisão do Manfred.

## Contexto mínimo

A MT vai distribuir, de graça, aos clientes do seu suporte remoto (empresas e pessoas físicas, cerca de 150 a 200 máquinas Windows), o "MapDesk": versão modificada do RustDesk 1.5.0, programa de acesso remoto de código aberto sob a licença GNU AGPL-3.0, cujo copyright é exibido em nome da Purslane Tech Pte. Ltd. (Singapura). A MT troca o nome exibido, os ícones e as cores, embute o próprio servidor e a própria chave, desliga funções que enviariam dados à RustDesk e deixa a aprovação por clique como padrão. O executável é publicado num repositório público do GitHub com o código-fonte de cada versão e oferecido na página de download do site da MT.

Análises que sustentam as perguntas, no repositório do projeto:

- `docs/legal/verificacao-licenca-agpl-e-marcas-2026-10-05.md`
- `docs/legal/verificacao-privacidade-cliente-2026-10-05.md`
- `C:\COWORK\CODE\VPS-MT\docs\legal\verificacao-servidor-rustdesk-2026-10-04.md` (servidor)

O projeto tem 6 pendências. Esta consulta trata as pendências 3 a 6, nas questões 1 a 4. As pendências 1 (registro de "RustDesk" no INPI) e 2 (busca de "MapDesk" por radical no INPI) são buscas que o Manfred faz no INPI e não vêm para cá, salvo se acharem algo.

## Questão 1 (pendência 3): troca do nome e LPI, art. 195, VI

**Pergunta.** A MT pode exibir o programa como "MapDesk", sem o nome "RustDesk" na interface, mantendo o aviso "Copyright © [ano] Purslane Tech Pte. Ltd." e a frase "Baseado no RustDesk, software livre distribuído sob a licença AGPL-3.0; não é produto oficial do RustDesk", sem incidir na Lei nº 9.279/1996, art. 195, VI? Responder sim ou não e, se não, o que muda.

**O que já foi apurado.**

- LPI, art. 195, VI (Planalto, consultado em 05/10/2026): comete crime de concorrência desleal quem "substitui, pelo seu próprio nome ou razão social, em produto de outrem, o nome ou razão social deste, sem o seu consentimento;".
- AGPL-3.0, seção 5 (https://www.gnu.org/licenses/agpl-3.0.txt, 05/10/2026), autoriza transmitir "a work based on the Program", com aviso de modificação e data (5a) e aviso da licença (5b).
- Não foi encontrada política de marca do RustDesk (repositório, README, termos do site). Os termos do rustdesk.com (vigência 16/09/2026) excluem o cliente e o Server OSS da definição de "Software" e dizem que o cliente customizado do produto pago não leva "any right to use Company's name or logos".
- Lei nº 9.609/1998, art. 2º, § 1º: o autor de programa conserva o direito de "reivindicar a paternidade".

**Interpretações.**

1. A licença autoriza a modificação, inclusive do nome exibido. O produto passa a ser obra derivada distribuída pela MT, a origem é declarada e o copyright é mantido. Não há substituição "sem consentimento". Risco: baixo, se o texto de origem estiver sempre visível.
2. O consentimento do inciso VI seria específico para nome e marca, e a licença de direito autoral não o supre. Nesse caso, a MT teria de manter "RustDesk" visível de outra forma, ou pedir autorização. Risco: usar o nome "RustDesk" de forma mais destacada aumenta o risco de confusão do art. 195, IV, e de violar o que o titular declara nos termos.

**Impacto prático.** Define o texto da tela "Sobre", do instalador e da página de download, e se é preciso escrever à Purslane Tech.

**Urgência.** Antes da primeira versão distribuída a clientes.

## Questão 2 (pendência 4): licença do `hbb_common`

**Pergunta.** Se a MT alterar arquivos do submódulo `rustdesk/hbb_common` e publicar essas alterações num fork público, ela tem licença para isso, considerando que o repositório não declara licença mas é distribuído como parte do RustDesk sob a AGPL-3.0? Responder sim ou não e, se não, o caminho.

**O que já foi apurado.**

- Em 05/10/2026, o repositório `rustdesk/hbb_common` (commit `229b904508364c8997aad0fb5af57effac859f60`) não tem arquivo de licença; a API do GitHub informa licença nula; o `Cargo.toml` não tem campo de licença e indica `authors = ["open-trade <info@opentradesolutions.com>"]`.
- O RustDesk, que inclui o `hbb_common` como submódulo, está sob a AGPL-3.0. A seção 5(c) diz que a licença se aplica "to the whole of the work, and all its parts, regardless of how they are packaged".
- Existe caminho técnico que evita alterar o `hbb_common` (configuração em tempo de execução no repositório principal).

**Interpretações.**

1. O `hbb_common` faz parte da obra licenciada sob a AGPL-3.0, e quem recebe o RustDesk recebe todas as partes sob essa licença. Alterar e publicar é permitido. Risco: baixo.
2. O repositório isolado, sem licença declarada, não estaria licenciado fora do contexto do RustDesk, e o fork alterado e separado precisaria de base própria. Risco: médio, se a MT publicar o fork alterado como repositório independente.

**Impacto prático.** Decide se a MT pode alterar o `hbb_common` ou se deve usar só a configuração em tempo de execução.

**Urgência.** Só se o desenho técnico exigir alterar o `hbb_common`. Se não exigir, a questão pode ser arquivada.

## Questão 3 (pendência 5): Marco Civil, art. 7º, IX

**Pergunta.** Para registrar ID, IP e horário das máquinas dos clientes no servidor da MT, com base na execução do contrato (LGPD, art. 7º, V) ou em outra base que não o consentimento, a MT precisa também colher o "consentimento expresso" do Marco Civil, art. 7º, IX? Responder sim ou não.

**O que já foi apurado.**

- Marco Civil, art. 7º, IX (Planalto, 05/10/2026): "consentimento expresso sobre coleta, uso, armazenamento e tratamento de dados pessoais, que deverá ocorrer de forma destacada das demais cláusulas contratuais;".
- LGPD, art. 7º (Planalto, 05/10/2026): o consentimento é uma das hipóteses (inciso I), ao lado de obrigação legal (II), execução de contrato (V), legítimo interesse (IX) e outras.
- A verificação do servidor no VPS-MT (04/10/2026) não tratou do art. 7º, IX.

**Interpretações.**

1. A LGPD, posterior e específica, rege as bases legais. O art. 7º, IX, só se aplica quando o consentimento for a base escolhida. Basta o aviso claro do art. 7º, VIII, do Marco Civil e do art. 9º da LGPD. Risco: baixo, se o aviso for completo.
2. O art. 7º, IX, convive com a LGPD e exige consentimento destacado em toda coleta por aplicação de internet. A MT teria de pôr um aceite destacado na página de download ou na primeira execução. Risco: consentimento sem necessidade cria a expectativa de que, retirado, o tratamento para, e o suporte não funciona sem os registros.

**Impacto prático.** Decide se o MapDesk ou a página de download precisam de caixa de aceite antes do primeiro uso.

**Urgência.** Antes de publicar a página de download com o MapDesk.

## Questão 4 (pendência 6): papel da MT na sessão de suporte

**Pergunta.** No suporte remoto a cliente empresa, em que o técnico da MT vê e controla, com aceite por clique, a tela de máquinas usadas por empregados do cliente, a MT é operadora (LGPD, art. 5º, VII) quanto ao que aparece na tela? Qual base legal cobre os empregados, e quais cláusulas mínimas o contrato de suporte precisa ter?

**O que já foi apurado.**

- LGPD, art. 5º, VI e VII, e art. 39 (Planalto, 05/10/2026): o operador trata "em nome do controlador" e "segundo as instruções fornecidas pelo controlador".
- A verificação do VPS-MT (item 3.1) já registrou que o empregado não é parte do contrato de suporte, de modo que o art. 7º, V, não o alcança, e que a MT tende a ser operadora na sessão (item 3.5). Para os registros do servidor, a MT é controladora.
- Hoje o contrato de suporte com clientes empresa não tem forma escrita com cláusula de dados.
- A tela pode mostrar dados de terceiros e, por acaso, dados sensíveis (LGPD, art. 5º, II).

**Interpretações.**

1. MT operadora na sessão; a base legal é a do cliente empresa, controlador. Exige contrato com instruções de tratamento, confidencialidade, segurança e aviso de incidente. Risco: baixo com contrato; médio sem contrato escrito.
2. MT controladora em conjunto, por definir meios relevantes (programa, servidor, guarda). Base própria, provavelmente legítimo interesse (art. 7º, IX), com avaliação documentada. Risco: obrigações de controlador também sobre o conteúdo da sessão.

**Impacto prático.** Define o texto do aviso de privacidade na parte de cliente empresa e a minuta da cláusula de dados do contrato de suporte.

**Urgência.** Antes de atender clientes empresa com o MapDesk. Enquanto isso, a MT segue com o modelo atual de suporte.

## Resumo

| Questão | Pendência | Tema | Urgência |
|---|---|---|---|
| 1 | 3 | Troca do nome e LPI, art. 195, VI | Antes da primeira versão |
| 2 | 4 | Licença do `hbb_common` | Só se for alterar o `hbb_common` |
| 3 | 5 | Marco Civil, art. 7º, IX | Antes da página de download |
| 4 | 6 | Papel da MT na sessão e contrato | Antes de atender empresas com o MapDesk |
