# Publicação do MapDesk-MT

Passo a passo para publicar uma versão (fatia 5 e todas as seguintes). Publicar distribui o programa a clientes: cada publicação precisa do "pode publicar" do Manfred.

## Antes de publicar

1. Pendências que bloqueiam a primeira publicação (`docs/superpowers/pendencias.md`):
   - respostas do advogado às questões 1, 3 e 4 da consulta (`docs/legal/CONSULTA-ADVOGADO-mapdesk-agpl-marca-2026-10-05.md`);
   - aviso de privacidade publicado no site da MT e o endereço gravado em `kMtPrivacidade` (`flutter/lib/mt/mt_info.dart`);
   - cessão do autor para a MT assinada.
2. A chave pública de **produção** (VPS-MT, `docs/instalacao.md`, passo G4) está em `CHAVE_PUBLICA` (`src/mt_config.rs`). Feito em 01/11/2026, quando a VPS da HostGator passou a responder por `rustdesk.manfred.com.br`; o teste `mt_config` do workflow confere o valor exato antes de empacotar. A do laboratório nunca vai para a versão distribuída.
3. O certificado de assinatura está válido, e os segredos do GitHub existem (fatia 4).
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
4. Baixar o executável da versão e conferir a assinatura (Propriedades e depois Assinaturas digitais).

## Depois de publicar

1. Publicar ou atualizar a página do produto (seção "Site do produto", abaixo). A página `manfred.com.br/acesso`, dos clientes do suporte, continua com o RustDesk oficial: os dois caminhos não se misturam (decisão do Manfred em 01/11/2026).
2. Atualizar a "Situação do projeto" do `README-MT.md`.
3. Nunca apagar tags nem versões antigas que algum cliente recebeu (AGPL-3.0, seção 6).

## Site do produto

A página `https://mapdesk.manfred.com.br/` mora em `public/` deste repositório (spec `2026-11-01-mapdesk-site-produto-design.md`, seção 8). Cada passo só sai com a frase do Manfred.

1. Portão antes da tag. O Manfred confirma, ou adia por escrito:
   - cessão do autor para a MT;
   - respostas do advogado (pendências jurídicas 1 a 6);
   - página de privacidade no ar, que pode ser a `privacidade.html` deste site, gravada também em `kMtPrivacidade` numa fatia própria;
   - bloco do MapDesk-MT no `README.md` da raiz;
   - conferência das licenças dos binários de terceiros do build.
2. Merge do PR do site, com o workflow `MapDesk-MT site` verde.
3. Tag com o valor de `kMtVersao` (seção "Publicar", acima). O botão da página aponta para essa tag, e a versão traz o `MapDesk-MT.exe` e o `MapDesk-MT.exe.sha256`.
4. No cPanel da GoDaddy, pelo `roteiro-publicacao-git-cpanel.md`:
   - clonar `https://github.com/manfredjr/mapdesk-mt.git` em `repositories/mapdesk-mt`, sem chave SSH, porque o repositório é público;
   - apontar o subdomínio `mapdesk.manfred.com.br` para a pasta `public` do clone;
   - rodar "Update from Remote" e depois "Deploy HEAD Commit".
5. No Cloudflare: bloqueio de robôs de IA no subdomínio.
6. Conferência no ar:
   - a página abre em HTTPS;
   - o botão baixa o arquivo certo, e o SHA-256 confere com o `MapDesk-MT.exe.sha256`;
   - nenhum script de terceiros carrega.

A cada versão nova, `kMtVersao` muda e o teste da página exige os links com a tag nova: atualizar o `public/index.html` no mesmo PR.

## Versão nova do RustDesk

Ver a spec, seção 11:
- merge da tag nova do oficial em PR;
- conferir a lista de workflows ativos e desligar os do oficial;
- passar pelos testes;
- nova tag `<versão>-mt.<n>`.
