# Publicação do MapDesk-MT

Passo a passo para publicar uma versão (fatia 5 e todas as seguintes). Publicar distribui o programa a clientes: cada publicação precisa do "pode publicar" do Manfred.

## Antes de publicar

1. Pendências que bloqueiam a primeira publicação (`docs/superpowers/pendencias.md`):
   - respostas do advogado às questões 1, 3 e 4 da consulta (`docs/legal/CONSULTA-ADVOGADO-mapdesk-agpl-marca-2026-10-05.md`);
   - aviso de privacidade publicado no site da MT e o endereço gravado em `kMtPrivacidade` (`flutter/lib/mt/mt_info.dart`);
   - cessão do autor para a MT assinada.
2. A chave pública de **produção** (VPS-MT, `docs/instalacao.md`, passo G4) está em `CHAVE_PUBLICA` (`src/mt_config.rs`). A do laboratório nunca vai para a versão distribuída.
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

1. Avisar a sessão do site-mt para trocar, na página de download, o RustDesk oficial renomeado pelo `MapDesk-MT.exe` da versão. A página mantém o aviso de privacidade, a licença e o link do código.
2. Atualizar a "Situação do projeto" do `README-MT.md`.
3. Nunca apagar tags nem versões antigas que algum cliente recebeu (AGPL-3.0, seção 6).

## Versão nova do RustDesk

Ver a spec, seção 11:
- merge da tag nova do oficial em PR;
- conferir a lista de workflows ativos e desligar os do oficial;
- passar pelos testes;
- nova tag `<versão>-mt.<n>`.
