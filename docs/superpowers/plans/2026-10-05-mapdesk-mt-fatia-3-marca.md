# MapDesk-MT, fatia 3 (marca): plano de implementação

> **Para quem executa:** usar `superpowers:subagent-driven-development`, tarefa por tarefa. Os passos usam caixas (`- [ ]`).

**Objetivo:** o executável compilado se chama `MapDesk-MT.exe` e se apresenta como MapDesk-MT em todos os lugares: janela, bandeja, ícones, instalação, propriedades do arquivo e tela Sobre. Usa o tema verde da MT, mostra os avisos da AGPL e não fala com nenhum servidor de API do RustDesk.

**Arquitetura:** a configuração em tempo de execução vai em `src/mt_config.rs`, com uma linha de gancho em `load_custom_client`. A arte fica versionada em `docs/marca/` e gera os ícones e as imagens nos lugares que o RustDesk já lê. O nome do executável é trocado no workflow da MT, depois da compilação, sem mexer no `CMakeLists.txt`, no `build.py` nem no `generate.py`. As edições em arquivos do RustDesk são pequenas e pontuais.

**Spec:** `docs/superpowers/specs/2026-10-05-mapdesk-mt-versao-1-design.md` (seções 4, 6 e 9). Levantamento do código: `.superpowers/rascunho/levantamento-fatias-2-3.md`.

## Decisões desta fatia (05/10/2026)

1. A fatia 3 vem antes da 2. A chave do laboratório ainda não chegou, então o `mt_config.rs` nasce aqui **sem** servidor nem chave. A fatia 2 acrescenta só essas duas linhas (e `hide-server-settings`).
2. O símbolo é provisório (monitor com contorno `#006B2D` e cursor `#43A92C`), aprovado pelo Manfred como base. A arte final substitui os arquivos de `docs/marca/`, e o roteiro gera tudo de novo.
3. O link de privacidade fica escondido até a página do site-mt existir. Inventar um endereço está proibido. A pendência fica registrada.
4. O copyright da MT não entra (só depois de o Manfred confirmar). O copyright do RustDesk fica.
5. A versão MT (`1.5.0-mt.1`) é uma constante em Dart, usada na tela Sobre e no link do código. Ela sobe junto com a tag, e a regra fica escrita no `README-MT.md`.

## Restrições globais

- Pasta: só `C:\COWORK\CODE\MAPDESK-MT`. Rascunhos em `.superpowers/rascunho/`. Nunca `find /`.
- Autor: Manfred Heil Junior. Nenhum crédito a IA; nunca `Co-Authored-By`. Toda mensagem de commit termina com `Autor: Manfred Heil Junior`, tem título com verbo na 3ª pessoa sem acento e corpo com o porquê, em arquivo `.superpowers/rascunho/msg-*.txt` e `git commit -F`.
- Antes de cada commit: `sh .superpowers/rascunho/portoes.sh <arquivo-da-mensagem>` precisa terminar com `PORTOES OK`.
- Nunca `--amend`, `rebase`, `reset`, `push --force`. O gancho envia cada commit ao GitHub.
- Textos em português sem travessão longo ou médio, aspas curvas, reticências de um caractere, setas, NBSP. Texto de tela passa pela `humanizar-ptbr`.
- Regras de código do `AGENTS.md` do RustDesk: diff mínimo, sem refatorar, sem `unwrap()` fora de trava ou teste, `use` agrupado por crate, comentário só para o porquê.
- Ramo: `marca`, a partir de `mt`.
- Nome do programa: `MapDesk-MT` (APP_NAME, executável, pasta, serviço). Nome exibido em texto corrido: "MapDesk-MT". Logotipo: "MapDesk - MT".
- Cores: `#006B2D` (principal escuro), `#0F8F2F`, `#43A92C` (destaque), `#9AD52B`; texto `#202020`.
- "RustDesk" não aparece no nome, no ícone, no executável, no serviço nem no instalador. A origem aparece só na tela Sobre e nos avisos legais.

---

### Tarefa 1: `src/mt_config.rs` (nome e padrões)

**Arquivos:** criar `src/mt_config.rs`; alterar `src/lib.rs` (uma linha `mod mt_config;` perto de `mod custom_server;`, linha 46) e `src/common.rs` (`load_custom_client`, linha 2360: primeira linha do corpo `crate::mt_config::aplicar();`, antes do `#[cfg(debug_assertions)]`); alterar `.github/workflows/mapdesk-windows.yml` (passo de teste).

**Produz:** `pub fn aplicar()` idempotente (a interface gráfica chama `load_custom_client` duas vezes).

Comportamento de `aplicar()`:

| Tabela (`hbb_common::config`) | Chave | Valor |
|---|---|---|
| `APP_NAME` | | `MapDesk-MT` |
| `DEFAULT_SETTINGS` | `approve-mode` | `click` |
| `OVERWRITE_SETTINGS` | `allow-auto-update` | `N` |
| `BUILTIN_SETTINGS` | `register-device` | `N` |
| `BUILTIN_SETTINGS` | `hide-powered-by-me` | `Y` |

Escrever como o `read_custom_client` faz (`src/common.rs`, perto das linhas 2397 a 2416 e 2478): `.write().unwrap().insert(k.to_owned(), v.to_owned())`. Usar as constantes de `base::config::keys` quando existirem (`OPTION_APPROVE_MODE`, `OPTION_ALLOW_AUTO_UPDATE`, `OPTION_REGISTER_DEVICE`, `OPTION_HIDE_POWERED_BY_ME`). Conferir em `libs/base/src/config/keys.rs` qual caminho de import o resto de `src/` usa.

O `custom.txt` assinado continua lido depois de `aplicar()`, sem mudança. Ninguém além da RustDesk consegue assiná-lo.

- [ ] **Passo 1: teste primeiro** (`#[cfg(test)] mod tests` dentro de `src/mt_config.rs`): chama `aplicar()` duas vezes e confere:
  - `APP_NAME` igual a "MapDesk-MT";
  - `password_security::approve_mode() == ApproveMode::Click` (ou a leitura direta de `DEFAULT_SETTINGS`);
  - `Config::no_register_device()` verdadeiro;
  - `crate::common::get_api_server(String::new(), String::new())` vazio;
  - `allow-auto-update` em `OVERWRITE_SETTINGS` igual a "N".

  Ao final, devolver `APP_NAME` para "RustDesk" e remover as chaves inseridas, para não contaminar outros testes.
- [ ] **Passo 2: implementação mínima** e gancho.
- [ ] **Passo 3: CI roda o teste.** No `mapdesk-windows.yml`, depois de "Upload executable" e antes de "Publish release", acrescentar um passo `Test mt_config` que roda `cargo test --lib --features flutter,hwcodec,vram mt_config`, com `shell: bash`. Antes, conferir no `build.py` quais features o build Windows usa e usar as mesmas, para reaproveitar a compilação. O executável já está no artefato antes do teste.
- [ ] **Passo 4: portões e commit** (`Cria configuracao propria do MapDesk-MT`).

### Tarefa 2: arte e ícones

**Arquivos:**
- Criar: `docs/marca/mapdesk-mt-simbolo.svg`, `docs/marca/mapdesk-mt-logo.svg` (cópias de `.superpowers/rascunho/marca/`), `docs/marca/leia-me.md`, `ferramentas-mt/gerar-marca.py`.
- Substituir: `flutter/windows/runner/resources/app_icon.ico`, `res/icon.ico`, `res/tray-icon.ico`, `flutter/assets/icon.svg`, `libs/portable/src/res/label.png`.
- Criar: `flutter/assets/icon.ico`, `flutter/assets/icon.png`, `flutter/assets/logo.png`.

O `gerar-marca.py` usa o Inkscape (`C:\Program Files\Inkscape\bin\inkscape`) para gerar PNG a partir do SVG, e o Pillow para montar os `.ico`. Os `.ico` saem em DIB de 32 bits com máscara AND, como o `gerar-icone.py` do MapDisk-MT (`C:\COWORK\CODE\MAPDISK-MT\ferramentas\gerar-icone.py`, só leitura). Esse formato evita o bloqueio visto no CronoAula com ícone só PNG.

| Saída | Conteúdo |
|---|---|
| `app_icon.ico`, `res/icon.ico`, `flutter/assets/icon.ico` | 16, 24, 32, 48, 64, 128, 256 |
| `res/tray-icon.ico` | 16, 20, 24, 32, 40, 48 |
| `flutter/assets/icon.png` | 256x256 |
| `flutter/assets/icon.svg` | o símbolo |
| `flutter/assets/logo.png` | logo horizontal com 60 px de altura útil e fundo transparente (o `loadLogo` limita a 300x60) |
| `libs/portable/src/res/label.png` | 96x32, símbolo e "MapDesk-MT", como o original |

A fonte do logo é Montserrat 700. Sem ela instalada, o Inkscape cai para Arial. Ainda assim, gerar e registrar no `leia-me.md` que a arte final deve vir em curvas.

- [ ] Passo 1: roteiro e geração.
- [ ] Passo 2: conferir as imagens geradas (abrir os PNG; os `.ico` com Pillow listando os tamanhos).
- [ ] Passo 3: portões e commit (`Traz a marca do MapDesk-MT para icones e imagens`).

### Tarefa 3: executável e metadados

**Arquivos:** alterar `flutter/windows/runner/Runner.rc` e `.github/workflows/mapdesk-windows.yml`.

- `Runner.rc`, bloco `StringFileInfo`:
  - `CompanyName`: "MT - Manfred Tecnologia";
  - `FileDescription`: "MapDesk-MT, acesso remoto";
  - `InternalName`: "MapDesk-MT";
  - `OriginalFilename`: "MapDesk-MT.exe";
  - `ProductName`: "MapDesk-MT";
  - `LegalCopyright`: mantém o do RustDesk e acrescenta " Modificado por MT - Manfred Tecnologia. AGPL-3.0." (sem copyright da MT).
- Workflow, passo "Build rustdesk", logo depois do `mv ./flutter/build/... ./rustdesk`: `Rename-Item ./rustdesk/rustdesk.exe MapDesk-MT.exe`. A DLL `librustdesk.dll` não muda: o `main.cpp` a carrega por esse nome.
- Workflow, passo "Build self-extracted executable":
  - `-e ../../rustdesk/MapDesk-MT.exe`;
  - saída `./SaidaMT/MapDesk-MT.exe`, para o técnico mandar ao cliente;
  - o artefato e a release passam a levar `MapDesk-MT.exe`.
  - Conferir em `libs/portable/src/main.rs` (linhas 270 a 300) e em `libs/portable/generate.py` que o nome do executável interno é lido de `-e` e não está fixo como `rustdesk.exe`. Se estiver fixo em algum lugar, parar e reportar NEEDS_CONTEXT.
- [ ] Passos: editar, portões, commit (`Renomeia o executavel e os metadados para MapDesk-MT`).

### Tarefa 4: tema verde e textos fixos

**Arquivos:** `flutter/lib/common.dart`, `flutter/lib/desktop/widgets/tabbar_widget.dart`, `src/auth_2fa.rs` e os três pontos de cor solta apontados no levantamento (`common.dart:1324`, `desktop_setting_page.dart:2572`, `server_page.dart:466`).

- `MyTheme` (`common.dart`, linhas 248 a 262):
  - `accent` = `0xFF0F8F2F`;
  - `accent50` = `0x770F8F2F`;
  - `accent80` = `0xAA0F8F2F`;
  - `button` = `0xFF0F8F2F`;
  - `idColor` = `0xFF43A92C`.
- `ColorScheme` com `Colors.blue` (`common.dart`, perto das linhas 454 e 562): trocar o azul pelo verde `0xFF0F8F2F`, com o menor diff possível.
- Cores soltas `0xFF2c8cff` e equivalentes: trocar por `MyTheme.button` ou pelo mesmo verde.
- `tabbar_widget.dart:644`: o texto fixo "RustDesk" passa a ser o nome do app, pela mesma fonte que o resto do Flutter usa (procurar `bind.mainGetAppNameSync()` ou equivalente; não criar função nova no Rust).
- `src/auth_2fa.rs:17`: `ISSUER` deixa de ser constante fixa. Usar o `APP_NAME` em tempo de execução, com a menor mudança possível. Se mudar a assinatura de algo compartilhado, parar e reportar.
- [ ] Passos: editar, portões, commit (`Aplica o tema verde da MT e o nome nos textos fixos`).

### Tarefa 5: tela Sobre, aviso de modificação e README

**Arquivos:**
- Criar: `flutter/lib/mt/mt_info.dart` (constantes) e `AVISO-DE-MODIFICACAO.md`.
- Alterar: `flutter/lib/desktop/pages/desktop_setting_page.dart` (seção About, linhas 2525 a 2590), `README-MT.md` e `docs/superpowers/pendencias.md`.

`mt_info.dart`:

```dart
const String kMtVersao = '1.5.0-mt.1';
const String kMtVersaoBase = '1.5.0';
const String kMtCodigoFonte = 'https://github.com/manfredjr/mapdesk-mt/tree/$kMtVersao';
const String kMtLicenca = 'https://www.gnu.org/licenses/agpl-3.0.html';
const String kMtSite = 'https://manfred.com.br';
const String kMtPrivacidade = '';
```

Tela Sobre (manter a estrutura do card; trocar só o conteúdo):
- título: continua `translate('About RustDesk')`, que o `lang.rs` já transforma em "Sobre o MapDesk-MT";
- versão: `MapDesk-MT $kMtVersao (base RustDesk $kMtVersaoBase)`, e depois data de compilação, impressão digital e ID, como hoje;
- link "Política de privacidade": só aparece se `kMtPrivacidade` não for vazio;
- link "Site": `kMtSite`;
- link "Código-fonte desta versão": `kMtCodigoFonte`;
- link "Licença AGPL-3.0": `kMtLicenca`;
- faixa colorida: troca o azul `0xFF2c8cff` pelo verde `0xFF006B2D`. Mantém `Copyright © <ano> Purslane Tech Pte. Ltd.` e `$license`. O `Slogan_tip` sai, e no lugar dele entra o texto abaixo, em branco.

Texto da faixa (passa pela `humanizar-ptbr` antes):

```text
Baseado no RustDesk, software livre distribuído sob a AGPL-3.0. Não é produto oficial do RustDesk.
Versão modificada pela MT - Manfred Tecnologia. Este programa é distribuído sem nenhuma garantia. Você pode redistribuí-lo e modificá-lo nos termos da AGPL-3.0.
```

`AVISO-DE-MODIFICACAO.md`: diz que é obra derivada do RustDesk (`rustdesk/rustdesk`, tag `1.5.0`, AGPL-3.0) e tem a tabela das mudanças da MT (data 05/10/2026, item, arquivos). A licença não dá direito de uso dos nomes "MapDesk-MT" e "MT - Manfred Tecnologia" nem dos logotipos da MT (AGPL-3.0, seção 7). O `LICENCE` continua valendo.

`README-MT.md`: fatia 1 "feita, PR #1"; fatia 3 "em andamento". Novo item: "A versão MT fica em `flutter/lib/mt/mt_info.dart` (`kMtVersao`) e sobe junto com a tag".

`pendencias.md`, linhas novas:
- endereço da política de privacidade (`kMtPrivacidade` vazio, link escondido);
- arte final do símbolo e do logo em curvas;
- teste do 2FA com o nome novo.

- [ ] Passos: editar, `humanizar-ptbr` nos textos, portões, commit (`Cria tela Sobre e aviso de modificacao do MapDesk-MT`).

### Tarefa 6: PR, CI e executável

- [ ] Corpo do PR em `.superpowers/rascunho/pr-fatia-3.md` ("O que muda", "Como testar", linha de autor), passando pela `humanizar-ptbr`.

  "Como testar":
  1. baixar `MapDesk-MT.exe` do artefato;
  2. abrir e conferir janela, ícone, bandeja, tela Sobre e cores;
  3. clicar em "Instalar" e conferir `C:\Program Files\MapDesk-MT`, o serviço `MapDesk-MT` e o atalho;
  4. conferir que o RustDesk oficial, se instalado, continua funcionando (teste 4 da spec);
  5. aviso: ainda conecta pelos servidores públicos do RustDesk até a fatia 2.
- [ ] `gh pr create -R manfredjr/mapdesk-mt --base mt --head marca --title "Fatia 3: marca do MapDesk-MT" --body-file ...`
- [ ] Ler o CI com `gh pr checks`. Falha: `gh run view --log-failed`, depurar com `superpowers:systematic-debugging` e corrigir em commit novo.
- [ ] Baixar o artefato para `.superpowers/rascunho/artefato-fatia-3/` e conferir o SHA-256 com o log.
- [ ] Conferir a lista de workflows ativos (só os três da MT).
- [ ] Merge só com a frase do Manfred.
