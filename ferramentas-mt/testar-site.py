"""Confere a pagina do produto em public/ antes da publicacao (spec do site, secao 6)."""
import html.parser
import pathlib
import re
import sys

RAIZ = pathlib.Path(__file__).resolve().parent.parent
PUBLIC = RAIZ / "public"
REPO = "https://github.com/manfredjr/mapdesk-mt"
IMAGENS = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".ico", ".avif", ".bmp"}

PROIBIDOS = {
    "\u2014": "travessao longo",
    "\u2013": "travessao medio",
    "\u201c": "aspa curva",
    "\u201d": "aspa curva",
    "\u2018": "aspa curva",
    "\u2019": "aspa curva",
    "\u2026": "reticencias de um caractere",
    "\u00a0": "espaco especial",
    "\u202f": "espaco especial",
    "\u2009": "espaco especial",
    "\u200b": "espaco de largura zero",
    "\u2192": "seta",
    "\u00d7": "sinal de multiplicacao",
    "\u2212": "sinal de menos",
    "\u2190": "seta",
    "\u2022": "marcador solto",
    "\u2011": "hifen especial",
    "\u2060": "espaco de largura zero",
    "\ufeff": "marca de ordem de bytes",
}
MEDICAO = re.compile(r"googletagmanager|google-analytics|clarity\.ms|facebook\.net|fonts\.googleapis|doubleclick", re.I)
# URL absoluta ou "//", fora o proprio dominio do site (o canonical aponta para ele).
EXTERNO = r"(?:https?:)?//(?!mapdesk\.manfred\.com\.br/)"
REGRAS_EXTERNAS = {
    "script externo": re.compile(r"<script\b[^>]*\bsrc\s*=\s*[\"']?" + EXTERNO, re.I),
    "link externo": re.compile(r"<link\b[^>]*\bhref\s*=\s*[\"']?" + EXTERNO, re.I),
    "iframe externo": re.compile(r"<iframe\b[^>]*\bsrc\s*=\s*[\"']?" + EXTERNO, re.I),
    "midia externa": re.compile(r"<(?:img|object|embed|source|video)\b[^>]*\b(?:src|data)\s*=\s*[\"']?" + EXTERNO, re.I),
    "@import externo": re.compile(r"@import\s+(?:url\(\s*)?[\"']?" + EXTERNO, re.I),
    "url() externa": re.compile(r"url\(\s*[\"']?" + EXTERNO, re.I),
}


class Ancoras(html.parser.HTMLParser):
    """Junta os <a> com href e classes. O parser ignora comentarios HTML."""

    def __init__(self):
        super().__init__()
        self.ancoras = []

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            a = dict(attrs)
            self.ancoras.append(((a.get("class") or "").split(), a.get("href")))


def versao():
    texto = (RAIZ / "flutter/lib/mt/mt_info.dart").read_text(encoding="utf-8")
    achado = re.search(r"kMtVersao\s*=\s*'([^']+)'", texto)
    return achado.group(1) if achado else None


def conferir_botao(ancoras, classe, esperado, desc):
    hrefs = [href for classes, href in ancoras if classe in classes]
    if not hrefs:
        return [f"public/index.html: falta o {desc} (a.{classe})"]
    return [f"public/index.html: {desc} (a.{classe}) aponta para {h}, esperado {esperado}" for h in hrefs if h != esperado]


def conferir():
    falhas = []
    if not (PUBLIC / "index.html").is_file():
        return ["public/index.html nao existe"]
    v = versao()
    if not v:
        falhas.append("kMtVersao nao encontrado em mt_info.dart")
    textos = {}
    for p in sorted(PUBLIC.rglob("*")):
        if p.is_file() and p.suffix.lower() not in IMAGENS:
            textos[p] = p.read_text(encoding="utf-8", errors="replace")
    for caminho, texto in textos.items():
        nome = caminho.relative_to(RAIZ).as_posix()
        for marca in re.findall(r"\[(?:PREENCHER|FONTE\?)[^\]]*\]", texto):
            falhas.append(f"{nome}: marca {marca}")
        for car, desc in PROIBIDOS.items():
            if car in texto:
                falhas.append(f"{nome}: {desc}")
        for termo in sorted({m.group(0).lower() for m in MEDICAO.finditer(texto)}):
            falhas.append(f"{nome}: medicao ou conteudo de terceiros ({termo})")
        for desc, regra in REGRAS_EXTERNAS.items():
            if regra.search(texto):
                falhas.append(f"{nome}: {desc}")
        if re.search(r"sourceMappingURL", texto, re.I):
            falhas.append(f"{nome}: sourceMappingURL")
        if "releases/latest" in texto:
            falhas.append(f"{nome}: releases/latest nao alcanca a pre-versao")
    for mapa in PUBLIC.rglob("*.map"):
        falhas.append(f"{mapa.relative_to(RAIZ).as_posix()}: source map")
    index = textos.get(PUBLIC / "index.html", "")
    leitor = Ancoras()
    leitor.feed(index)
    hrefs = {href for _, href in leitor.ancoras}
    if v:
        baixar = f"{REPO}/releases/download/{v}/MapDesk-MT.exe"
        falhas += conferir_botao(leitor.ancoras, "btn--primario", baixar, "botao de baixar")
        falhas += conferir_botao(leitor.ancoras, "btn--secundario", f"{REPO}/tree/{v}", "botao do codigo")
        regra = re.compile(r"href\s*=\s*[\"']?([^\"'\s>]*releases/download/[^\"'\s>]*)", re.I)
        for caminho, texto in textos.items():
            for h in regra.findall(texto):
                if h not in (baixar, f"{baixar}.sha256"):
                    falhas.append(f"{caminho.relative_to(RAIZ).as_posix()}: link de download fora da versao ({h})")
        exigidos = {
            f"{baixar}.sha256": "SHA-256 da versao",
            f"{REPO}/tree/{v}": "codigo da versao exata",
            f"{REPO}/blob/{v}/LICENCE": "licenca AGPL-3.0",
            "privacidade.html": "pagina de privacidade",
        }
        for alvo, desc in exigidos.items():
            if alvo not in hrefs:
                falhas.append(f"public/index.html: falta o link da {desc} ({alvo})")
    if "AGPL-3.0" not in re.sub(r"(?s)<!--.*?-->", "", index):
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
