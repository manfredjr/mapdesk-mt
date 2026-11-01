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
        for marca in re.findall(r"\[(?:PREENCHER|FONTE\?)[^\]]*\]", texto):
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
