# Site do produto MapDesk-MT: plano de implementação

> **Para agentes:** use `superpowers:subagent-driven-development` (recomendado) ou `superpowers:executing-plans` para seguir este plano tarefa por tarefa. Os passos usam caixas (`- [ ]`) para o acompanhamento.

**Objetivo:** publicar a página estática do MapDesk-MT em `mapdesk.manfred.com.br`, no modelo do MapDisk, com o teste que barra publicação sem as exigências da AGPL e com medição de terceiros.

**Arquitetura:** pasta `public/` no próprio repositório `manfredjr/mapdesk-mt`, servida pelo Git do cPanel. Um roteiro Python sem dependências (`ferramentas-mt/testar-site.py`) confere a página e roda num workflow próprio. O workflow de compilação ganha o arquivo SHA-256 na versão pública.

**Tecnologia:** HTML e CSS estáticos, Python 3.12 (biblioteca padrão), GitHub Actions, Apache (`.htaccess`).

**Spec:** `docs/superpowers/specs/2026-11-01-mapdesk-site-produto-design.md`.

## Regras globais

- Ramo `mt-site`. Nunca commit no `mt`. Nada de `--amend`, rebase, reset nem force-push.
- Commit: verbo na 3ª pessoa, título sem acento, corpo com o porquê, última linha `Autor: Manfred Heil Junior`. Sem `Co-Authored-By`, sem "Generated with", sem nome de ferramenta de IA.
- Portões antes de cada commit: `sh .superpowers/rascunho/portoes.sh <arquivo-da-mensagem>`. Na worktree, use o `portoes.sh` da pasta principal do projeto.
- Texto em português do Brasil, sem travessão longo ou médio, aspas curvas, reticências de um caractere, espaço especial nem seta. Os textos da página passam pela skill `humanizar-ptbr` antes de gravar.
- Não inventar dado: o que não tem fonte vira `[PREENCHER]`, e o teste barra a publicação.
- Versão da página: a de `kMtVersao` em `flutter/lib/mt/mt_info.dart`, hoje `1.5.0-mt.1`.
- Modelo: o repositório público `manfredjr/mapdisk`, lido com `gh api repos/manfredjr/mapdisk/contents/<caminho> --jq .content | base64 -d`.
- Proibido nesta fatia: criar tag, criar versão, fazer merge e publicar no cPanel.
- `gh` sempre com `-R manfredjr/mapdesk-mt`.

---

### Tarefa 1: teste da página e workflow

**Arquivos:**
- Criar: `ferramentas-mt/testar-site.py`
- Criar: `.github/workflows/mapdesk-site.yml`

**Interfaces:**
- Produz: `python ferramentas-mt/testar-site.py`, que sai com 0 quando tudo passa e com 1 quando algo falha, listando cada falha numa linha que começa com `FALHA:`.

- [ ] **Passo 1: escrever o teste**

```python
"""Confere a pagina do produto em public/ antes da publicacao (spec do site, secao 6)."""
import pathlib
import re
import sys

RAIZ = pathlib.Path(__file__).resolve().parent.parent
PUBLIC = RAIZ / "public"
REPO = "https://github.com/manfredjr/mapdesk-mt"

PROIBIDOS = {
    "\u2014": "travessao longo",
    "\u2013": "travessao medio",
    "\u201c": "aspa curva",
    "\u201d": "aspa curva",
    "\u2018": "aspa curva",
    "\u2019": "aspa curva",
    "\u2026": "reticencias de um caractere",
    "\u00a0": "espaco especial",
    "\u2192": "seta",
}
MEDICAO = ["googletagmanager", "google-analytics", "clarity.ms", "facebook.net", "fonts.googleapis", "doubleclick"]


def versao():
    texto = (RAIZ / "flutter/lib/mt/mt_info.dart").read_text(encoding="utf-8")
    achado = re.search(r"kMtVersao\s*=\s*'([^']+)'", texto)
    return achado.group(1) if achado else None


def conferir():
    falhas = []
    if not (PUBLIC / "index.html").is_file():
        return ["public/index.html nao existe"]
    v = versao()
    if not v:
        falhas.append("kMtVersao nao encontrado em mt_info.dart")
    textos = {p: p.read_text(encoding="utf-8") for p in PUBLIC.rglob("*") if p.suffix in (".html", ".css", ".htaccess") or p.name == ".htaccess"}
    for caminho, texto in textos.items():
        nome = caminho.relative_to(RAIZ).as_posix()
        for marca in ("[PREENCHER]", "[FONTE?]"):
            if marca in texto:
                falhas.append(f"{nome}: marca {marca}")
        for car, desc in PROIBIDOS.items():
            if car in texto:
                falhas.append(f"{nome}: {desc}")
        for termo in MEDICAO:
            if termo in texto:
                falhas.append(f"{nome}: medicao ou conteudo de terceiros ({termo})")
        if re.search(r"<script[^>]+src=[\"']https?://", texto):
            falhas.append(f"{nome}: script externo")
    for mapa in PUBLIC.rglob("*.map"):
        falhas.append(f"{mapa.relative_to(RAIZ).as_posix()}: source map")
    index = textos.get(PUBLIC / "index.html", "")
    if v:
        exigidos = {
            f"{REPO}/releases/download/{v}/MapDesk-MT.exe": "botao de baixar com a tag exata",
            f"{REPO}/tree/{v}": "codigo da versao exata",
            f"{REPO}/blob/{v}/LICENCE": "licenca AGPL-3.0",
            "privacidade.html": "pagina de privacidade",
        }
        for alvo, desc in exigidos.items():
            if f'href="{alvo}"' not in index:
                falhas.append(f"public/index.html: falta o link da {desc} ({alvo})")
    if "AGPL-3.0" not in index:
        falhas.append("public/index.html: falta a mencao a AGPL-3.0")
    if not (PUBLIC / "privacidade.html").is_file():
        falhas.append("public/privacidade.html nao existe")
    cpanel = RAIZ / ".cpanel.yml"
    if not cpanel.is_file():
        falhas.append(".cpanel.yml nao existe")
    else:
        for alvo in re.findall(r"test -f \$REPO/(\S+)", cpanel.read_text(encoding="utf-8")):
            if not (RAIZ / alvo).is_file():
                falhas.append(f".cpanel.yml cita {alvo}, que nao existe")
    return falhas


if __name__ == "__main__":
    resultado = conferir()
    for f in resultado:
        print(f"FALHA: {f}")
    print("SITE OK" if not resultado else f"{len(resultado)} falha(s)")
    sys.exit(1 if resultado else 0)
```

- [ ] **Passo 2: rodar e ver falhar**

Rodar: `python ferramentas-mt/testar-site.py`
Esperado: `FALHA: public/index.html nao existe` e saída 1.

- [ ] **Passo 3: criar o workflow**

```yaml
name: MapDesk-MT site

on:
  pull_request:
    paths:
      - "public/**"
      - ".cpanel.yml"
      - "ferramentas-mt/testar-site.py"
      - "flutter/lib/mt/mt_info.dart"
      - ".github/workflows/mapdesk-site.yml"
  push:
    branches: [mt]
    paths:
      - "public/**"
      - ".cpanel.yml"
      - "ferramentas-mt/testar-site.py"

permissions:
  contents: read

jobs:
  testar-site:
    runs-on: ubuntu-22.04
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - run: python ferramentas-mt/testar-site.py
```

- [ ] **Passo 4: commit** "Cria o teste da pagina do produto MapDesk-MT". O CI desse commit falha de propósito, porque a página ainda não existe. A Tarefa 2 resolve.

---

### Tarefa 2: página, privacidade, estilo, imagens e `.cpanel.yml`

**Arquivos:**
- Criar: `public/index.html`, `public/privacidade.html`, `public/css/site.css`, `public/.htaccess`
- Criar: `public/imagens/mapdesk.png` (cópia de `docs/marca/mapdesk-mt-simbolo.png`), `public/imagens/mt-logo.png` (cópia de `flutter/assets/mt-logo.png`) e `public/imagens/janela.png`
- Criar: `.cpanel.yml`

**Interfaces:**
- Consome: o teste da Tarefa 1.

- [ ] **Passo 1: copiar o modelo.** Baixar do `manfredjr/mapdisk` os arquivos `public/index.html`, `public/privacidade.html`, `public/css/site.css`, `public/.htaccess` e `.cpanel.yml` para `.superpowers/rascunho/modelo-mapdisk/`, só como leitura. Preservar a estrutura de seções, as classes CSS e o cabeçalho.
- [ ] **Passo 2: `.htaccess` e `.cpanel.yml`.** Copiar o `.htaccess` do MapDisk, trocando "MapDisk" por "MapDesk-MT" no comentário. No `.cpanel.yml`, usar `REPO=$HOME/repositories/mapdesk-mt` e manter as tarefas.
- [ ] **Passo 3: estilo.** Copiar o `site.css`. Trocar só as variáveis de cor pelas da família: `#006B2D`, `#0F8F2F`, `#43A92C`, `#9AD52B` e o texto `#202020`. Fonte local ou do sistema, nunca `fonts.googleapis`.
- [ ] **Passo 4: imagens.**
  - copiar os dois logos;
  - montar o `janela.png` com Pillow, a partir de um print da janela do MapDesk-MT, trocando o ID por `123 456 789` e o nome do computador por `estacao-exemplo`;
  - se não houver print, pedir um ao orquestrador. Nunca publicar ID ou nome de máquina real.
- [ ] **Passo 5: `index.html`**, com as seções da spec (seção 3), na ordem e com os links exigidos pelo teste (v = `1.5.0-mt.1`):
  - baixar: `https://github.com/manfredjr/mapdesk-mt/releases/download/1.5.0-mt.1/MapDesk-MT.exe`;
  - código: `https://github.com/manfredjr/mapdesk-mt/tree/1.5.0-mt.1`;
  - licença: `https://github.com/manfredjr/mapdesk-mt/blob/1.5.0-mt.1/LICENCE`;
  - privacidade: `privacidade.html`;
  - versões: `https://github.com/manfredjr/mapdesk-mt/releases`;
  - logo da MT, clicável para `https://www.manfred.com.br`.
  
  O SHA-256 ainda não existe: escrever "o SHA-256 está na página da versão" com o link das versões, sem número.
  
  O texto de privacidade vem de `https://manfred.com.br/acesso`, lido em 01/11/2026 (ID, IP e horário de cada conexão, 6 meses, acesso restrito, nada da tela gravado).
  
  O texto de "Uso autorizado", com a cláusula contra cópia e raspagem do conteúdo, fica marcado `[PREENCHER]` até passar pela `legal-br`. O teste vai acusar a marca; a Tarefa 4 resolve.
- [ ] **Passo 6: `privacidade.html`.** Seguir o modelo do MapDisk, com o conteúdo do MapDesk-MT:
  - o que o servidor registra e por quanto tempo;
  - que o programa não manda dado para a RustDesk (`register-device = N`);
  - o contato público `manfred@manfred.com.br`.
  
  Endereço e telefone do cartão CNPJ nunca entram. O que não tiver fonte fica `[PREENCHER]`.
- [ ] **Passo 7: humanizar.** Passar os textos de `index.html` e `privacidade.html` pela `humanizar-ptbr`.
- [ ] **Passo 8: rodar o teste.** Esperado: só sobram as falhas de `[PREENCHER]` da Tarefa 4.
- [ ] **Passo 9: commit** "Cria a pagina do produto MapDesk-MT".

---

### Tarefa 3: SHA-256 e notas na versão pública

**Arquivos:**
- Modificar: `.github/workflows/mapdesk-windows.yml`, nos passos entre "Build self-extracted executable" e "Publish release (tag only)".

- [ ] **Passo 1:** depois da linha `sha256sum ./SaidaMT/*.exe` (linha 177 hoje), acrescentar no mesmo passo:

```bash
(cd SaidaMT && sha256sum MapDesk-MT.exe > MapDesk-MT.exe.sha256)
```

- [ ] **Passo 2:** no passo "Publish release (tag only)", trocar `files: ./SaidaMT/*.exe` por:

```yaml
          files: |
            ./SaidaMT/MapDesk-MT.exe
            ./SaidaMT/MapDesk-MT.exe.sha256
```

  e acrescentar `body_path: docs/notas-versao.md`.
- [ ] **Passo 3:** criar `docs/notas-versao.md` com:
  - o aviso de modificação (com a data);
  - a AGPL-3.0;
  - o fork `manfredjr/hbb_common` com o commit do submódulo (`git submodule status libs/hbb_common`);
  - o aviso de que o executável não tem assinatura digital;
  - o link para `https://mapdesk.manfred.com.br/`.
  
  Passar pela `humanizar-ptbr`.
- [ ] **Passo 4:** o PR roda a compilação, que leva de 40 a 60 minutos. Conferir que o artefato traz os dois arquivos. A versão só sai na tag, que não é desta fatia.
- [ ] **Passo 5: commit** "Publica o SHA-256 e as notas junto da versao".

---

### Tarefa 4: texto jurídico do "Uso autorizado"

**Arquivos:**
- Modificar: `public/index.html`, seção "Uso autorizado".
- Criar: `docs/legal/verificacao-site-produto-2026-11-01.md`.

- [ ] **Passo 1:** rodar a skill `legal-br` sobre a seção "Uso autorizado", a cláusula contra cópia e raspagem e o rodapé da AGPL. A verificação, com fonte e data de cada regra, vai para o arquivo acima.
- [ ] **Passo 2:** trocar o `[PREENCHER]` pelo texto aprovado na verificação.
- [ ] **Passo 3:** rodar o teste. Esperado: `SITE OK` e saída 0.
- [ ] **Passo 4: commit** "Traz o texto juridico da pagina do produto".

---

### Tarefa 5: varredura de dados sensíveis, situação e PR

**Arquivos:**
- Modificar: `README-MT.md` (situação do projeto) e `docs/publicacao.md` (passos do site, como na seção 8 da spec).
- Criar: `.superpowers/rascunho/varredura-repositorio-2026-11-01.md` (fora do git).

- [ ] **Passo 1: varredura.** Rodar no repositório inteiro e no histórico das mudanças da MT (`git log --all -p -- . ':!libs'` filtrado pelos commits da MT desde a base 1.5.0):

```bash
git grep -nIE "BEGIN (RSA|OPENSSH|EC|PRIVATE)|ghp_[A-Za-z0-9]{20,}|github_pat_|password\s*=|senha\s*=|192\.168\.|10\.[0-9]+\.[0-9]+\.[0-9]+|C:\\\\Users\\\\" -- . ':!libs' ':!*.lock'
git log --all --format=%H --author="Manfred" | while read c; do git show --name-only --format= "$c"; done | sort -u | grep -iE "\.(env|pfx|p12|pem|key)$"
```

  Registrar no rascunho o resultado de cada busca. Achado no código do RustDesk de origem não é da MT e não se altera; só se anota. Achado nas mudanças da MT para a fatia e vai ao orquestrador.
- [ ] **Passo 2:** atualizar o `README-MT.md` e o `docs/publicacao.md`.
- [ ] **Passo 3: commit** "Atualiza situacao e roteiro de publicacao do site".
- [ ] **Passo 4: PR.** `gh pr create -R manfredjr/mapdesk-mt --base mt --head mt-site --title "Site do produto MapDesk-MT" --body-file <arquivo>`, com "O que muda", "Como testar" (abrir `public/index.html` no navegador e conferir os links) e `Autor: Manfred Heil Junior`.
- [ ] **Passo 5:** ler o CI dos dois workflows com `gh pr checks <n> -R manfredjr/mapdesk-mt` até o fim e informar o resultado lido.
