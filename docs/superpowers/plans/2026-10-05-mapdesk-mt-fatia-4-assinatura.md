# MapDesk-MT, fatia 4 (assinatura): plano

> **Situação:** preparado em 05/10/2026, à espera da escolha e da compra do certificado pelo Manfred. Nada aqui roda enquanto os segredos não existirem.

**Objetivo:** o `MapDesk-MT.exe` distribuído e os arquivos que ele instala saem assinados com o certificado da MANFRED TECNOLOGIA LTDA. Assim o Windows mostra o editor certo, e o SmartScreen passa a juntar reputação para o programa.

**Base:** pesquisa em `.superpowers/rascunho/assinatura-opcoes-2026-10-05.md` (fontes oficiais, 05/10/2026). Ela tem três conclusões:
- a chave do certificado fica em nuvem ou token, então no GitHub Actions só serve assinatura em nuvem;
- o EV não dá mais reputação imediata;
- o Artifact Signing da Microsoft não aceita empresa do Brasil.

## Decisões

1. **Escolha do Manfred (05/10/2026): Certum Padrão em nuvem (SimplySign).** A SSL.com com eSigner fica como reserva. A Certum não tem ação oficial para o GitHub Actions. Há dois caminhos, e o primeiro passo da fatia é decidir entre eles, olhando o código:
   - **`ssign`** (crate Rust, licença MIT, mantenedor Le-Syl21, projeto pequeno, consultado em docs.rs em 05/10/2026). Assina por HTTPS, sem o SimplySign Desktop, com implementação própria de Authenticode. Usa `CERTUM_EMAIL` e `CERTUM_OTP` (semente TOTP em base32). Como ele manuseia a credencial de assinatura, só entra depois de revisar o código e com versão fixada (`cargo install ssign --version <x> --locked`).
   - **SimplySign Desktop e `signtool`** no runner Windows, com login automatizado pelo TOTP. As ferramentas são as oficiais da Certum, mas a automação do login é de terceiros e mais frágil.
   A semente TOTP é uma credencial de longa duração: quem a tiver, junto com o e-mail, assina como a MT até o QR do SimplySign ser emitido de novo.
2. São assinados dois grupos, como faz o RustDesk oficial:
   - antes de empacotar, os arquivos da pasta `./rustdesk`: `MapDesk-MT.exe`, `librustdesk.dll` e as demais `.dll` da MT/RustDesk, porque são eles que ficam instalados no cliente;
   - depois de empacotar, o `SaidaMT/MapDesk-MT.exe`, que é o que o cliente baixa.
3. Os passos de assinatura só rodam quando os segredos existem. Sem eles, o build continua saindo sem assinatura, como hoje.
4. Segredos (criados pelo Manfred, nunca colados no chat) ficam num **ambiente protegido do GitHub** chamado `assinatura`, com o Manfred como aprovador obrigatório, e não como segredo comum do repositório. Na Certum com `ssign`, são `CERTUM_EMAIL` e `CERTUM_OTP`. Na SSL.com, seriam `ES_USERNAME`, `ES_PASSWORD`, `CREDENTIAL_ID` e `ES_TOTP_SECRET`.
5. Com a Certum, a assinatura roda **só no build de tag** (publicação), num job separado que usa o ambiente `assinatura`. O GitHub pede a aprovação do Manfred antes de liberar os segredos. Os artefatos de PR continuam sem assinatura.

## Tarefas

### Tarefa 1: passos no workflow

Arquivo: `.github/workflows/mapdesk-windows.yml`.

- **Com a Certum**, a estrutura muda: um job novo `assinar`, com `needs: build-windows-x64`, `if: startsWith(github.ref, 'refs/tags/')` e `environment: assinatura`. Ele baixa o artefato, assina e só então publica a versão. O passo de release sai do job de build e vai para esse job. A pasta `./rustdesk` precisa ir no artefato (ou ser assinada no job de build antes do empacotamento, por um passo condicionado à tag que use o mesmo ambiente). Decidir isso na implementação, lendo o `ssign`.
- **Com a SSL.com (reserva):** no `env` do job, `ES_USERNAME: ${{ secrets.ES_USERNAME }}`, e depois "Download RustDeskTempTopMostWindow artifacts" e antes de "Build self-extracted executable", um passo "Sign files" com `if: env.ES_USERNAME != ''`:
  - `uses: sslcom/esigner-codesign@v1.3.2`;
  - `command: batch_sign`;
  - `dir_path` e `output_path` ajustados para assinar no lugar os `.exe` e `.dll` de `./rustdesk`. Conferir no README da ação se `batch_sign` aceita filtro de extensão. Se não aceitar, assinar um a um com `sign` e `override: true`;
  - `malware_block: false` (com `batch_sign`, ver o aviso do README sobre `malware_block`);
  - `environment_name: PROD`.
- Depois de "Build self-extracted executable", um passo "Sign installer", com o mesmo `if:`, que assina `./SaidaMT/MapDesk-MT.exe` com `command: sign` e `override: true`.
- Um passo "Verify signature" com o mesmo `if:`, em PowerShell: `Get-AuthenticodeSignature ./SaidaMT/MapDesk-MT.exe` e `./rustdesk/MapDesk-MT.exe`. Falha se `Status` não for `Valid` e mostra o `SignerCertificate.Subject`.
- [ ] Commit `Assina o MapDesk-MT no GitHub Actions`.

### Tarefa 2: teste 6 da spec

- [ ] Abrir o PR. Conferir no log que os dois passos de assinatura rodaram e que a verificação mostra a MT como editor.
- [ ] O Manfred baixa o artefato num Windows limpo e confere:
  - Propriedades e depois Assinaturas digitais: MANFRED TECNOLOGIA LTDA;
  - o SmartScreen, que ainda pode avisar enquanto não houver reputação;
  - o Windows Defender (o arquivo não pode ser bloqueado).
- [ ] Se o Defender bloquear, mandar o arquivo para análise da Microsoft como falso positivo (o Manfred faz, pelo portal de envio de amostras da Microsoft).

## Fora desta fatia

- Renovar o certificado: com validade máxima de 460 dias, registrar a data de vencimento em `docs/superpowers/pendencias.md` quando ele for emitido.
- Assinar o MSI: não geramos MSI na versão 1.
