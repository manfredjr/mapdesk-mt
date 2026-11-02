# Avaliação do Virtual-Display-Driver como troca do usbmmidd_v2

Data: 02/11/2026. Só leitura: nada foi instalado nem executado.

## Conferido

- Repositório https://github.com/VirtualDrivers/Virtual-Display-Driver, LICENSE MIT. Último commit lido: 22/06/2026. Última versão estável: 25.7.23, de 23/07/2025 (https://github.com/VirtualDrivers/Virtual-Display-Driver/releases/tag/25.7.23), consulta em 02/11/2026.
- Pacote `VirtualDisplayDriver-x86.Driver.Only.zip` (o inf é NTamd64), SHA-256 `e24210692b442b39af763536330ce78b423f19342b7a7792c26de3944e418b3a`, 132 KB.
- `mttvdd.cat` e `MttVDD.dll` com Authenticode válido, assinante SignPath Foundation, certificado até 07/09/2027. Sem assinatura da Microsoft, ao contrário do usbmmidd_v2.
- Hardware ID `Root\MttVDD`. Provedor "MikeTheTech". Configuração em `C:\VirtualDisplayDriver\vdd_settings.xml` ou no caminho do registro `HKLM\SOFTWARE\MikeTheTech\VirtualDisplayDriver`. Controle por pipe `MTTVirtualDisplayPipe`, com `RELOAD_DRIVER`, e quantidade de monitores no XML.
- O `Driver.cpp` do ramo `master` abre com "Copyright (c) Microsoft Corporation": deriva do exemplo da Microsoft, repositório com MS-PL. A lista da FSF (consulta em 02/11/2026) diz que a MIT (Expat) é compatível com a GPL e a Ms-PL é "incompatible with the GNU GPL". Não trata da AGPL nesses trechos.
- O README avisa de conflito com atualização grande de driver de vídeo, com tela preta possível na inicialização.
- `src/virtual_display_manager.rs` e outros arquivos de `src/`, `flutter/` e `res/` citam a implementação da Amyuni. A troca pede um módulo novo, porque hoje o controle é por IOCTL e `usbmmidd`.

## Não conferido

- Se o binário da versão 25.7.23 foi compilado desse código, e o zip não traz arquivo de licença.
- Se o Windows instala sem aviso. Sem assinatura da Microsoft, pode pedir confirmação, e numa máquina sem monitor ninguém responderia.
- Funcionamento em máquina sem monitor, no Windows 10 e no 11, e com Secure Boot.
- Permissão do pipe, acesso à rede pelo driver e pacotes de terceiros no build.
- Aplicação da AGPL ao driver como "aggregate": código público ajuda, mas segue leitura jurídica.
- O pacote `VDD.Control`: só foi lido o pacote do driver.

Autor: Manfred Heil Junior
