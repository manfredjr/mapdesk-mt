# Verificação jurídica: licenças dos binários de terceiros do build

Data da consulta: 02/11/2026. Projeto MAPDESK-MT. Feita com a skill `legal-br`.

Objeto: o que o workflow `.github/workflows/mapdesk-windows.yml` baixa ou compila de terceiros para montar o `MapDesk-MT.exe`, item do portão antes da tag (`docs/publicacao.md`, seção "Site do produto").

**Resultado:** dois pacotes que entram no executável ficaram sem licença localizada, o driver de monitor virtual e os pacotes do driver de impressora. Os dois estão marcados com `[FONTE?]`. Enquanto isso não se resolver, a conferência não fecha para esses itens. Os demais têm licença localizada, com os avisos e as ressalvas das seções 3 e 4.

## 1. Contexto e premissas

| Premissa | O que aciona | Fundamento |
|---|---|---|
| A MT transmite (convey) o executável a quem baixa | AGPL-3.0, seções 5 e 6 | Já tratada em `verificacao-licenca-agpl-e-marcas-2026-10-05.md`, item 1.2 |
| O executável leva software de terceiros dentro do pacote | A licença de cada componente, e a Lei nº 9.610/1998 quando não há licença | O passo "Build rustdesk" copia os arquivos para `./rustdesk`, e o `libs/portable/generate.py` empacota essa pasta |
| Há uso de programa de computador no Brasil | Lei nº 9.609/1998, art. 2º | "O regime de proteção à propriedade intelectual de programa de computador é o conferido às obras literárias pela legislação de direitos autorais e conexos vigentes no País, observado o disposto nesta Lei." |

Relação de consumo, dados pessoais e menores não entram nesta verificação: o assunto é só a licença de cada componente.

## 2. Fontes consultadas em 02/11/2026

| Fonte | Endereço | Observação |
|---|---|---|
| AGPL-3.0, cópia do repositório | arquivo `LICENCE`, seções 1, 5, 6 e 13 | Comparada com o texto oficial em 05/10/2026 (verificação anterior, item 1.3) |
| Lei nº 9.609/1998, arts. 2º e 12 | https://www.planalto.gov.br/ccivil_03/leis/l9609.htm | Conferida online |
| Lei nº 9.610/1998, art. 29, VI | https://www.planalto.gov.br/ccivil_03/leis/l9610.htm | Conferida online |
| Versão `usbmmidd_v2` | https://api.github.com/repos/rustdesk-org/rdev/releases/tags/usbmmidd_v2 | Corpo da versão vazio |
| Licença do repositório `rdev` | https://api.github.com/repos/rustdesk-org/rdev/license | MIT |
| Versão `driver` do `hbb_common` | https://api.github.com/repos/rustdesk/hbb_common/releases/tags/driver | Corpo da versão vazio |
| Licença do repositório `hbb_common` | https://api.github.com/repos/rustdesk/hbb_common/license | 404 |
| Versão `main` e licença do `rustdesk/engine` | https://github.com/rustdesk/engine/releases/tag/main e https://raw.githubusercontent.com/rustdesk/engine/main/LICENSE | Texto BSD, 3 cláusulas no formato |
| Flutter 3.24.5 | https://raw.githubusercontent.com/flutter/flutter/3.24.5/LICENSE | Texto BSD, 3 cláusulas no formato |
| `RustDeskTempTopMostWindow`, commit fixado | https://github.com/rustdesk-org/RustDeskTempTopMostWindow/tree/ecd8d6a139eee76845ea66423fb739af450fda90 (`LICENSE` e `README.md`) | MIT, "Copyright (c) 2022 fufesou"; o README diz que deriva do MobileShell |
| MobileShell | https://api.github.com/repos/ADeltaX/MobileShell/license | MIT |
| FFmpeg n7.1.1 | https://raw.githubusercontent.com/FFmpeg/FFmpeg/n7.1.1/LICENSE.md e https://ffmpeg.org/legal.html | Ver item 3.5 |
| Portas do vcpkg da MT | `res/vcpkg/*/vcpkg.json` e `res/vcpkg/ffmpeg/portfile.cmake` deste repositório | Campo `license` declarado pela porta |
| Portas do vcpkg oficial, commit da linha de base | https://github.com/microsoft/vcpkg/tree/9e593bb18ea69cc5095e012465dcd675a822ed0d/ports (`libjpeg-turbo`, `ffnvcodec`, `amd-amf`) | Campo `license` declarado pela porta |
| libyuv, commit fixado | https://chromium.googlesource.com/libyuv/libyuv/+/0faf8dd0e004520a61a603a4d2996d5ecc80dc3f/LICENSE | Só o início do arquivo foi lido: copyright dos autores do LibYuv e texto de redistribuição |
| nv-codec-headers n12.1.14.0 | https://raw.githubusercontent.com/FFmpeg/nv-codec-headers/n12.1.14.0/include/ffnvcodec/nvEncodeAPI.h | Aviso da NVIDIA no cabeçalho, com texto de permissão no formato MIT |
| AMF v1.4.35 | https://raw.githubusercontent.com/GPUOpen-LibrariesAndSDKs/AMF/v1.4.35/LICENSE.txt | Permissão no formato MIT e aviso sobre padrões |
| `hwcodec`, commit do `Cargo.lock` | https://github.com/rustdesk-org/hwcodec/tree/778df1f99597722473b29443bac22ae6c23946fe | Ver item 3.7 |

A biblioteca da `legal-br` (clone de 02/11/2026) não tem `STATUS-FONTES.md`. Por isso as duas leis foram conferidas no Planalto.

**O que esta verificação não cobriu:**

- Os pacotes `.zip` não foram baixados nem abertos, porque baixar depende de autorização do Manfred. Se algum deles traz um arquivo de licença dentro, ele não foi lido.
- As licenças das dependências de código (crates do Cargo e pacotes do `pub`) ficaram de fora. O objeto aqui são os binários e as bibliotecas nativas do build. Só o `hwcodec` entrou, porque traz os codecs.
- Os avisos de terceiros que o próprio Flutter possa embutir no pacote não foram conferidos no executável.

## 3. O que entra no executável

| # | Componente | De onde vem | Licença localizada | Conferência |
|---|---|---|---|---|
| 1 | `usbmmidd_v2.zip`, driver de monitor virtual | https://github.com/rustdesk-org/rdev/releases/download/usbmmidd_v2/usbmmidd_v2.zip | `[FONTE?]` | Sem SHA-256 no workflow |
| 2 | `rustdesk_printer_driver_v4-1.4.zip`, driver de impressora | https://github.com/rustdesk/hbb_common/releases/download/driver/rustdesk_printer_driver_v4-1.4.zip | `[FONTE?]` | SHA-256 de `sha256sums`, da mesma versão |
| 3 | `printer_driver_adapter.zip`, adaptador | https://github.com/rustdesk/hbb_common/releases/download/driver/printer_driver_adapter.zip | `[FONTE?]` | SHA-256 de `sha256sums`, da mesma versão |
| 4 | `windows-x64-release.zip`, engine do Flutter modificada pelo RustDesk | https://github.com/rustdesk/engine/releases/download/main/windows-x64-release.zip | BSD, 3 cláusulas no formato | Sem SHA-256 no workflow |
| 5 | Flutter 3.24.5, framework | `subosito/flutter-action`, com o patch `.github/patches/flutter_3.24.4_dropdown_menu_enableFilter.diff` | BSD, 3 cláusulas no formato | Versão fixa |
| 6 | `WindowInjection.dll`, do `RustDeskTempTopMostWindow` | Compilada do código, no commit `ecd8d6a` | MIT (fufesou), derivado de MobileShell, MIT | Commit fixo |
| 7 | FFmpeg 7.1.1, ligação estática | `res/vcpkg/ffmpeg`, com `--enable-gpl` no Windows | GPL v2 ou posterior nesta compilação | Tag `n7.1.1` |
| 8 | aom 3.14.1 | `res/vcpkg/aom` | BSD-2-Clause, declarada pela porta | Commit fixo |
| 9 | libvpx 1.15.2 | `res/vcpkg/libvpx` | BSD-3-Clause, declarada pela porta | Tag fixa |
| 10 | opus 1.5.2 | `res/vcpkg/opus` | BSD-3-Clause, declarada pela porta | Tag fixa |
| 11 | mfx-dispatch 1.35.1 | `res/vcpkg/mfx-dispatch` | BSD-3-Clause, declarada pela porta | Tag fixa |
| 12 | libyuv 1857 | `res/vcpkg/libyuv`; a porta traz `license: null` | Texto do repositório, início lido; tipo exato `[FONTE?]` | Commit fixo |
| 13 | libjpeg-turbo 3.2.0 | vcpkg oficial | BSD-3-Clause, declarada pela porta | Linha de base fixa |
| 14 | nv-codec-headers 12.1.14.0 (`ffnvcodec`) | Sobrescrita no `vcpkg.json` | Formato MIT, no cabeçalho lido | Versão fixa |
| 15 | AMF 1.4.35 (`amd-amf`) | Sobrescrita no `vcpkg.json` | Formato MIT | Versão fixa |
| 16 | `hwcodec`, commit `778df1f` | Dependência git do Cargo | `[FONTE?]` | Commit fixo no `Cargo.lock` |

Usados só na compilação, sem entrar no pacote como programa próprio (INTERPRETAÇÃO, pela leitura do workflow): vcpkg, LLVM 15.0.6, `flutter_rust_bridge_codegen`, `cargo-expand`, `brotli` do `pip` e as actions do GitHub. Suas licenças não foram consultadas (`[FONTE?]`) porque não mudam o que a MT distribui. O Rust 1.75 também compila, mas a biblioteca padrão entra no executável, e a licença dela também está `[FONTE?]`.

### 3.1. Driver de monitor virtual (`usbmmidd_v2`)

**FATO.** A versão no repositório `rustdesk-org/rdev` foi publicada em 20/07/2024, tem corpo vazio e um único arquivo de 199.309 bytes. O repositório é MIT, mas o arquivo da versão não está na árvore do código. O código do MapDesk-MT chama essa implementação de `amyuni_idd`, com o nome de dispositivo "USB Mobile Monitor Virtual Display" (`src/virtual_display_manager.rs`, linhas 7 e 11). Catálogos de drivers listam "Amyuni USB Mobile Monitor" (https://treexy.com/products/driver-fusion/database/display-adapters/amyuni/usb-mobile-monitor-mirror/).

Duas buscas na internet em 02/11/2026 não acharam os termos desse driver no site da Amyuni. Os contratos da Amyuni que apareceram tratam dos produtos de PDF e não citam esse driver.

**INTERPRETAÇÃO.** O autor provável é a Amyuni, não o RustDesk. A MIT do `rdev` não prova permissão para este binário, e os contratos de PDF não servem de base. Licença: `[FONTE?]`.

**RISCO.** Alto até haver fonte. Sem licença, vale a regra geral: "Depende de autorização prévia e expressa do autor a utilização da obra", inclusive "a distribuição" (Lei nº 9.610/1998, art. 29, VI). A Lei nº 9.609/1998, art. 12, tipifica "Violar direitos de autor de programa de computador". O fato de o RustDesk distribuir o mesmo arquivo não transfere a permissão à MT, se ela existir.

### 3.2. Driver de impressora e adaptador

**FATO.** Os dois estão na versão `driver` do `rustdesk/hbb_common`, com corpo vazio. A API do GitHub não acha licença nesse repositório (404), e a verificação de 05/10/2026 já registrava a falta de arquivo de licença. O código-fonte desses pacotes não foi localizado. O programa carrega o adaptador pelo nome `printer_driver_adapter` (`src/server/printer_service.rs`, linha 11).

**INTERPRETAÇÃO.** A origem aponta para os autores do RustDesk, mas isso não diz sob qual licença os pacotes saem. Se o adaptador for parte da obra, ele cai na AGPL-3.0 e precisa de código correspondente, porque a seção 1 inclui "the source code for shared libraries and dynamically linked subprograms that the work is specifically designed to require". O driver instalado à parte pode ser um "aggregate" da seção 5, mas essa leitura depende de ver o pacote. Licença: `[FONTE?]`.

**RISCO.** Médio a alto. Além da permissão de distribuir, a MT pode não conseguir oferecer o código correspondente do adaptador, que é obrigação dela pela seção 6.

### 3.3. Engine do Flutter

**FATO.** O arquivo vem da versão `main` do `rustdesk/engine`, fork da engine do Flutter, com licença BSD. O arquivo foi atualizado em 01/12/2024, a API não traz SHA-256 dele, e o workflow também não confere.

**INTERPRETAÇÃO.** A licença não preocupa. O problema é rastrear: o nome da versão não fixa um commit, e nada liga o arquivo baixado a um estado do código. Isso dificulta dizer qual é o código correspondente a cada executável (AGPL-3.0, seções 1 e 6).

**RISCO.** Baixo na licença e médio na oferta de código-fonte. Sem conferência de hash, o arquivo pode mudar entre duas compilações sem aviso.

### 3.4. Flutter e `WindowInjection.dll`

**FATO.** As licenças BSD e MIT permitem redistribuir, com condição. A do Flutter diz: "Redistributions in binary form must reproduce the above copyright notice". A MIT pede o aviso em todas as cópias.

**RISCO.** Baixo, ver o item 4.

### 3.5. FFmpeg

**FATO.** O `portfile.cmake` passa `--enable-gpl` no Windows (linha 133). O `LICENSE.md` do FFmpeg diz que, nesse caso, "FFmpeg's license changes to GPL v2+". A opção `--enable-nonfree` não é passada: o arquivo só cita "nonfree" ao identificar a licença resultante (linha 707). O `hwcodec` é o caminho provável de uso, e essa ligação não foi verificada no binário.

**INTERPRETAÇÃO.** A GPL v2 ou posterior permite adotar a versão 3, e a seção 13 da AGPL-3.0 autoriza combinar com "a work licensed under version 3 of the GNU General Public License". O resultado é compatível, e a compilação com GPL não fecha nenhuma porta num programa que já é AGPL. O checklist da página do FFmpeg que manda compilar sem `--enable-gpl` é para quem quer ficar na LGPL, o que não é o caso aqui.

**RISCO.** Baixo na compatibilidade. Fica a obrigação de oferecer o código e como foi compilado: a tag da MT traz a porta e os patches, mas o código do FFmpeg fica no repositório de origem. A seção 6(d) admite outro servidor com "clear directions next to the object code", e a página de notas da versão ainda não diz isso (`docs/notas-versao.md`).

### 3.6. Patentes de codecs

**FATO.** O programa habilita H.264 e HEVC no FFmpeg. A licença do AMF avisa que a AMD não dá licença de direitos sobre padrões, citando AVC/H.264 e HEVC/H.265, e que eventuais royalties são de quem usa. A página do FFmpeg diz, sobre patentes, "We do not know, we are not lawyers".

**INTERPRETAÇÃO.** A licença de direito autoral não resolve patente. Esta verificação não examinou a existência de patente válida no Brasil nem a incidência de royalties sobre o caso da MT.

**RISCO.** Não medido. É pendência de validação, não achado.

### 3.7. `hwcodec`

**FATO.** No commit `778df1f`, a raiz não tem arquivo de licença, e o `Cargo.toml` não tem campo `license`. A API também não acha licença no submódulo `rustdesk-org/externals` (404). O projeto compila com `--hwcodec`.

**INTERPRETAÇÃO.** É o mesmo quadro do `hbb_common`, tratado na questão 2 da consulta ao advogado. A diferença é que aqui a MT distribui o código compilado, mesmo sem alterá-lo. Licença: `[FONTE?]`.

**RISCO.** Médio.

## 4. Requisitos para a versão

- [ ] Decidir o destino de `usbmmidd_v2`: achar os termos, pedir permissão por escrito à Amyuni ou tirar do build.
- [ ] Decidir o destino do driver de impressora e do adaptador: achar a licença e o código com o RustDesk ou tirar do build.
- [ ] Abrir os três `.zip` e a engine, com autorização para baixar, e procurar arquivo de licença.
- [ ] Criar um arquivo de avisos de terceiros que acompanhe o programa, com os textos de licença dos itens 4 a 15. Hoje o repositório não tem esse arquivo. Conferir antes se o pacote do Flutter já traz parte deles.
- [ ] Gravar nas notas da versão onde está o código do FFmpeg e das demais bibliotecas compiladas, com a forma de compilação.
- [ ] Fixar o SHA-256 de `usbmmidd_v2.zip` e de `windows-x64-release.zip` no workflow, se ficarem no build.
- [ ] Inventariar as licenças das crates e dos pacotes `pub`, que ficaram fora desta verificação.

## 5. Pendências de validação para o advogado externo

Estas perguntas ainda não entraram em `CONSULTA-ADVOGADO-mapdesk-agpl-marca-2026-10-05.md`.

1. **Componente sem licença localizada.** A MT pode distribuir `usbmmidd_v2`, o driver de impressora, o adaptador e o `hwcodec` sem licença expressa, pelo fato de virem no build oficial de um programa AGPL? Leituras possíveis: (a) não pode sem autorização, o que é o risco maior; (b) no caso dos autores do RustDesk, a seção 5(c) da AGPL cobre as partes da obra, o que não alcança um terceiro como a Amyuni. Impacto: tirar os componentes do build ou mantê-los. Urgência: antes da primeira tag.
2. **Driver como "aggregate".** Um driver instalado à parte pelo programa conta como "aggregate" (seção 5) ou como parte da obra? Impacto: dever de oferecer o código do driver. Urgência: antes da primeira tag, se o driver ficar.
3. **Patentes de H.264 e HEVC.** A distribuição gratuita pela MT, no Brasil, gera obrigação de licença ou de royalties? Impacto: manter ou desligar esses codecs. Urgência: antes da primeira tag.

## 6. Decisão necessária

Para o Manfred: manter, trocar ou retirar os dois drivers do build da primeira versão. A retirada mexe no workflow e tira os recursos de monitor virtual e de impressora remota, e esse efeito precisa de teste. Nada foi alterado no build por esta verificação.
