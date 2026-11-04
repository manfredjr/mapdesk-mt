# Publicação do MapDesk-MT

Passo a passo para publicar uma versão (fatia 5 e todas as seguintes). Publicar distribui o programa a clientes: cada publicação precisa do "pode publicar" do Manfred.

## Antes de publicar

1. Pendências que bloqueiam a primeira publicação (`docs/superpowers/pendencias.md`): as do portão da seção "Site do produto", abaixo.

   Decisões do Manfred em 02/11/2026:
   - a primeira versão sai sem esperar as respostas do advogado, com o risco assumido por ele e a consulta (`docs/legal/CONSULTA-ADVOGADO-mapdesk-agpl-marca-2026-10-05.md`) enviada em paralelo. As questões continuam abertas nas pendências;
   - a cessão do autor para a MT não bloqueia a tag, porque o programa é gratuito, e bloqueia a primeira venda. O contrato está com o grupo do contrato único e depende do contador (`docs/legal/verificacao-publicacao-sem-cessao-2026-11-02.md`).
2. A chave pública de **produção** (VPS-MT, `docs/instalacao.md`, passo G4) está em `CHAVE_PUBLICA` (`src/mt_config.rs`). Feito em 01/11/2026, quando a VPS da HostGator passou a responder por `rustdesk.manfred.com.br`; o teste `mt_config` do workflow confere o valor exato antes de empacotar. A do laboratório nunca vai para a versão distribuída.
3. Certificado de assinatura: a primeira versão sai sem certificado, por decisão do Manfred em 01/11/2026, registrada aqui em 02/11/2026. Depois que houver certificado, conferir antes de cada versão se ele está válido e se os segredos do GitHub existem (fatia 4).
4. A versão MT foi atualizada em dois lugares, com o mesmo valor:
   - `kMtVersao` em `flutter/lib/mt/mt_info.dart` (por exemplo `1.5.0-mt.1`);
   - a linha nova na tabela do `AVISO-DE-MODIFICACAO.md`, com a data da publicação.
5. O ramo `mt` está com o CI verde, e o Manfred testou o executável do último PR:
   - testes 1 a 7 da spec;
   - o teste de rede (`ferramentas-mt/teste-rede.ps1`), que precisa dar "OK".

## Publicar

1. Criar a tag no commit testado do `mt`, com o mesmo valor de `kMtVersao`:

   ```bash
   git tag 1.5.0-mt.1
   ```

   ```bash
   git push origin 1.5.0-mt.1
   ```

2. O workflow `MapDesk-MT Windows x64` roda pela tag e cria a versão (release) com o `MapDesk-MT.exe` e o link do código-fonte da tag.
3. Conferir na página da versão:
   - o executável está lá;
   - o link do código abre a árvore da tag;
   - o SHA-256 do log bate com o do arquivo baixado.
4. Só depois do certificado: baixar o executável da versão e conferir a assinatura (Propriedades e depois Assinaturas digitais).

## Depois de publicar

1. Publicar ou atualizar a página do produto (seção "Site do produto", abaixo), antes de divulgar a versão.
   - Depois da conferência no ar e com a confirmação do Manfred ("Site do produto", passo 7), pedir à sessão do site a troca em `manfred.com.br/acesso`: o MapDesk-MT vira o botão principal e o RustDesk oficial fica como alternativa. A decisão é do Manfred, em 02/11/2026, e substitui o "os dois caminhos não se misturam" de 01/11/2026.
2. Atualizar a "Situação do projeto" do `README-MT.md`.
3. Nunca apagar tags nem versões antigas que algum cliente recebeu (AGPL-3.0, seção 6).

## Site do produto

A página `https://mapdesk.manfred.com.br/` mora em `public/` deste repositório (spec `2026-11-01-mapdesk-site-produto-design.md`, seção 8). Cada passo só sai com a frase do Manfred.

1. Portão antes da tag. O Manfred confirma, ou adia por escrito:
   - cessão do autor para a MT, adiada pelo Manfred em 02/11/2026: não bloqueia a tag, mas precisa estar assinada antes de qualquer venda;
   - respostas do advogado (pendências jurídicas 1 a 6), adiadas pelo Manfred em 02/11/2026 para a primeira versão, conforme a seção "Antes de publicar";
   - texto completo da `privacidade.html` no ramo `mt`, com os itens da verificação de privacidade (seção 5), e o endereço gravado em `kMtPrivacidade`. A página entra no ar no passo 4, antes de a versão ser divulgada;
   - bloco do MapDesk-MT no `README.md` da raiz;
   - licenças dos binários (`docs/legal/licencas-binarios-terceiros-2026-11-02.md`): a conferência não fechou. Cada item abaixo precisa estar resolvido ou adiado pelo Manfred por escrito:
     - decisão sobre como avisar o cliente do anúncio do `usbmmidd_v2`. O teste de 04/11/2026, com o monitor virtual ativo, não mostrou anúncio;
     - arquivo de avisos de terceiros;
     - instruções do código do FFmpeg nas notas da versão;
     - perguntas com urgência "antes da primeira tag" em `docs/legal/CONSULTA-ADVOGADO-complemento-2026-11-02.md`, que as decisões de 02/11/2026 e 04/11/2026 não cobrem. A questão 6, do `hwcodec` e do `hbb_common`, está coberta: o Manfred assumiu a dúvida em 04/11/2026;
   - ajuste da linha 17 do `AGENTS-MT.md` e ressalva de terceiros nas linhas 21, 25 e 27, com o ok do Manfred;
   - teste de convivência com o RustDesk oficial na mesma máquina, inclusive a desinstalação do MapDesk-MT;
   - promessas da página sobre o servidor conferidas: IP da máquina no painel, servidor no Brasil, registro de cada conexão, guarda por 6 meses e acesso restrito;
   - verificação do provedor, inclusive o acesso do suporte a partir do exterior registrado no VPS-MT;
   - buscas no INPI: o Manfred confirma se ficam para depois, porque a decisão de 02/11/2026 registra só as respostas do advogado.
2. Merge do PR do site, com o workflow `MapDesk-MT site` verde.
3. Tag com o valor de `kMtVersao` (seção "Publicar", acima). O botão da página aponta para essa tag, e a versão traz o `MapDesk-MT.exe` e o `MapDesk-MT.exe.sha256`. A tag vem antes do site para o botão nunca apontar para uma versão que não existe. Até o fim do passo 6, a versão não é divulgada a ninguém, porque o link de privacidade do programa só funciona depois do passo 4.
4. No cPanel da GoDaddy, pelo `roteiro-publicacao-git-cpanel.md`:
   - clonar `https://github.com/manfredjr/mapdesk-mt.git` em `repositories/mapdesk-mt`, sem chave SSH, porque o repositório é público;
   - apontar o subdomínio `mapdesk.manfred.com.br` para a pasta `public` do clone;
   - rodar "Update from Remote" e depois "Deploy HEAD Commit".
5. No Cloudflare: bloqueio de robôs de IA no subdomínio.
6. Conferência no ar:
   - a página abre em HTTPS;
   - o botão baixa o arquivo certo, e o SHA-256 confere com o `MapDesk-MT.exe.sha256`;
   - nenhum script de terceiros carrega;
   - a tela Sobre do executável abre a página de privacidade.
7. Só agora a versão é divulgada e a sessão do site troca o `manfred.com.br/acesso`, se o Manfred tiver confirmado o botão principal (`docs/superpowers/pendencias.md`).

A cada versão nova, `kMtVersao` muda e o teste da página exige os links com a tag nova: atualizar o `public/index.html` no mesmo PR.

## Versão nova do RustDesk

Ver a spec, seção 11:
- merge da tag nova do oficial em PR;
- conferir a lista de workflows ativos e desligar os do oficial;
- passar pelos testes;
- nova tag `<versão>-mt.<n>`.
