# MapDesk-MT: site do produto (mapdesk.manfred.com.br)

Desenho aprovado pelo Manfred em 01/11/2026, em duas partes. Depende da spec `2026-10-05-mapdesk-mt-versao-1-design.md`.

## 1. O que é

É a página do MapDesk-MT como produto, no mesmo modelo dos irmãos da família Map (MapDisk, MapHard e MapNet). Ela fica em `https://mapdesk.manfred.com.br/` e oferece o `MapDesk-MT.exe` sem assinatura, baixado de uma versão pública do GitHub.

Há dois caminhos de acesso, e eles não se misturam (decisão do Manfred em 01/11/2026):

- **Clientes do suporte:** entram pelo Helpdesk e baixam em `manfred.com.br/acesso` o RustDesk oficial assinado, com a configuração da MT no nome do arquivo. Este site não muda isso.
- **Produto:** este site. Quando houver o certificado (fatia 4), o mesmo endereço passa a entregar o executável assinado, sem mudar a página.

Fica de fora: preços, MapHub-MT e o botão de login do catálogo de endereços, até existirem.

## 2. Arquivos

O modelo é o repositório `manfredjr/mapdisk`, lido em 01/11/2026.

| Caminho | O que é |
|---|---|
| `public/index.html` | página do produto |
| `public/privacidade.html` | privacidade do programa e do servidor da MT |
| `public/css/site.css` | estilo copiado do MapDisk, com as cores do MapDesk-MT |
| `public/imagens/` | logo do MapDesk-MT (de `docs/marca/`), logo da MT e print da janela com ID fictício |
| `public/.htaccess` | o mesmo do MapDisk, conferido linha a linha |
| `.cpanel.yml` | tarefas do "Deploy HEAD Commit", no modelo do MapDisk, com `REPO=$HOME/repositories/mapdesk-mt` |
| `.github/workflows/mapdesk-site.yml` | teste da página, separado da compilação |
| `ferramentas-mt/testar-site.py` | o teste chamado pelo workflow |

O print entra quando o Manfred mandar um; até lá, a página sai sem ele.

## 3. Seções da página

1. **Topo:** "MapDesk - MT" e uma frase sobre o acesso remoto da MT. O botão "Baixar para Windows" aponta para o arquivo da versão pela tag exata (`releases/download/<tag>/MapDesk-MT.exe`), porque a versão sai como pré-versão e o endereço `latest` não a alcança. O botão "Ver o código" leva ao código dessa tag. Embaixo, o link para o arquivo `MapDesk-MT.exe.sha256` da mesma versão (`releases/download/<tag>/MapDesk-MT.exe.sha256`). O número do SHA-256 fica fora da página até a tag sair, porque o executável só existe depois dela; a conferência do download é pelo arquivo `.sha256`.
2. **Por que ele existe:** atendimento remoto com servidor próprio da MT, no Brasil, e, por padrão, conexão só depois do aceite.
3. **O que ele faz:**
   - aceite pelo botão verde;
   - senha permanente opcional;
   - transferência de arquivos;
   - repasse quando não há conexão direta;
   - servidor travado no da MT;
   - marca da MT.
4. **Como usar:** baixar, abrir, informar o ID ao técnico e aceitar.
5. **Aviso do Windows:**
   - o SmartScreen se resolve com "Mais informações" e "Executar assim mesmo";
   - o Smart App Control não tem esse botão. Onde ele está ligado, o programa não abre até haver a assinatura. A página diz isso com franqueza.
6. **Privacidade:** o que o servidor registra (ID, IP e horário) e por quanto tempo, no mesmo texto de `manfred.com.br/acesso`. O detalhe fica em `privacidade.html`.
7. **Código aberto:**
   - obra derivada do RustDesk, sob a AGPL-3.0;
   - aviso de modificação, com a data;
   - link para o código da versão exata e para o texto da licença.
   
   A marca RustDesk aparece só como origem, nunca como argumento de venda.
8. **Uso autorizado:** usar só em computadores com autorização de quem os administra; a cláusula contra cópia e raspagem do conteúdo (regra 11, site de conteúdo). O texto passa pela `legal-br`.

Todo texto passa pela `humanizar-ptbr` antes de gravar.

## 4. O que não entra no repositório público

O repositório é público por causa da AGPL. Antes da publicação, uma varredura do repositório inteiro e do histórico procura:

- senha, token e chave privada;
- arquivo `.env`, `.pfx` ou `.p12`;
- IP interno, caminho de máquina do Manfred e dado de cliente (ID, nome de computador, e-mail que não seja o público da MT).

A chave pública e o nome do servidor (`rustdesk.manfred.com.br`) podem aparecer: não são segredo. O print da janela usa um ID fictício.

## 5. Sem medição

A página não carrega script de medição nem conteúdo de terceiros (Google Analytics, Clarity, pixel, fonte externa). Assim, nada roda antes de um aceite (regra 8).

## 6. Testes

O `ferramentas-mt/testar-site.py` roda no workflow `mapdesk-site.yml` a cada PR que mexe em `public/`, `.cpanel.yml` ou no próprio teste. Ele falha se:

1. sobrar `[PREENCHER]` ou `[FONTE?]` em `public/`;
2. aparecer `<script src=` externo, `googletagmanager`, `google-analytics`, `clarity.ms`, `facebook.net` ou `fonts.googleapis`;
3. aparecer caractere proibido (travessão longo ou médio, aspas curvas, reticências de um caractere, espaço especial);
4. o botão de baixar (`a.btn--primario`) não apontar para `https://github.com/manfredjr/mapdesk-mt/releases/download/<v>/MapDesk-MT.exe`, ou o botão do código (`a.btn--secundario`) não apontar para `tree/<v>`, com `<v>` igual a `kMtVersao` de `flutter/lib/mt/mt_info.dart`; ou aparecer `releases/latest` em `public/`;
5. faltar o link do código da versão exata, do `MapDesk-MT.exe.sha256`, da licença AGPL-3.0 ou de `privacidade.html`, sem contar links dentro de comentário HTML;
6. aparecer arquivo `.map` ou `sourceMappingURL` em `public/`, ou `<link`, `<iframe`, `@import` ou `url()` com endereço externo;
7. faltar arquivo citado pelo `.cpanel.yml` (`public/index.html` e `public/.htaccess`).

Depois do CI verde vêm o revisor-mt (Opus) e o revisor-ux (computador e celular), e só então o teste do Manfred.

## 7. Versão pública

- O workflow `mapdesk-windows.yml` publica a versão na tag `*-mt.*`. A fatia acrescenta um arquivo `MapDesk-MT.exe.sha256` aos arquivos da versão, para a página e o cliente conferirem o download.
- A primeira tag é `1.5.0-mt.1`, que ainda não existe.
- Na página da versão entram o fork do `hbb_common` com o commit do submódulo e o aviso de que o executável não tem assinatura.

## 8. Publicação

Cada passo só sai com a frase do Manfred (regras 5 e 7):

1. **Portão antes da tag,** com os itens das pendências e da spec da versão 1, que o Manfred confirma ou decide adiar por escrito:
   - cessão do autor para a MT;
   - respostas do advogado (pendências jurídicas 1 a 6);
   - página de privacidade no ar, que pode ser a `privacidade.html` deste site, gravada também em `kMtPrivacidade` numa fatia própria;
   - bloco do MapDesk-MT no `README.md` da raiz;
   - conferência das licenças dos binários de terceiros do build.
2. **Merge** do PR do site.
3. **Tag `1.5.0-mt.1`:** o Actions compila e cria a versão pública.
4. **No cPanel da GoDaddy,** pelo `roteiro-publicacao-git-cpanel.md`:
   - clonar `https://github.com/manfredjr/mapdesk-mt.git` em `repositories/mapdesk-mt`, sem chave SSH, porque o repositório é público;
   - apontar o subdomínio `mapdesk.manfred.com.br`, já criado pelo Manfred, para a pasta `public` do clone;
   - rodar "Update from Remote" e depois "Deploy HEAD Commit".
5. **No Cloudflare,** onde o domínio já foi criado pelo Manfred: bloqueio de robôs de IA no subdomínio.
6. **Conferência no ar:**
   - a página abre em HTTPS;
   - o botão baixa o arquivo certo, e o SHA-256 confere;
   - nenhum script de terceiros carrega.

## 9. Riscos aceitos

- Sem assinatura, o Smart App Control bloqueia o programa em parte das máquinas. Isso é aceito até o certificado.
- O clone do cPanel traz o código inteiro do RustDesk, com algumas centenas de megabytes, porque a página mora no mesmo repositório. A pasta publicada é só `public/`. Se o espaço da hospedagem não comportar, a alternativa é um repositório só do site, numa decisão nova.
