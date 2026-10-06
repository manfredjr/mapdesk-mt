# MapDesk-MT, fatia 2 (servidor embutido): plano de implementação

> **Para quem executa:** usar `superpowers:subagent-driven-development`. Passos com caixas (`- [ ]`).

**Objetivo:** o MapDesk-MT abre e já se liga ao servidor da MT (`rustdesk.manfred.com.br`) com a chave pública do laboratório, sem nenhuma configuração manual. O técnico não vê nem muda o servidor. Um roteiro de teste de rede mostra que nada vai para `*.rustdesk.com`.

**Spec:** `docs/superpowers/specs/2026-10-05-mapdesk-mt-versao-1-design.md`, seções 4 e 10. Esta fatia sai do ramo `marca` (fatia 3), porque o `src/mt_config.rs` nasceu lá.

## Decisões (05/10/2026)

1. O ramo `servidor` sai de `marca`. O PR só abre depois que a chave do laboratório chegar e o PR #2 for juntado; aí a base passa a ser `mt`.
2. A chave fica numa constante (`CHAVE_PUBLICA`) em `src/mt_config.rs`. Até a chave chegar, a constante fica vazia, e o teste falha de propósito (`assert!(!CHAVE_PUBLICA.is_empty())`), para nenhuma compilação sem chave passar despercebida.
3. O repasse (porta 21117) não é configurado à parte: o cliente o deriva do servidor de ID. Conferir no código do `hbb_common` (`get_relay_server` ou equivalente) e registrar.
4. `hide-server-settings = Y` em `BUILTIN_SETTINGS` esconde a linha de servidor da tela de rede.

## Restrições globais

As mesmas da fatia 3 (`docs/superpowers/plans/2026-10-05-mapdesk-mt-fatia-3-marca.md`, "Restrições globais"), com o ramo `servidor`.

---

### Tarefa 1: servidor, chave e configurações escondidas

**Arquivos:** `src/mt_config.rs`.

| Tabela | Chave | Valor |
|---|---|---|
| `OVERWRITE_SETTINGS` | `custom-rendezvous-server` (`keys::OPTION_CUSTOM_RENDEZVOUS_SERVER`) | `rustdesk.manfred.com.br` |
| `OVERWRITE_SETTINGS` | `key` (`keys::OPTION_KEY`) | `CHAVE_PUBLICA` |
| `BUILTIN_SETTINGS` | `hide-server-settings` (`keys::OPTION_HIDE_SERVER_SETTINGS`) | `Y` |

- [ ] O teste existente passa a conferir também:
  - `Config::get_rendezvous_server()` ou o equivalente público devolve o servidor da MT, com a porta padrão;
  - a chave em `OVERWRITE_SETTINGS` é igual a `CHAVE_PUBLICA`, e `CHAVE_PUBLICA` não é vazia;
  - `hide-server-settings` é "Y".

  Restaurar o estado no fim, como hoje.
- [ ] Commit `Embute o servidor e a chave da MT no MapDesk-MT`.

### Tarefa 2: roteiro de teste de rede

**Arquivos:** criar `ferramentas-mt/teste-rede.ps1`.

O roteiro roda em PowerShell 5.1 no Windows, sem instalar nada, e funciona assim:
- recebe a duração em segundos (padrão 120);
- a cada 2 segundos, lista as conexões TCP (`Get-NetTCPConnection`) e UDP (`Get-NetUDPEndpoint`) dos processos `MapDesk-MT` e guarda endereço remoto, porta e horário;
- no início, resolve `rs-ny.rustdesk.com`, `rs-sg.rustdesk.com`, `rs-cn.rustdesk.com`, `api.rustdesk.com`, `admin.rustdesk.com` e `rustdesk.com`, e marca qualquer conexão a esses IPs;
- no fim, lê o cache de DNS (`Get-DnsClientCache`) e lista toda entrada com "rustdesk";
- grava um relatório em texto na pasta atual e imprime um resumo: "OK: nenhuma conexão ao RustDesk" ou "ATENÇÃO", com a lista;
- textos em português, sem caracteres proibidos; comentário no topo com o modo de usar.

- [ ] Commit `Cria roteiro de teste de rede do MapDesk-MT`.

### Tarefa 3: PR e teste (depois da chave e do merge do PR #2)

- [ ] Mudar a base para `mt` e abrir o PR "Fatia 2: servidor embutido".
- [ ] No "Como testar":
  - teste 1 (duas redes, uma no 4G, aceite pelo botão verde);
  - teste 2 (repasse forçado);
  - teste de rede com o roteiro;
  - tela de rede sem a linha de servidor;
  - a dica de "servidor público" da tela de conexão sumiu.
- [ ] Ler o CI, baixar o artefato e esperar a frase do Manfred.
