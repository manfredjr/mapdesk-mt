MapDesk-MT {VERSAO}, para Windows 64 bits. Página do produto: https://mapdesk.manfred.com.br/

Esta é uma versão modificada do RustDesk. A MT - Manfred Tecnologia mexe no programa desde 05/10/2026, e a lista das mudanças, com as datas, está no arquivo AVISO-DE-MODIFICACAO.md desta tag. O MapDesk-MT não é um produto oficial do RustDesk.

O programa é distribuído sob a AGPL-3.0, a mesma licença do RustDesk (arquivo LICENCE, que acompanha esta versão). O código-fonte desta versão está em https://github.com/manfredjr/mapdesk-mt/tree/{VERSAO}.

O submódulo libs/hbb_common aponta para o fork https://github.com/manfredjr/hbb_common, no commit {HBB_COMMIT}.

Esta versão não traz a impressora remota do RustDesk, porque o driver ficou de fora do pacote.

O monitor virtual usa o usbmmidd_v2, da Amyuni Technologies Inc. (https://www.amyuni.com), que vai sem código-fonte e com a licença dela, no arquivo License.txt da pasta usbmmidd_v2. A licença desse driver prevê que uma página de anúncio pode aparecer ao usar o monitor virtual. Isso não aconteceu no nosso teste, mas não há garantia de que nunca aconteça.

Os avisos dos componentes de terceiros estão no arquivo AVISOS-DE-TERCEIROS.md, que acompanha esta versão.

O FFmpeg 7.1.1 entra no programa com ligação estática, sob a GPL v2 ou posterior. O código dele está em https://github.com/FFmpeg/FFmpeg/tree/n7.1.1. A forma de compilar, com os patches, está em res/vcpkg/ffmpeg nesta tag, e os passos estão em .github/workflows/mapdesk-windows.yml. As demais bibliotecas compiladas seguem o mesmo caminho, em res/vcpkg e vcpkg.json, com a origem de cada uma em AVISOS-DE-TERCEIROS.md. A engine do Flutter vem do arquivo windows-x64-release.zip, da versão main de https://github.com/rustdesk/engine, atualizado em 01/12/2024, e o código está nesse repositório. O commit exato desse arquivo não foi conferido.

O MapDesk-MT.exe não tem assinatura digital. Na primeira vez, o SmartScreen do Windows pode pedir confirmação ("Mais informações" e depois "Executar assim mesmo"). Nos computadores com o Controle Inteligente de Aplicativos ligado, o programa não abre até ter a assinatura.

Para conferir o download, compare o SHA-256 do arquivo com o do MapDesk-MT.exe.sha256 desta versão.
