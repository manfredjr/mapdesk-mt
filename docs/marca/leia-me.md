# Marca do MapDesk-MT

A arte final foi recebida do Manfred em 05/10/2026. Ela foi feita a partir do briefing da marca, com fundo transparente. Esta pasta guarda as duas PNG que servem de fonte para todos os ícones e imagens do projeto.

## Arquivos

| Arquivo | Uso |
|---|---|
| `mapdesk-mt-simbolo.png` | Símbolo (monitor com cursor), 1024x1024. Fonte dos ícones. |
| `mapdesk-mt-logo.png` | Logotipo horizontal "MapDesk - MT", 2000x341. Fonte do `logo.png`. |

## Cores

| Cor | Uso |
|---|---|
| `#006B2D` | Verde escuro (monitor, "MapDesk") |
| `#46AA2C` | Verde claro (cursor, "- MT"), valor aproximado lido da arte |
| `#9AD52B` | Verde de apoio, usado no cursor do rótulo do instalador portátil |

Fonte do logotipo: Montserrat Bold. O texto já está dentro da PNG, então a fonte não precisa estar instalada para usar a arte.

## O que o roteiro gera

| Saída | Tamanhos |
|---|---|
| `flutter/windows/runner/resources/app_icon.ico`, `res/icon.ico`, `flutter/assets/icon.ico` | 16, 24, 32, 48, 64, 128, 256 |
| `res/tray-icon.ico` | 16, 20, 24, 32, 40, 48 |
| `flutter/assets/icon.png` | 256x256 |
| `flutter/assets/icon.svg` | SVG simples que embute o `icon.png` (reserva do `loadIcon`) |
| `flutter/assets/logo.png` | 600x102, fundo transparente |
| `libs/portable/src/res/label.png` | 96x32, monitor branco, cursor `#9AD52B` e texto "MapDesk-MT" em branco |

Cada tamanho é reduzido da PNG grande com LANCZOS. Do 16 ao 32 px entra um leve realce de nitidez. O texto do rótulo usa Montserrat Bold se ela estiver instalada, senão Arial Bold.

## Como gerar de novo

Troque as duas PNG desta pasta e rode, na raiz do repositório:

```
python ferramentas-mt/gerar-marca.py
```

Precisa só do Python com Pillow.
