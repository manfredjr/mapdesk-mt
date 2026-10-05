# Marca do MapDesk-MT

A arte atual é provisória. O Manfred aprovou a base em 05/10/2026. A arte final deve vir com o texto do logotipo convertido em curvas, para não depender da fonte instalada.

## Arquivos

| Arquivo | Uso |
|---|---|
| `mapdesk-mt-simbolo.svg` | Símbolo (tela com cursor). Fonte dos ícones. |
| `mapdesk-mt-logo.svg` | Logotipo horizontal "MapDesk - MT". Fonte do `logo.png`. |

## Cores

| Cor | Uso |
|---|---|
| `#006B2D` | Principal escuro (moldura, base, "MapDesk") |
| `#0F8F2F` | Contorno do cursor |
| `#43A92C` | Destaque (cursor, "MT") |
| `#9AD52B` | Apoio claro |
| `#202020` | Texto |

Fonte do logotipo: Montserrat 700. Sem ela instalada, o Inkscape usa Arial.

## O que o roteiro gera

| Saída | Tamanhos |
|---|---|
| `flutter/windows/runner/resources/app_icon.ico`, `res/icon.ico`, `flutter/assets/icon.ico` | 16, 24, 32, 48, 64, 128, 256 |
| `res/tray-icon.ico` | 16, 20, 24, 32, 40, 48 |
| `flutter/assets/icon.png` | 256x256 |
| `flutter/assets/icon.svg` | cópia do símbolo |
| `flutter/assets/logo.png` | 600x103, fundo transparente |
| `libs/portable/src/res/label.png` | 96x32, símbolo claro e texto branco |

## Como gerar de novo

Troque os dois SVG desta pasta e rode, na raiz do repositório:

```
python ferramentas-mt/gerar-marca.py
```

Precisa do Python com Pillow e do Inkscape. Se o Inkscape estiver em outro caminho, defina a variável de ambiente `INKSCAPE`.
