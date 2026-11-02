# Pendências do MapDesk-MT

| Item | Motivo | O que fecha |
|---|---|---|
| Cessão do autor para a MT | A titularidade das mudanças da MT exige documento escrito do autor para a empresa (Lei nº 9.610/1998, arts. 49 e 50). A licença do projeto continua AGPL-3.0 | Cessão única de todos os produtos, assinada antes da tag da primeira versão, que continua bloqueada sem ela (decisão do Manfred em 02/11/2026). Conferir se o projeto está no Anexo I da minuta |
| Mac, Linux, Android, iOS | Fora da versão 1 (briefing, seção 6) | Nova spec por plataforma |
| Cliente web | Fora da versão 1; a porta 21118/21119 fica fechada no servidor | Decisão de abrir o cliente web no VPS-MT |
| Atualização automática própria | Fora da versão 1; o MapDesk-MT não consulta versão no RustDesk | Spec própria, com servidor de atualização da MT |
| Recursos do RustDesk Server Pro | Fora da versão 1; `register-device` = "N" desliga `--assign` e `--deploy` | Decisão de contratar o Server Pro |
| Pendências jurídicas 1 a 6 | Ver `docs/superpowers/specs/2026-10-05-mapdesk-mt-versao-1-design.md`, seção 13. Decisão do Manfred em 02/11/2026: a primeira versão sai sem esperar as respostas do advogado, com o risco assumido por ele e a consulta enviada em paralelo | Buscas no INPI pelo Manfred e resposta do advogado. As questões continuam abertas, mas não bloqueiam a primeira versão |
| Página da política de privacidade no ar | Endereço definido em 02/11/2026: `https://mapdesk.manfred.com.br/privacidade.html`, gravado em `kMtPrivacidade` (`flutter/lib/mt/mt_info.dart`). A tela Sobre passa a mostrar o link, e a página mora em `public/privacidade.html` | Publicação do site, conforme `docs/publicacao.md`, seção "Site do produto" |
| Teste do 2FA com o nome novo | O nome que aparece no aplicativo autenticador mudou para MapDesk-MT na fatia 3 | Teste do Manfred com um aplicativo autenticador nas máquinas Windows |
| Certificado de assinatura (fatia 4) | Adiado pelo Manfred em 05/10/2026: nenhum certificado será comprado por enquanto. A spec dizia que nenhum cliente recebe executável sem assinatura; o Manfred reviu essa regra em 01/11/2026, e a primeira versão sai sem certificado (registrado em 02/11/2026) | Decisão do Manfred de comprar (preferência: Certum Padrão em nuvem). A conferência da assinatura na publicação só vale depois do certificado |
