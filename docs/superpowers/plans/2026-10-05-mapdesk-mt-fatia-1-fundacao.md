# MapDesk-MT, fatia 1 (fundação): plano de implementação

> **Para quem executa:** usar `superpowers:subagent-driven-development` (recomendado) ou `superpowers:executing-plans`, tarefa por tarefa. Os passos usam caixas (`- [ ]`) para acompanhamento.

**Objetivo:** criar os forks e os ramos e trazer as regras e os documentos da MT para o ramo `mt`. Depois, compilar no GitHub Actions o RustDesk 1.5.0 sem nenhuma mudança de código, com o executável Windows x64 publicado como artefato do PR.

**Arquitetura:** `manfredjr/mapdesk-mt` é fork público de `rustdesk/rustdesk`. O ramo `mt` nasce da tag `1.5.0` e é o ramo principal. O submódulo `libs/hbb_common` passa a apontar para `manfredjr/hbb_common`, um fork sem alteração, no mesmo commit. Um workflow da MT, derivado do job `build-for-windows-flutter` do `flutter-build.yml` oficial, compila só o Windows x64.

**Tecnologias:** Git, GitHub CLI (`gh`), GitHub Actions (`windows-2022`), Rust 1.75, Flutter 3.24.5, vcpkg, Python 3 (`build.py` do RustDesk).

**Spec:** `docs/superpowers/specs/2026-10-05-mapdesk-mt-versao-1-design.md`.

## Restrições globais

- Pasta: só `C:\COWORK\CODE\MAPDESK-MT`. Rascunhos em `.superpowers/rascunho/`, ignorada pelo git. Nunca `find /`.
- Autor: Manfred Heil Junior. Nenhum commit, arquivo ou PR credita ferramenta de IA; nunca `Co-Authored-By` nem "Generated with". Toda mensagem de commit termina com a linha `Autor: Manfred Heil Junior`.
- Commit: título com verbo na 3ª pessoa, sem acento; corpo com o porquê. A mensagem vai num arquivo em `.superpowers/rascunho/` e entra com `git commit -F`.
- Nunca `--amend`, `rebase`, `reset` nem `push --force` em commit enviado.
- Textos em português, sem travessão longo ou médio, aspas curvas, reticências de um caractere, setas, sinal de multiplicação ou de menos unicode.
- Base: tag `1.5.0` de `rustdesk/rustdesk`; submódulo `hbb_common` no commit `229b904508364c8997aad0fb5af57effac859f60`.
- Nenhum arquivo do RustDesk muda nesta fatia, salvo `.gitmodules` (URL do submódulo), `.gitignore` (linha `.superpowers/`) e `CLAUDE.md` (uma linha a mais).
- Nenhum segredo no repositório. Esta fatia não usa segredo nenhum.
- Merge do PR só com a frase do Manfred "conferi tudo certo, pode juntar o PR #N".

## Mapa de arquivos

| Arquivo | Situação | Responsabilidade |
|---|---|---|
| `AGENTS-MT.md` | já existe na pasta | Regras da MT |
| `CLAUDE.md` | do RustDesk, alterado | Carrega `@AGENTS-MT.md` e `@AGENTS.md` |
| `README-MT.md` | novo | O que é o MapDesk-MT, como compilar, "Situação do projeto", "Antes de publicar", "Depois de publicar", "A confirmar com" |
| `.gitignore` | do RustDesk, alterado | Ignora `.superpowers/` |
| `.gitmodules` | do RustDesk, alterado | Submódulo aponta para `manfredjr/hbb_common` |
| `.githooks/post-commit` e `.githooks/post-merge` | novos (cópia do UNITASK) | Enviam ao GitHub todo commit e todo merge |
| `.github/workflows/mapdesk-windows.yml` | novo | Compila o Windows x64 em PR para `mt`, em tag `*-mt.*` e por acionamento manual |
| `docs/legal/*`, `docs/superpowers/*` | já existem na pasta | Verificações jurídicas, spec, plano, pendências |
| `.superpowers/rascunho/portoes.sh` | novo, fora do git | Portões antes de cada commit |

O README do RustDesk (`README.md`) fica intacto. A troca dele, se houver, é decidida na fatia 3.

---

### Tarefa 1: Autorização e criação dos forks

**Arquivos:** nenhum.

**Produz:** repositórios `manfredjr/mapdesk-mt` (fork de `rustdesk/rustdesk`) e `manfredjr/hbb_common` (fork de `rustdesk/hbb_common`), públicos, só com o ramo padrão; Actions ligado no `mapdesk-mt` com os workflows do oficial desligados.

- [ ] **Passo 1: Pedir autorização no chat**

Criar repositório pede autorização (`AGENTS-MT.md`, "Autonomia"). Perguntar ao Manfred e esperar a frase exata **pode criar os forks**. Sem essa frase, parar aqui.

- [ ] **Passo 2: Criar os dois forks**

```bash
gh repo fork rustdesk/rustdesk --clone=false --default-branch-only --fork-name mapdesk-mt
gh repo fork rustdesk/hbb_common --clone=false --default-branch-only
```

- [ ] **Passo 3: Conferir os forks**

```bash
gh repo view manfredjr/mapdesk-mt --json isFork,parent,visibility --jq '[.isFork, .parent.owner.login+"/"+.parent.name, .visibility]'
gh repo view manfredjr/hbb_common --json isFork,parent,visibility --jq '[.isFork, .parent.owner.login+"/"+.parent.name, .visibility]'
gh api repos/manfredjr/hbb_common/commits/229b904508364c8997aad0fb5af57effac859f60 --jq .sha
```

Esperado: `[true,"rustdesk/rustdesk","PUBLIC"]`, `[true,"rustdesk/hbb_common","PUBLIC"]` e o SHA `229b904508364c8997aad0fb5af57effac859f60`. Se o último comando der 404, parar e avisar o Manfred: o submódulo não teria de onde vir.

- [ ] **Passo 4: Ligar o Actions e desligar os workflows do oficial**

Os workflows do oficial reagem a PR e tag e não interessam ao fork. `bridge.yml` e `third-party-RustDeskTempTopMostWindow.yml` só rodam quando chamados (`workflow_call`) e ficam ligados, porque o workflow da MT os usa.

```bash
gh api -X PUT repos/manfredjr/mapdesk-mt/actions/permissions -F enabled=true -f allowed_actions=all
for w in ci.yml flutter-ci.yml flutter-build.yml flutter-tag.yml flutter-nightly.yml fdroid.yml playground.yml clear-cache.yml update-webpki-roots.yml; do
  gh workflow disable "$w" -R manfredjr/mapdesk-mt || echo "NAO DESLIGOU: $w"
done
gh workflow list -R manfredjr/mapdesk-mt --all
```

Esperado: nenhuma linha "NAO DESLIGOU"; na lista, esses nove aparecem como `disabled_manually`.

---

### Tarefa 2: Clone local e ramo `mt`

**Arquivos:** a pasta `C:\COWORK\CODE\MAPDESK-MT` vira o repositório git.

**Consome:** os forks da tarefa 1.

**Produz:** remoto `origin` = `manfredjr/mapdesk-mt`, remoto `upstream` = `rustdesk/rustdesk`, ramo `mt` local e no GitHub, apontando para a tag `1.5.0`; `mt` como ramo padrão do repositório.

- [ ] **Passo 1: Iniciar o repositório e configurar a identidade só neste projeto**

```bash
cd /c/COWORK/CODE/MAPDESK-MT
git init
git config user.name "Manfred Heil Junior"
git config user.email "manfred@manfred.com.br"
git remote add origin https://github.com/manfredjr/mapdesk-mt.git
git remote add upstream https://github.com/rustdesk/rustdesk.git
git fetch upstream refs/tags/1.5.0:refs/tags/1.5.0 --no-tags
git fetch origin
```

- [ ] **Passo 2: Tirar da frente o `CLAUDE.md` local**

O RustDesk traz o próprio `CLAUDE.md`. O local tem só a linha `@AGENTS-MT.md`, que volta no passo 4 da tarefa 3. Sem tirá-lo, o `checkout` se recusa a sobrescrever.

```bash
if [ "$(cat CLAUDE.md)" = "@AGENTS-MT.md" ]; then rm CLAUDE.md; else echo "CLAUDE.md diferente do esperado, NADA FEITO"; exit 1; fi
```

- [ ] **Passo 3: Criar o ramo `mt` a partir da tag e conferir que nada local foi sobrescrito**

```bash
git checkout -b mt 1.5.0
git status --short
```

Esperado: `git status` lista como não rastreados só `AGENTS-MT.md`, `docs/legal/`, `docs/superpowers/` e `.superpowers/`. Nenhum arquivo do RustDesk aparece como modificado.

- [ ] **Passo 4: Enviar `mt` e a tag, e tornar `mt` o ramo padrão**

```bash
git push origin mt
git push origin refs/tags/1.5.0
gh repo edit manfredjr/mapdesk-mt --default-branch mt
gh repo view manfredjr/mapdesk-mt --json defaultBranchRef --jq .defaultBranchRef.name
```

Esperado: `mt`.

---

### Tarefa 3: Regras, documentos, ganchos e submódulo (primeiro commit da MT)

**Arquivos:**
- Criar: `README-MT.md`, `.githooks/post-commit`, `.githooks/post-merge`, `.superpowers/rascunho/portoes.sh`, `.superpowers/rascunho/msg-tarefa-3.txt`
- Alterar: `CLAUDE.md`, `.gitignore`, `.gitmodules`
- Incluir no commit: `AGENTS-MT.md`, `docs/legal/`, `docs/superpowers/`

**Consome:** ramo `mt` da tarefa 2.

**Produz:** ramo `fundacao` no GitHub com o primeiro commit da MT; `portoes.sh` usado nas tarefas seguintes.

- [ ] **Passo 1: Ramo da fatia**

```bash
git checkout -b fundacao mt
```

- [ ] **Passo 2: Ganchos copiados do UNITASK e ligados**

```bash
mkdir -p .githooks
cp /c/COWORK/CODE/UNITASK/.githooks/post-commit /c/COWORK/CODE/UNITASK/.githooks/post-merge .githooks/
chmod +x .githooks/post-commit .githooks/post-merge
git config core.hooksPath .githooks
```

- [ ] **Passo 3: `.gitignore` e `.gitmodules`**

```bash
printf '\n# Rascunhos e roteiros da MT, fora do git\n.superpowers/\n' >> .gitignore
git config -f .gitmodules submodule.libs/hbb_common.url https://github.com/manfredjr/hbb_common
cat .gitmodules
git ls-tree mt libs/hbb_common
```

Esperado: a URL é `https://github.com/manfredjr/hbb_common`, e o `ls-tree` mostra o commit `229b904508364c8997aad0fb5af57effac859f60`, que não muda.

- [ ] **Passo 4: `CLAUDE.md` carrega os dois arquivos**

Conteúdo final do `CLAUDE.md`:

```text
@AGENTS-MT.md
@AGENTS.md
```

- [ ] **Passo 5: `README-MT.md`**

Conteúdo (passa pela `humanizar-ptbr` antes do commit):

```markdown
# MapDesk-MT

Versão do cliente RustDesk feita pela MT - Manfred Tecnologia para os clientes do suporte remoto. Baseado no RustDesk, software livre distribuído sob a AGPL-3.0; não é produto oficial do RustDesk.

O código continua sob a AGPL-3.0 (arquivo `LICENCE`). As regras do projeto estão em `AGENTS-MT.md`, e o desenho, em `docs/superpowers/specs/`.

## Ramos

| Ramo | Para que serve |
|---|---|
| `mt` | Ramo principal, com as mudanças da MT. Toda mudança entra por Pull Request |
| `master` | Espelho do RustDesk oficial. Nunca recebe mudança da MT |

## Como compilar

O GitHub Actions compila o Windows x64 pelo workflow `.github/workflows/mapdesk-windows.yml`:

- em todo Pull Request para `mt`, com o executável como artefato do PR;
- em toda tag `<versão>-mt.<n>` (por exemplo `1.5.0-mt.1`), com o executável publicado na versão (release);
- por acionamento manual, na aba Actions.

## Situação do projeto

| Fatia | O quê | Situação |
|---|---|---|
| 1 | Fundação: forks, ramos e compilação do oficial | em andamento |
| 2 | Servidor embutido | a fazer |
| 3 | Marca e avisos | a fazer |
| 4 | Assinatura | a fazer |
| 5 | Publicação | a fazer |

## Antes de publicar

- Buscas no INPI e respostas do advogado (`docs/legal/`).
- Executável assinado (fatia 4).
- Teste de rede: nenhuma conexão a `*.rustdesk.com`.

## Depois de publicar

- Avisar a sessão do site-mt para trocar o executável da página de download.

## A confirmar com

Nada por enquanto.
```

- [ ] **Passo 6: Roteiro de portões**

Criar `.superpowers/rascunho/portoes.sh`:

```bash
#!/bin/sh
# Portoes antes de cada commit do MapDesk-MT. Uso: sh .superpowers/rascunho/portoes.sh <arquivo-da-mensagem>
# Confere so os arquivos preparados (staged) que sao da MT ou foram alterados pela MT.
falhou=0
arquivos=$(git diff --cached --name-only --diff-filter=ACMR)
[ -z "$arquivos" ] && { echo "Nada preparado para commit."; exit 1; }

echo "== Arquivos no commit"; echo "$arquivos"

echo "== Caracteres proibidos nas linhas novas"
if git diff --cached -U0 | grep '^+' | grep -v '^+++' | python -c "
import sys
ruins='\u2013\u2014\u201c\u201d\u2018\u2019\u2026\u00a0\u2192\u00d7\u2212'
achou=[l for l in sys.stdin.read().splitlines() if any(c in l for c in ruins)]
print('\n'.join(achou)); sys.exit(1 if achou else 0)"; then echo "ok"; else echo "FALHOU: caractere proibido"; falhou=1; fi

echo "== Mencao a ferramenta de IA nas linhas novas"
# O nome de arquivo CLAUDE.md e do proprio RustDesk e sai da busca; a linha do grep abaixo tambem.
if git diff --cached -U0 -- . ':(exclude)CLAUDE.md' ':(exclude)AGENTS.md' | grep '^+' | grep -v '^+++' | grep -v 'grep -i -E' | sed 's/CLAUDE\.md//g' | grep -i -E 'claude|anthropic|openai|chatgpt|copilot|gemini'; then echo "FALHOU: mencao a IA"; falhou=1; else echo "ok"; fi

echo "== Mensagem de commit"
if [ -n "$1" ]; then
  grep -q '^Autor: Manfred Heil Junior$' "$1" || { echo "FALHOU: falta a linha Autor"; falhou=1; }
  if grep -i -E '^Co-Authored-By:|Generated with' "$1"; then echo "FALHOU: credito a IA na mensagem"; falhou=1; fi
else
  echo "FALHOU: informe o arquivo da mensagem (sh portoes.sh <arquivo>)"; falhou=1
fi

echo "== Segredos"
if echo "$arquivos" | grep -E '(^|/)\.env$|\.pfx$|\.p12$|\.pem$|\.key$'; then echo "FALHOU: arquivo de segredo"; falhou=1; else echo "ok"; fi
if git diff --cached -U0 | grep '^+' | grep -i -E 'BEGIN (RSA |EC |OPENSSH )?PRIVATE KEY|ghp_|gho_|github_pat_'; then echo "FALHOU: segredo no texto"; falhou=1; else echo "ok"; fi

[ $falhou -eq 0 ] && echo "PORTOES OK" || { echo "PORTOES FALHARAM"; exit 1; }
```

O `CLAUDE.md` e o `AGENTS.md` ficam fora da busca por IA porque o nome do arquivo e a referência `@AGENTS.md` são do próprio RustDesk.

- [ ] **Passo 7: Preparar o commit e rodar os portões**

Gravar antes a mensagem do passo 8 em `.superpowers/rascunho/msg-tarefa-3.txt`.

```bash
git add AGENTS-MT.md CLAUDE.md README-MT.md .gitignore .gitmodules .githooks docs/legal docs/superpowers
sh .superpowers/rascunho/portoes.sh .superpowers/rascunho/msg-tarefa-3.txt
```

Esperado: "PORTOES OK" e a lista só com os arquivos acima. Se falhar, corrigir e repetir antes de commitar.

- [ ] **Passo 8: Commit**

Gravar `.superpowers/rascunho/msg-tarefa-3.txt`:

```text
Traz regras, documentos e ganchos da MT para o fork

O MapDesk-MT nasce do RustDesk 1.5.0 sem mudanca de codigo. Este commit
traz as regras da MT (AGENTS-MT.md), o desenho, o plano, as verificacoes
juridicas e as pendencias, liga os ganchos que enviam cada commit ao
GitHub e aponta o submodulo hbb_common para o fork da MT, no mesmo
commit, para o codigo de cada versao continuar disponivel (AGPL-3.0,
secao 6).

Autor: Manfred Heil Junior
```

```bash
git commit -F .superpowers/rascunho/msg-tarefa-3.txt
git log -1 --format='%an <%ae>%n%B'
git ls-remote origin refs/heads/fundacao
```

Esperado: autor "Manfred Heil Junior <manfred@manfred.com.br>", a mensagem acima, e o `ls-remote` com o mesmo SHA do commit local (o gancho enviou). Se o gancho avisar que falhou, rodar `git push origin fundacao`.

---

### Tarefa 4: Workflow de compilação do Windows x64

**Arquivos:**
- Criar: `.github/workflows/mapdesk-windows.yml`, `.superpowers/rascunho/msg-tarefa-4.txt`

**Consome:** ramo `fundacao` da tarefa 3; workflows `bridge.yml` e `third-party-RustDeskTempTopMostWindow.yml` do oficial, ligados.

**Produz:** artefato `mapdesk-mt-windows-x64` com `rustdesk-1.5.0-x86_64.exe` em todo PR para `mt`; release com o executável em tag `*-mt.*`.

O conteúdo vem do job `build-for-windows-flutter` do `flutter-build.yml` da tag `1.5.0`, linhas 109 a 463. Fica só a linha x64; saem o ARM64, a assinatura (fatia 4), o MSI e o modelo de MSI (o executável se instala pelo botão "Instalar"). O nome do arquivo continua `rustdesk-...` nesta fatia e muda na fatia 3.

- [ ] **Passo 1: Escrever o workflow**

```yaml
name: MapDesk-MT Windows x64

on:
  pull_request:
    branches: [mt]
  push:
    tags: ["*-mt.*"]
  workflow_dispatch:

env:
  RUST_VERSION: "1.75"
  SCITER_RUST_VERSION: "1.75"
  LLVM_VERSION: "15.0.6"
  FLUTTER_VERSION: "3.24.5"
  VCPKG_BINARY_SOURCES: "clear;x-gha,readwrite"
  VCPKG_COMMIT_ID: "9e593bb18ea69cc5095e012465dcd675a822ed0d"
  VERSION: "1.5.0"

jobs:
  generate-bridge:
    uses: ./.github/workflows/bridge.yml

  build-topmostwindow:
    uses: ./.github/workflows/third-party-RustDeskTempTopMostWindow.yml
    with:
      upload-artifact: true
      target: windows-2022
      configuration: Release
      platform: x64
      target_version: Windows10

  build-windows-x64:
    name: Windows x64
    needs: [generate-bridge, build-topmostwindow]
    runs-on: windows-2022
    permissions:
      contents: write
    steps:
      - name: Export GitHub Actions cache environment variables
        uses: actions/github-script@d7906e4ad0b1822421a7e6a35d5ca353c962f410 # v6
        with:
          script: |
            core.exportVariable('ACTIONS_CACHE_URL', process.env.ACTIONS_CACHE_URL || '');
            core.exportVariable('ACTIONS_RUNTIME_TOKEN', process.env.ACTIONS_RUNTIME_TOKEN || '');

      - name: Checkout source code
        uses: actions/checkout@34e114876b0b11c390a56381ad16ebd13914f8d5 # v4
        with:
          submodules: recursive

      - name: Restore bridge files
        uses: actions/download-artifact@3e5f45b2cfb9172054b4087a40e8e0b5a5461e7c # v8.0.1
        with:
          name: bridge-artifact
          path: ./

      - name: Install LLVM and Clang
        uses: KyleMayes/install-llvm-action@ebc0426251bc40c7cd31162802432c68818ab8f0 # v2.0.9
        with:
          version: ${{ env.LLVM_VERSION }}

      - name: Install flutter
        uses: subosito/flutter-action@2783a3f08e1baf891508463f8c6653c258246225 # v2.12.0
        with:
          channel: "stable"
          flutter-version: ${{ env.FLUTTER_VERSION }}
          architecture: x64

      - name: Replace engine with rustdesk custom flutter engine
        run: |
          flutter doctor -v
          flutter precache --windows
          Invoke-WebRequest -Uri https://github.com/rustdesk/engine/releases/download/main/windows-x64-release.zip -OutFile windows-x64-release.zip
          Expand-Archive -Path windows-x64-release.zip -DestinationPath windows-x64-release
          mv -Force windows-x64-release/*  C:/hostedtoolcache/windows/flutter/stable-${{ env.FLUTTER_VERSION }}-x64/bin/cache/artifacts/engine/windows-x64-release/

      - name: Patch flutter
        shell: bash
        run: |
          cp .github/patches/flutter_3.24.4_dropdown_menu_enableFilter.diff $(dirname $(dirname $(which flutter)))
          cd $(dirname $(dirname $(which flutter)))
          if [[ "3.24.5" == ${{ env.FLUTTER_VERSION }} ]]; then
            git apply flutter_3.24.4_dropdown_menu_enableFilter.diff
          fi

      - name: Install Rust toolchain
        uses: dtolnay/rust-toolchain@e97e2d8cc328f1b50210efc529dca0028893a2d9 # v1
        with:
          toolchain: ${{ env.SCITER_RUST_VERSION }}
          targets: x86_64-pc-windows-msvc
          components: "rustfmt"

      - uses: Swatinem/rust-cache@e18b497796c12c097a38f9edb9d0641fb99eee32 # v2
        with:
          prefix-key: windows-2022

      - name: Setup vcpkg with Github Actions binary cache
        uses: lukka/run-vcpkg@b1a0dd252f06b9e25b3c022a9a03bd7a427fb6a2 # v11
        with:
          vcpkgDirectory: C:\vcpkg
          vcpkgGitCommitId: ${{ env.VCPKG_COMMIT_ID }}
          doNotCache: false

      - name: Install vcpkg dependencies
        env:
          VCPKG_DEFAULT_HOST_TRIPLET: x64-windows-static
        shell: bash
        run: |
          if ! $VCPKG_ROOT/vcpkg install --triplet x64-windows-static --x-install-root="$VCPKG_ROOT/installed"; then
            find "${VCPKG_ROOT}/" -name "*.log" | while read -r _1; do
              echo "$_1:"; echo "======"; cat "$_1"; echo "======"; echo ""
            done
            exit 1
          fi

      - name: Build rustdesk
        run: |
          python3 .\build.py --portable --flutter --skip-portable-pack --hwcodec --vram
          mv ./flutter/build/windows/x64/runner/Release ./rustdesk

          Invoke-WebRequest -Uri https://github.com/rustdesk-org/rdev/releases/download/usbmmidd_v2/usbmmidd_v2.zip -OutFile usbmmidd_v2.zip
          Expand-Archive usbmmidd_v2.zip -DestinationPath .
          Remove-Item -Path usbmmidd_v2\Win32 -Recurse
          Remove-Item -Path "usbmmidd_v2\deviceinstaller64.exe", "usbmmidd_v2\deviceinstaller.exe", "usbmmidd_v2\usbmmidd.bat"
          mv -Force .\usbmmidd_v2 ./rustdesk

          try {
            Invoke-WebRequest -Uri https://github.com/rustdesk/hbb_common/releases/download/driver/rustdesk_printer_driver_v4-1.4.zip -OutFile rustdesk_printer_driver_v4-1.4.zip
            Invoke-WebRequest -Uri https://github.com/rustdesk/hbb_common/releases/download/driver/printer_driver_adapter.zip -OutFile printer_driver_adapter.zip
            Invoke-WebRequest -Uri https://github.com/rustdesk/hbb_common/releases/download/driver/sha256sums -OutFile sha256sums
            $checksum_driver = (Select-String -Path .\sha256sums -Pattern '^([a-fA-F0-9]{64}) \*rustdesk_printer_driver_v4-1.4\.zip$').Matches.Groups[1].Value
            $downloadsum_driver = Get-FileHash -Path rustdesk_printer_driver_v4-1.4.zip -Algorithm SHA256
            $checksum_adapter = (Select-String -Path .\sha256sums -Pattern '^([a-fA-F0-9]{64}) \*printer_driver_adapter\.zip$').Matches.Groups[1].Value
            $downloadsum_adapter = Get-FileHash -Path printer_driver_adapter.zip -Algorithm SHA256
            if ($checksum_driver -eq $downloadsum_driver.Hash -and $checksum_adapter -eq $downloadsum_adapter.Hash) {
                Expand-Archive rustdesk_printer_driver_v4-1.4.zip -DestinationPath .
                mkdir ./rustdesk/drivers
                mv -Force .\rustdesk_printer_driver_v4-1.4 ./rustdesk/drivers/RustDeskPrinterDriver
                Expand-Archive printer_driver_adapter.zip -DestinationPath .
                mv -Force .\printer_driver_adapter.dll ./rustdesk
            } else {
                Write-Output "Printer driver checksums do not match, ignore the files."
            }
          } catch {
              Write-Host "Ignore the printer driver error."
          }

      - name: Find Runner.res
        continue-on-error: true
        shell: bash
        run: |
          runner_res=$(find . -name "Runner.res");
          if [ "$runner_res" == "" ]; then
            echo "Runner.res: not found";
          else
            cp $runner_res ./libs/portable/Runner.res;
            ls -l ./libs/portable/Runner.res;
          fi

      - name: Download RustDeskTempTopMostWindow artifacts
        uses: actions/download-artifact@3e5f45b2cfb9172054b4087a40e8e0b5a5461e7c # v8.0.1
        with:
          name: topmostwindow-artifacts-x64
          path: "./rustdesk"

      - name: Build self-extracted executable
        shell: bash
        run: |
          sed -i '/dpiAware/d' res/manifest.xml
          pushd ./libs/portable
          pip3 install -r requirements.txt
          python3 ./generate.py -f ../../rustdesk/ -o . -e ../../rustdesk/rustdesk.exe
          popd
          mkdir -p ./SaidaMT
          mv ./target/release/rustdesk-portable-packer.exe ./SaidaMT/rustdesk-${{ env.VERSION }}-x86_64.exe
          sha256sum ./SaidaMT/*.exe

      - name: Upload executable
        uses: actions/upload-artifact@043fb46d1a93c77aae656e7c1c64a875d1fc6a0a # v7.0.1
        with:
          name: mapdesk-mt-windows-x64
          path: ./SaidaMT/*.exe

      - name: Publish release (tag only)
        if: startsWith(github.ref, 'refs/tags/')
        uses: softprops/action-gh-release@de2c0eb89ae2a093876385947365aca7b0e5f844 # v1
        with:
          prerelease: true
          tag_name: ${{ github.ref_name }}
          body: |
            Código-fonte desta versão: https://github.com/${{ github.repository }}/tree/${{ github.ref_name }}
            Distribuído sob a AGPL-3.0. Baseado no RustDesk; não é produto oficial do RustDesk.
          files: ./SaidaMT/*.exe
```

- [ ] **Passo 2: Portões e commit**

Gravar `.superpowers/rascunho/msg-tarefa-4.txt`:

```text
Cria compilacao do Windows x64 no GitHub Actions

Workflow da MT derivado do job build-for-windows-flutter do
flutter-build.yml oficial (tag 1.5.0), so com o Windows x64 e sem
assinatura, MSI e ARM64. Roda em Pull Request para mt, em tag
<versao>-mt.<n> e por acionamento manual. Em PR, o executavel sai
como artefato para o teste; em tag, vai para a versao (release) com o
link do codigo-fonte.

Autor: Manfred Heil Junior
```

```bash
git add .github/workflows/mapdesk-windows.yml
sh .superpowers/rascunho/portoes.sh .superpowers/rascunho/msg-tarefa-4.txt
git commit -F .superpowers/rascunho/msg-tarefa-4.txt
git ls-remote origin refs/heads/fundacao
```

Esperado: "PORTOES OK"; o `ls-remote` mostra o SHA do commit novo.

---

### Tarefa 5: Pull Request, CI e executável

**Arquivos:**
- Criar: `.superpowers/rascunho/pr-fatia-1.md`
- Alterar (se o CI falhar): `.github/workflows/mapdesk-windows.yml`

**Consome:** ramo `fundacao` com as tarefas 3 e 4.

**Produz:** PR `fundacao` para `mt`, com o CI verde e o executável baixado para o teste do Manfred.

- [ ] **Passo 1: Corpo do PR**

Gravar `.superpowers/rascunho/pr-fatia-1.md` (passa pela `humanizar-ptbr`):

```markdown
## O que muda

- Traz as regras da MT (`AGENTS-MT.md`), o `README-MT.md`, o desenho, o plano, as verificações jurídicas e as pendências.
- Liga os ganchos que enviam cada commit ao GitHub.
- Aponta o submódulo `hbb_common` para `manfredjr/hbb_common`, no mesmo commit do oficial.
- Cria a compilação do Windows x64 no GitHub Actions.
- Nenhum código do RustDesk muda: o executável é o RustDesk 1.5.0 puro, sem assinatura.

## Como testar

1. Baixar o artefato `mapdesk-mt-windows-x64` da execução do Actions deste PR (ou o arquivo entregue no chat).
2. Abrir o `rustdesk-1.5.0-x86_64.exe` numa máquina de teste. O SmartScreen avisa "editor desconhecido": clicar em "Mais informações" e "Executar assim mesmo".
3. Conferir que a janela do RustDesk abre e mostra um ID.

Atenção: este executável ainda é o RustDesk oficial e fala com os servidores do RustDesk. É só para teste interno.

Autor: Manfred Heil Junior
```

- [ ] **Passo 2: Abrir o PR**

```bash
gh pr create -R manfredjr/mapdesk-mt --base mt --head fundacao --title "Fatia 1: fundacao do MapDesk-MT" --body-file .superpowers/rascunho/pr-fatia-1.md
```

- [ ] **Passo 3: Ler o CI**

```bash
gh pr checks <n> -R manfredjr/mapdesk-mt
```

A compilação leva bem mais de meia hora. Esperar a notificação, sem consultar em laço. Esperado: todos os checks `pass`. Se algum falhar: `gh run view <id> -R manfredjr/mapdesk-mt --log-failed`. Investigar a causa com `superpowers:systematic-debugging`, corrigir o workflow num commit novo (portões antes) e ler o CI de novo. Nunca dizer que passou sem ler a saída do `gh pr checks`.

- [ ] **Passo 4: Baixar o executável**

```bash
gh run download <id-da-execucao> -R manfredjr/mapdesk-mt -n mapdesk-mt-windows-x64 -D .superpowers/rascunho/artefato-fatia-1
ls -la .superpowers/rascunho/artefato-fatia-1
sha256sum .superpowers/rascunho/artefato-fatia-1/*.exe
```

Esperado: `rustdesk-1.5.0-x86_64.exe`, com o mesmo SHA-256 mostrado no log do passo "Build self-extracted executable".

- [ ] **Passo 5: Atualizar a situação no mesmo PR**

No `README-MT.md`, linha da fatia 1: trocar "em andamento" por "pronta para teste, PR #<n>". Gravar `.superpowers/rascunho/msg-tarefa-5.txt` com o título `Atualiza situacao da fatia 1`, uma linha em branco e `Autor: Manfred Heil Junior`; `git add README-MT.md`; `sh .superpowers/rascunho/portoes.sh .superpowers/rascunho/msg-tarefa-5.txt`; `git commit -F .superpowers/rascunho/msg-tarefa-5.txt`.

- [ ] **Passo 6: Teste do Manfred e merge**

Entregar ao Manfred o caminho do executável e o link do PR. O merge só acontece com a frase "conferi tudo certo, pode juntar o PR #<n>":

```bash
gh pr merge <n> -R manfredjr/mapdesk-mt --merge --delete-branch
git checkout mt
git pull origin mt
gh run list -R manfredjr/mapdesk-mt --branch mt --limit 3
```

Depois do merge, a linha da fatia 1 no `README-MT.md` passa a "feita, PR #<n>" no primeiro commit da fatia 2.

---

## Fora desta fatia

`src/mt_config.rs` (fatia 2), nome e ícones (fatia 3), assinatura (fatia 4) e release `1.5.0-mt.1` (fatia 5).
