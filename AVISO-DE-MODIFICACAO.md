# Aviso de modificação

O MapDesk-MT é uma obra derivada do RustDesk. A origem é o repositório `rustdesk/rustdesk`, na tag `1.5.0`, distribuído sob a AGPL-3.0.

Este programa foi modificado pela MT - Manfred Tecnologia. A licença continua a AGPL-3.0, e o arquivo `LICENCE` da raiz continua valendo para o código inteiro, inclusive para as mudanças da MT. Os avisos de copyright do RustDesk ficam como estão.

## Mudanças da MT

| Data | Mudança | Arquivos |
|---|---|---|
| 05/10/2026 | Regras, documentos e ganchos do git da MT | `AGENTS-MT.md`, `CLAUDE.md`, `README-MT.md`, `.githooks/`, `.gitignore`, `docs/legal/`, `docs/superpowers/` |
| 05/10/2026 | Submódulo `libs/hbb_common` apontando para o fork `manfredjr/hbb_common`, no mesmo commit do oficial | `.gitmodules` |
| 05/10/2026 | Compilação do Windows x64 no GitHub Actions | `.github/workflows/mapdesk-windows.yml` |
| 05/10/2026 | Configuração própria do MapDesk-MT, definida em tempo de execução | `src/mt_config.rs`, `src/lib.rs`, `src/common.rs` |
| 05/10/2026 | Marca do MapDesk-MT nos ícones e imagens | `flutter/assets/`, `flutter/windows/runner/resources/app_icon.ico`, `res/icon.ico`, `res/tray-icon.ico`, `libs/portable/src/res/label.png`, `docs/marca/`, `ferramentas-mt/gerar-marca.py` |
| 05/10/2026 | Nome do executável e metadados do Windows | `flutter/windows/runner/Runner.rc`, `.github/workflows/mapdesk-windows.yml` |
| 05/10/2026 | Tema verde da MT e nome do programa nos textos fixos | `flutter/lib/common.dart`, `flutter/lib/desktop/pages/server_page.dart`, `flutter/lib/desktop/widgets/tabbar_widget.dart`, `src/auth_2fa.rs` |
| 05/10/2026 | Tela Sobre com a versão, a origem, a licença e o link do código-fonte | `flutter/lib/mt/mt_info.dart`, `flutter/lib/desktop/pages/desktop_setting_page.dart`, `AVISO-DE-MODIFICACAO.md` |

## Nomes e logotipos

Conforme a seção 7 da AGPL-3.0, a licença não dá direito de uso dos nomes "MapDesk-MT" e "MT - Manfred Tecnologia" nem dos logotipos da MT.

## Código-fonte de cada versão

Cada versão distribuída tem uma tag no formato `<versão>-mt.<n>`, por exemplo `1.5.0-mt.1`, em https://github.com/manfredjr/mapdesk-mt. O código correspondente ao executável de cada versão está na tag com o mesmo número.
