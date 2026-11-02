# Aviso de modificação

O MapDesk-MT é uma obra derivada do RustDesk. A origem é o repositório `rustdesk/rustdesk`, na tag `1.5.0`, distribuído sob a AGPL-3.0.

Este programa foi modificado pela MT - Manfred Tecnologia. A licença continua a AGPL-3.0, e o arquivo `LICENCE` da raiz continua valendo para o código inteiro, inclusive para as mudanças da MT. Os avisos de copyright do RustDesk ficam como estão.

## Mudanças da MT

| Data | Mudança | Arquivos |
|---|---|---|
| 05/10/2026 | Regras, documentos e ganchos do git da MT | `AGENTS-MT.md`, `README-MT.md`, `.githooks/`, `.gitignore`, `docs/legal/`, `docs/superpowers/` |
| 05/10/2026 | Submódulo `libs/hbb_common` apontando para o fork `manfredjr/hbb_common`, no mesmo commit do oficial | `.gitmodules` |
| 05/10/2026 | Compilação do Windows x64 no GitHub Actions | `.github/workflows/mapdesk-windows.yml` |
| 05/10/2026 | Configuração própria do MapDesk-MT, definida em tempo de execução | `src/mt_config.rs`, `src/lib.rs`, `src/common.rs` |
| 05/10/2026 | Marca do MapDesk-MT nos ícones e imagens | `flutter/assets/`, `flutter/windows/runner/resources/app_icon.ico`, `res/icon.ico`, `res/tray-icon.ico`, `libs/portable/src/res/label.png`, `docs/marca/`, `ferramentas-mt/gerar-marca.py` |
| 05/10/2026 | Nome do executável e metadados do Windows | `flutter/windows/runner/Runner.rc`, `libs/portable/Cargo.toml`, `.github/workflows/mapdesk-windows.yml` |
| 05/10/2026 | Tema verde da MT e nome do programa nos textos fixos | `flutter/lib/common.dart`, `flutter/lib/desktop/pages/server_page.dart`, `flutter/lib/desktop/widgets/tabbar_widget.dart`, `src/auth_2fa.rs` |
| 05/10/2026 | Tela Sobre com a versão, a origem, a licença e o link do código-fonte | `flutter/lib/mt/mt_info.dart`, `flutter/lib/desktop/pages/desktop_setting_page.dart`, `AVISO-DE-MODIFICACAO.md` |
| 05/10/2026 | Link da licença no instalador e a dica dele | `flutter/lib/desktop/pages/install_page.dart` |
| 05/10/2026 | Teste de rede e arquivo de instruções da raiz que carrega as regras da MT | `ferramentas-mt/teste-rede.ps1`, arquivos de instruções da raiz |
| 06/10/2026 | Logo da MT com link para o site, no painel esquerdo da tela principal e na tela Sobre | `flutter/assets/mt-logo.png`, `flutter/lib/mt/mt_logo_link.dart`, `flutter/lib/mt/mt_info.dart`, `flutter/lib/desktop/pages/desktop_home_page.dart`, `flutter/lib/desktop/pages/desktop_setting_page.dart`, `.gitignore` |
| 06/10/2026 | Ajustes nos ícones e no gerador da marca | `flutter/assets/`, `flutter/windows/runner/resources/app_icon.ico`, `res/icon.ico`, `res/tray-icon.ico`, `ferramentas-mt/gerar-marca.py` |
| 06/10/2026 | Chave pública do servidor de laboratório, para teste | `src/mt_config.rs` |
| 28/10/2026 | Gancho de conferência antes do commit | `.githooks/pre-commit` |
| 01/11/2026 | Chave pública do servidor de produção no lugar da de laboratório | `src/mt_config.rs` |
| 01/11/2026 | Ganchos de autoria e de conferência do commit | `.githooks/commit-msg` |
| 01/11/2026 | Página do produto, teste da página e publicação pelo cPanel | `public/`, `.cpanel.yml`, `.gitignore`, `ferramentas-mt/testar-site.py`, `.github/workflows/mapdesk-site.yml` |
| 01/11/2026 | SHA-256 e notas publicados junto da versão | `.github/workflows/mapdesk-windows.yml`, `docs/notas-versao.md` |
| 02/11/2026 | Bloco do MapDesk-MT no topo do README | `README.md` |
| 02/11/2026 | Link da página de privacidade na tela Sobre | `flutter/lib/mt/mt_info.dart` |
| 02/11/2026 | Versão sem impressora remota: o driver e o adaptador saem do pacote, e as opções da impressora somem das configurações e do instalador | `.github/workflows/mapdesk-windows.yml`, `src/mt_config.rs`, `flutter/lib/desktop/pages/install_page.dart` |

## Componentes de terceiros

O monitor virtual usa o `usbmmidd_v2`, da Amyuni Technologies Inc. (https://www.amyuni.com), distribuído com a licença dela. O programa não é da MT, vai no pacote sem código-fonte, e o arquivo `License.txt` o acompanha, na pasta `usbmmidd_v2`. O pacote sai sem a pasta `Win32`, os `deviceinstaller` e o `usbmmidd.bat`, e os demais arquivos não foram alterados. O `idd_instructions.txt`, da Amyuni, ainda cita o `.bat` retirado.

## Nomes e logotipos

Conforme a seção 7 da AGPL-3.0, a licença não dá direito de uso dos nomes "MapDesk-MT" e "MT - Manfred Tecnologia" nem dos logotipos da MT.

## Código-fonte de cada versão

Cada versão distribuída tem uma tag no formato `<versão>-mt.<n>`, por exemplo `1.5.0-mt.1`, em https://github.com/manfredjr/mapdesk-mt. O código correspondente ao executável de cada versão está na tag com o mesmo número, salvo os componentes de terceiros citados acima.
