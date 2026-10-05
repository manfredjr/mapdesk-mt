"""Gera os icones e imagens da marca MapDesk-MT a partir dos SVG de docs/marca/.

Uso, na raiz do repositorio: python ferramentas-mt/gerar-marca.py

Para trocar a arte, substitua os dois SVG em docs/marca/ e rode de novo.
Cada tamanho dos .ico e renderizado direto do SVG pelo Inkscape (sem reduzir
de um tamanho maior), para manter as linhas nitidas. Os .ico saem em DIB de
32 bits com mascara AND, o formato classico do Windows. Precisa do Pillow e do
Inkscape (caminho em INKSCAPE).
"""

import io
import os
import re
import shutil
import struct
import subprocess
import sys
import tempfile

from PIL import Image

INKSCAPE = os.environ.get("INKSCAPE", r"C:\Program Files\Inkscape\bin\inkscape")
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SIMBOLO = os.path.join(RAIZ, "docs", "marca", "mapdesk-mt-simbolo.svg")
LOGO = os.path.join(RAIZ, "docs", "marca", "mapdesk-mt-logo.svg")

TAMANHOS_APP = [16, 24, 32, 48, 64, 128, 256]
TAMANHOS_BANDEJA = [16, 20, 24, 32, 40, 48]
# O loadLogo() do Flutter limita o logo a 300x60 e reduz com BoxFit.contain.
# Como o logo e largo, a largura manda: 600 px e o dobro de 300 e fica nitido
# em telas com escala de 200%.
LARGURA_LOGO = 600


def caminho(*partes):
    return os.path.join(RAIZ, *partes)


def png_do_svg(svg, saida, largura, altura):
    subprocess.run(
        [INKSCAPE, svg, "--export-type=png", f"--export-filename={saida}",
         "-w", str(largura), "-h", str(altura)],
        check=True, capture_output=True,
    )
    return Image.open(saida).convert("RGBA")


def dib(imagem):
    largura, altura = imagem.size
    cabecalho = struct.pack("<IiiHHIIiiII", 40, largura, altura * 2, 1, 32, 0, 0, 0, 0, 0, 0)
    pixels = bytearray()
    mascara = bytearray()
    linha_mascara = ((largura + 31) // 32) * 4
    for y in range(altura - 1, -1, -1):
        linha = bytearray(linha_mascara)
        for x in range(largura):
            r, g, b, a = imagem.getpixel((x, y))
            pixels += bytes((b, g, r, a))
            if a == 0:
                linha[x // 8] |= 0x80 >> (x % 8)
        mascara += linha
    return cabecalho + bytes(pixels) + bytes(mascara)


def gravar_ico(imagens, destino):
    blocos = [dib(im) for im in imagens]
    saida = bytearray(struct.pack("<HHH", 0, 1, len(blocos)))
    inicio = 6 + 16 * len(blocos)
    for im, bloco in zip(imagens, blocos):
        lado = 0 if im.width >= 256 else im.width
        saida += struct.pack("<BBBBHHII", lado, lado, 0, 0, 1, 32, len(bloco), inicio)
        inicio += len(bloco)
    for bloco in blocos:
        saida += bloco
    os.makedirs(os.path.dirname(destino), exist_ok=True)
    with open(destino, "wb") as f:
        f.write(saida)
    print("gravado:", os.path.relpath(destino, RAIZ), [im.width for im in imagens])


def svg_do_rotulo():
    """Rotulo da tela do executavel portatil: simbolo claro e texto branco.

    O fundo da janela e azul acinzentado escuro e o original e texto branco,
    entao o simbolo usa branco no lugar do verde escuro.
    """
    with open(SIMBOLO, encoding="utf-8") as f:
        simbolo = f.read()
    miolo = re.search(r"<svg[^>]*>(.*)</svg>", simbolo, re.S).group(1)
    miolo = miolo.replace("#006B2D", "#FFFFFF").replace("#43A92C", "#9AD52B").replace("#0F8F2F", "#9AD52B")
    return (
        '<svg xmlns="http://www.w3.org/2000/svg" width="96" height="32" viewBox="0 0 96 32">'
        f'<g transform="translate(2 4) scale(0.375)">{miolo}</g>'
        '<text x="28" y="21" font-family="Montserrat, Arial, sans-serif" font-size="11.5" '
        'font-weight="700" fill="#FFFFFF" textLength="66" lengthAdjust="spacingAndGlyphs">MapDesk-MT</text>'
        "</svg>"
    )


def main():
    if not (os.path.exists(INKSCAPE) or shutil.which(INKSCAPE)):
        sys.exit(f"Inkscape nao encontrado em {INKSCAPE} (defina a variavel INKSCAPE)")
    with tempfile.TemporaryDirectory() as tmp:
        def render(lado):
            return png_do_svg(SIMBOLO, os.path.join(tmp, f"s{lado}.png"), lado, lado)

        app = [render(l) for l in TAMANHOS_APP]
        for destino in (
            caminho("flutter", "windows", "runner", "resources", "app_icon.ico"),
            caminho("res", "icon.ico"),
            caminho("flutter", "assets", "icon.ico"),
        ):
            gravar_ico(app, destino)
        gravar_ico([render(l) for l in TAMANHOS_BANDEJA], caminho("res", "tray-icon.ico"))

        app[-1].save(caminho("flutter", "assets", "icon.png"))
        print("gravado: flutter/assets/icon.png 256x256")
        shutil.copyfile(SIMBOLO, caminho("flutter", "assets", "icon.svg"))
        print("gravado: flutter/assets/icon.svg")

        altura_logo = round(LARGURA_LOGO * 110 / 640)
        png_do_svg(LOGO, caminho("flutter", "assets", "logo.png"), LARGURA_LOGO, altura_logo)
        print(f"gravado: flutter/assets/logo.png {LARGURA_LOGO}x{altura_logo}")

        rotulo = os.path.join(tmp, "rotulo.svg")
        with open(rotulo, "w", encoding="utf-8") as f:
            f.write(svg_do_rotulo())
        png_do_svg(rotulo, caminho("libs", "portable", "src", "res", "label.png"), 96, 32)
        print("gravado: libs/portable/src/res/label.png 96x32")


if __name__ == "__main__":
    main()
