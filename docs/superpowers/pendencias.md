# Pendências do MapDesk-MT

| Item | Motivo | O que fecha |
|---|---|---|
| Cessão do autor para a MT | A titularidade das mudanças da MT exige documento escrito do autor para a empresa (Lei nº 9.610/1998, arts. 49 e 50). A licença do projeto continua AGPL-3.0 | Cessão única de todos os produtos, assinada antes da primeira distribuição. Conferir se o projeto está no Anexo I da minuta |
| Mac, Linux, Android, iOS | Fora da versão 1 (briefing, seção 6) | Nova spec por plataforma |
| Cliente web | Fora da versão 1; a porta 21118/21119 fica fechada no servidor | Decisão de abrir o cliente web no VPS-MT |
| Atualização automática própria | Fora da versão 1; o MapDesk-MT não consulta versão no RustDesk | Spec própria, com servidor de atualização da MT |
| Recursos do RustDesk Server Pro | Fora da versão 1; `register-device` = "N" desliga `--assign` e `--deploy` | Decisão de contratar o Server Pro |
| Pendências jurídicas 1 a 6 | Ver `docs/superpowers/specs/2026-10-05-mapdesk-mt-versao-1-design.md`, seção 13 | Buscas no INPI pelo Manfred e resposta do advogado antes da fatia 5 |
| Endereço da política de privacidade | A página fica no projeto site-mt e ainda não existe. `kMtPrivacidade` em `flutter/lib/mt/mt_info.dart` está vazio, e o link fica escondido na tela Sobre | Endereço definido pelo site-mt, gravado em `kMtPrivacidade` |
| Teste do 2FA com o nome novo | O nome que aparece no aplicativo autenticador mudou para MapDesk-MT na fatia 3 | Teste do Manfred com um aplicativo autenticador nas máquinas Windows |
