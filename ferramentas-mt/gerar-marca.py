"""Gera os icones e imagens da marca MapDesk-MT a partir das PNG de docs/marca/.

Uso, na raiz do repositorio: python ferramentas-mt/gerar-marca.py

Para trocar a arte, substitua as duas PNG em docs/marca/ (simbolo 1024x1024 e
logo largo, ambos com fundo transparente) e rode de novo. Cada tamanho sai da
PNG grande, reduzido com LANCZOS; os tamanhos pequenos (ate 32 px) recebem um
leve realce de nitidez. Os .ico saem em DIB de 32 bits com mascara AND, o
formato classico do Windows. Precisa so do Pillow.
"""

import base64
import io
import os
import struct

from PIL import Image, ImageDraw, ImageFilter, ImageFont

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SIMBOLO = os.path.join(RAIZ, "docs", "marca", "mapdesk-mt-simbolo.png")
LOGO = os.path.join(RAIZ, "docs", "marca", "mapdesk-mt-logo.png")
FONTES = [r"C:\Windows\Fonts\Montserrat-Bold.ttf", r"C:\Windows\Fonts\arialbd.ttf"]

TAMANHOS_APP = [16, 24, 32, 48, 64, 128, 256]
TAMANHOS_BANDEJA = [16, 20, 24, 32, 40, 48]
# O loadLogo() do Flutter limita o logo a 300x60 e reduz com BoxFit.contain.
# Como o logo e largo, a largura manda: 600 px e o dobro de 300 e fica nitido
# em telas com escala de 200%.
LARGURA_LOGO = 600


def caminho(*partes):
    return os.path.join(RAIZ, *partes)


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


LIMITE_NITIDEZ = 32
# Ate este tamanho a margem transparente da arte e cortada antes de reduzir:
# na bandeja e na barra de tarefas cada pixel conta.
LIMITE_SEM_MARGEM = 48


def sem_margem(imagem):
    caixa = imagem.getbbox()
    recorte = imagem.crop(caixa)
    lado = max(recorte.size)
    quadrado = Image.new("RGBA", (lado, lado), (0, 0, 0, 0))
    quadrado.paste(recorte, ((lado - recorte.width) // 2, (lado - recorte.height) // 2))
    return quadrado


def reduzir(imagem, lado):
    if lado <= LIMITE_SEM_MARGEM:
        imagem = sem_margem(imagem)
    saida = imagem.resize((lado, lado), Image.LANCZOS)
    if lado <= LIMITE_NITIDEZ:
        saida = saida.filter(ImageFilter.UnsharpMask(radius=0.6, percent=60, threshold=0))
    return saida


def rotulo(simbolo):
    """Rotulo da tela do executavel portatil: simbolo claro e texto branco.

    O fundo da janela e azul acinzentado escuro, entao o monitor vira branco e
    o cursor usa o verde claro de apoio.
    """
    recorte = simbolo.crop(simbolo.getbbox()).resize((26, 24), Image.LANCZOS)
    pixels = recorte.load()
    for y in range(recorte.height):
        for x in range(recorte.width):
            r, g, b, a = pixels[x, y]
            t = min(1.0, max(0.0, (g - 107) / (170 - 107)))
            pixels[x, y] = (
                round(255 + (0x9A - 255) * t),
                round(255 + (0xD5 - 255) * t),
                round(255 + (0x2B - 255) * t),
                a,
            )
    tela = Image.new("RGBA", (96, 32), (0, 0, 0, 0))
    tela.alpha_composite(recorte, (2, 4))
    fonte = None
    for caminho_fonte in FONTES:
        if os.path.exists(caminho_fonte):
            fonte = ImageFont.truetype(caminho_fonte, 15)
            break
    if fonte is None:
        raise SystemExit("nem Montserrat nem Arial Bold encontradas")
    texto = "MapDesk-MT"
    while fonte.getlength(texto) > 66 and fonte.size > 8:
        fonte = fonte.font_variant(size=fonte.size - 1)
    ImageDraw.Draw(tela).text((30, 16), texto, font=fonte, fill=(255, 255, 255, 255), anchor="lm")
    return tela


def svg_do_icone(png256):
    buf = io.BytesIO()
    png256.save(buf, "PNG")
    dados = base64.b64encode(buf.getvalue()).decode("ascii")
    return (
        '<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" '
        'width="256" height="256" viewBox="0 0 256 256">'
        f'<image width="256" height="256" href="data:image/png;base64,{dados}"/></svg>\n'
    )


def main():
    simbolo = Image.open(SIMBOLO).convert("RGBA")
    logo = Image.open(LOGO).convert("RGBA")

    app = [reduzir(simbolo, l) for l in TAMANHOS_APP]
    for destino in (
        caminho("flutter", "windows", "runner", "resources", "app_icon.ico"),
        caminho("res", "icon.ico"),
        caminho("flutter", "assets", "icon.ico"),
    ):
        gravar_ico(app, destino)
    gravar_ico([reduzir(simbolo, l) for l in TAMANHOS_BANDEJA], caminho("res", "tray-icon.ico"))

    app[-1].save(caminho("flutter", "assets", "icon.png"))
    print("gravado: flutter/assets/icon.png 256x256")
    with open(caminho("flutter", "assets", "icon.svg"), "w", encoding="utf-8", newline="\n") as f:
        f.write(svg_do_icone(app[-1]))
    print("gravado: flutter/assets/icon.svg")

    altura_logo = round(LARGURA_LOGO * logo.height / logo.width)
    logo.resize((LARGURA_LOGO, altura_logo), Image.LANCZOS).save(caminho("flutter", "assets", "logo.png"))
    print(f"gravado: flutter/assets/logo.png {LARGURA_LOGO}x{altura_logo}")

    rotulo(simbolo).save(caminho("libs", "portable", "src", "res", "label.png"))
    print("gravado: libs/portable/src/res/label.png 96x32")


if __name__ == "__main__":
    main()
