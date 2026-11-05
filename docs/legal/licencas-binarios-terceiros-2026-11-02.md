# Verificação jurídica: licenças dos binários de terceiros do build

Data da consulta: 02/11/2026. Projeto MAPDESK-MT. Feita com a skill `legal-br`.

Objeto: o que o workflow `.github/workflows/mapdesk-windows.yml` baixa ou compila de terceiros para montar o `MapDesk-MT.exe`, item do portão antes da tag (`docs/publicacao.md`, seção "Site do produto").

**Correção de 02/11/2026:** esta verificação foi feita sem abrir os pacotes, e a conclusão sobre o monitor virtual estava errada. O pacote traz a licença da Amyuni. A análise atual está em `verificacao-drivers-2026-11-02.md`.

**Decisões do Manfred em 02/11/2026:** o driver de impressora e o adaptador saem do build, e a primeira versão vai sem impressora remota. Eles só voltam com licença e código, e os itens 2 e 3 da tabela ficam como registro. O `usbmmidd_v2` fica, com o crédito à Amyuni. A licença não diz "redistribuir", e ele decidiu não pedir autorização à Amyuni e assumir a dúvida da permissão e a do código.

**Resultado:** a conferência não fecha. Ficaram sem licença localizada, marcados com `[FONTE?]`, o driver de impressora e o adaptador, o `hwcodec` e a biblioteca padrão do Rust. A `libyuv` tem texto de licença, mas o tipo exato não foi fechado, e o pacote `flutter_gpu_texture_renderer` volta `NOASSERTION` na API do GitHub. Os demais têm licença localizada, com os avisos e as ressalvas das seções 3 e 4.

**Atualização de 04/11/2026:** a biblioteca padrão do Rust e a `libyuv` têm o texto em `AVISOS-DE-TERCEIROS.md`, e o `[FONTE?]` acima fica como registro de 02/11/2026.

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
| Pacotes do item 17 | https://api.github.com/repos/ seguido do dono e do nome em `flutter/pubspec.yaml`, campo `license` | Consulta de 02/11/2026 |

As duas leis foram conferidas no Planalto. Correção: o clone da `legal-br` usado aqui não tinha `STATUS-FONTES.md`, mas a cópia instalada tem, gerado em 02/11/2026, e as duas leis estão EM DIA nele.

**O que esta verificação não cobriu:**

- Os pacotes `.zip` não foram baixados nem abertos, porque baixar depende de autorização do Manfred. Se algum deles traz um arquivo de licença dentro, ele não foi lido.
- As licenças das dependências de código (crates do Cargo e pacotes do `pub`) ficaram de fora, salvo o `hwcodec`, que traz os codecs, e os pacotes vindos do git (item 17). O objeto aqui são os binários e as bibliotecas nativas do build.
- Os avisos de terceiros que o próprio Flutter possa embutir no pacote não foram conferidos no executável.

## 3. O que entra no executável

| # | Componente | De onde vem | Licença localizada | Conferência |
|---|---|---|---|---|
| 1 | `usbmmidd_v2.zip`, driver de monitor virtual | https://github.com/rustdesk-org/rdev/releases/download/usbmmidd_v2/usbmmidd_v2.zip | Licença da Amyuni, em `License.txt` dentro do pacote | SHA-256 fixo no workflow |
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
| 17 | Pacotes de `flutter/pubspec.yaml` vindos do git: `Dash-Chat-2`, `window_manager`, `rustdesk_desktop_multi_window`, `flutter_custom_cursor`, `flutter-desktop-embedding`, `uni_links`, `flutter_texture_rgba_renderer`, `flutter_gpu_texture_renderer`, `dynamic_layouts` | Dependência git do `pub` | Pela API do GitHub: MIT nos dois primeiros, Apache-2.0 em `rustdesk_desktop_multi_window`, `flutter_custom_cursor`, `flutter-desktop-embedding` e `flutter_texture_rgba_renderer`, BSD-2-Clause em `uni_links`, BSD-3-Clause em `dynamic_layouts`. `flutter_gpu_texture_renderer`: `NOASSERTION`, ou seja, `[FONTE?]` | Licença lida no ramo padrão, não na referência fixada. `window_size` vem de subpasta de `flutter-desktop-embedding`. Quais têm parte nativa ou geram DLL não foi conferido |

Usados só na compilação, sem entrar no pacote como programa próprio (INTERPRETAÇÃO, pela leitura do workflow): vcpkg, LLVM 15.0.6, `flutter_rust_bridge_codegen`, `cargo-expand`, `brotli` do `pip` e as actions do GitHub. Suas licenças não foram consultadas (`[FONTE?]`) porque não mudam o que a MT distribui. O Rust 1.75 também compila, mas a biblioteca padrão entra no executável, e a licença dela também está `[FONTE?]`.

### 3.1. Driver de monitor virtual (`usbmmidd_v2`)

**FATO.** A versão no repositório `rustdesk-org/rdev` foi publicada em 20/07/2024, tem corpo vazio e um único arquivo de 199.309 bytes. O repositório é MIT, mas o arquivo da versão não está na árvore do código. O código do MapDesk-MT chama essa implementação de `amyuni_idd`, com o nome de dispositivo "USB Mobile Monitor Virtual Display" (`src/virtual_display_manager.rs`, linhas 7 e 11). Catálogos de drivers listam "Amyuni USB Mobile Monitor" (https://treexy.com/products/driver-fusion/database/display-adapters/amyuni/usb-mobile-monitor-mirror/).

Duas buscas na internet em 02/11/2026 não acharam os termos desse driver no site da Amyuni. Os contratos da Amyuni que apareceram tratam dos produtos de PDF e não citam esse driver.

**INTERPRETAÇÃO, corrigida em 02/11/2026.** A autora é a Amyuni, não o RustDesk. A MIT do `rdev` não prova permissão para este binário, e os contratos de PDF não servem de base. O `License.txt` do pacote, que não tinha sido aberto, permite usar e não diz "redistribuir" (`verificacao-drivers-2026-11-02.md`).

**RISCO, corrigido em 02/11/2026.** Médio, assumido pelo Manfred, conforme a seção 6. A leitura anterior, sem o arquivo aberto, era de risco alto. Vale a regra geral para o que a licença não autoriza: "Depende de autorização prévia e expressa do autor a utilização da obra", inclusive "a distribuição, quando não intrínseca ao contrato firmado pelo autor com terceiros para uso ou exploração da obra" (Lei nº 9.610/1998, art. 29, VI). A Lei nº 9.609/1998, art. 12, tipifica "Violar direitos de autor de programa de computador". O fato de o RustDesk distribuir o mesmo arquivo não transfere à MT uma permissão que ele tenha.

### 3.2. Driver de impressora e adaptador

**FATO.** Os dois estão na versão `driver` do `rustdesk/hbb_common`, com corpo vazio. Até a retirada de 02/11/2026, o passo do workflow ficava dentro de um `try/catch` e ignorava falha de download ou de SHA-256, então um executável podia sair com ou sem esses arquivos. A API do GitHub não acha licença nesse repositório (404), e a verificação de 05/10/2026 já registrava a falta de arquivo de licença. O código-fonte desses pacotes não foi localizado. O programa carrega o adaptador pelo nome `printer_driver_adapter` (`src/server/printer_service.rs`, linha 11).

**INTERPRETAÇÃO.** A origem aponta para os autores do RustDesk, mas isso não diz sob qual licença os pacotes saem. Se o adaptador for parte da obra, ele cai na AGPL-3.0 e precisa de código correspondente, porque a seção 1 inclui "the source code for shared libraries and dynamically linked subprograms that the work is specifically designed to require, such as by intimate data communication or control flow between those subprograms and other parts of the work". O driver instalado à parte pode ser um "aggregate" da seção 5, mas o pacote aberto não traz licença nem resolve essa leitura. Licença: `[FONTE?]`.

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

**INTERPRETAÇÃO.** É o mesmo quadro do `hbb_common`, tratado na questão 2 da consulta ao advogado. A questão 2 olha para a alteração do `hbb_common`. Ela não responde se a MT pode distribuir compilados esses dois componentes sem alterá-los, e isso vale para ambos (questão 6 do complemento à consulta). Licença do `hwcodec`: `[FONTE?]`.

**RISCO.** Médio. Decisão do Manfred em 04/11/2026: manter o `hwcodec`, o `hbb_common` e o `flutter_gpu_texture_renderer` e assumir a dúvida até a resposta do advogado à questão 6. A decisão registra quem assume o risco e não dá licença nenhuma.

## 4. Requisitos para a versão

- [x] Decidir o destino de `usbmmidd_v2`: fica no build, por decisão do Manfred em 02/11/2026.
- [x] Achar os termos do `usbmmidd_v2`: `License.txt` do pacote.
- [x] Decidir a permissão de distribuir o `usbmmidd_v2` e o dever de código: dúvidas assumidas pelo Manfred em 02/11/2026, sem pedido à Amyuni.
- [x] Decidir o destino do driver de impressora e do adaptador: fora do build, por decisão do Manfred em 02/11/2026.
- [x] Abrir os três `.zip`: `verificacao-drivers-2026-11-02.md`.
- [ ] Abrir a engine e procurar arquivo de licença.
- [ ] Parcial em 04/11/2026, em `AVISOS-DE-TERCEIROS.md`, sem a engine, os avisos internos do Flutter, as crates e os pacotes `pub`. Criar um arquivo de avisos de terceiros que acompanhe o programa, com os textos de licença dos itens 1, 4 a 15 e 17, inclusive o aviso e o arquivo NOTICE que a Apache-2.0 pedir. Conferir antes se o pacote do Flutter já traz parte deles.
- [x] Gravar nas notas da versão onde está o código do FFmpeg e das demais bibliotecas compiladas, com a forma de compilação.
- [x] Fixar o SHA-256 de `usbmmidd_v2.zip` no workflow.
- [ ] Fixar o SHA-256 de `windows-x64-release.zip` no workflow.
- [ ] Inventariar as licenças das crates e dos pacotes `pub`, que ficaram fora desta verificação.

## 5. Pendências de validação para o advogado externo

Estas perguntas estão em `CONSULTA-ADVOGADO-complemento-2026-11-02.md`, questões 6 a 8.

1. **Componente sem licença localizada.** A MT pode distribuir o driver de impressora, o adaptador, o `hwcodec`, o `flutter_gpu_texture_renderer` e o `hbb_common` compilado sem licença expressa, pelo fato de virem no build oficial de um programa AGPL? Leituras possíveis: (a) não pode sem autorização, o que é o risco maior; (b) no caso dos autores do RustDesk, a seção 5(c) da AGPL cobre as partes da obra, o que não alcança um terceiro. Impacto: tirar os componentes do build ou mantê-los. Urgência: não segura a tag, por decisão do Manfred em 04/11/2026, para o `hwcodec`, o `flutter_gpu_texture_renderer` e o `hbb_common`; para o driver de impressora e o adaptador, só se voltarem ao build.
2. **Driver como "aggregate" e licença da Amyuni.** Um driver instalado à parte pelo programa conta como "aggregate" (seção 5) ou como parte da obra? A licença da Amyuni, que permite usar e não diz "redistribuir", autoriza a MT a distribuir o `usbmmidd_v2`? Impacto: dever de oferecer o código do driver e permanência dele no build. Urgência: não segura a tag, por decisão do Manfred em 02/11/2026.
3. **Patentes de H.264 e HEVC.** A distribuição gratuita pela MT, no Brasil, gera obrigação de licença ou de royalties? Impacto: manter ou desligar esses codecs. Urgência: não segura a tag, por decisão do Manfred em 04/11/2026.

## 6. Decisão

Decidido pelo Manfred em 02/11/2026, depois do parecer de `verificacao-drivers-2026-11-02.md`: retirar do build da primeira versão o driver de impressora e o adaptador, e manter o `usbmmidd_v2` com o crédito à Amyuni. Sobre o pedido à Amyuni, ele disse: "Eles nem vão me responder isso, eu só vou perder tempo. Tá? Se não tem nada lá dentro, seguimos como está a questão do Rust Desk, da mesma forma." Depois, com os riscos explicados, escolheu a opção "Publicar com o driver da Amyuni, com você assumindo a dúvida da permissão e a do código, e deixar a troca para a `1.5.0-mt.2`". Pela leitura do código, sem o adaptador o programa registra o erro uma vez e não cria o serviço da impressora, e a instalação do driver falha sem interromper a instalação do programa. Esse efeito precisa do teste do Manfred, junto com a conexão em máquina sem monitor ligado.
