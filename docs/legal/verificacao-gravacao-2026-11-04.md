# Verificação: gravação de sessão pelo técnico

Data: 04/11/2026. Projeto MAPDESK-MT. Feito com a skill `legal-br`. Decisão do Manfred em 04/11/2026: manter o recurso, sem gravação automática, e só gravar com combinado prévio por escrito, trocando a frase da página de privacidade.

**Premissa.** A LGPD se aplica porque a tela do atendimento pode mostrar dados de pessoas, e a gravação guarda esses dados no computador do técnico.

**Fonte.** `fontes/leis/03-lgpd`, na biblioteca da `legal-br`, marcada EM DIA no relatório de 02/11/2026.

**FATO LEGAL.** LGPD, art. 8º, § 4º: "O consentimento deverá referir-se a finalidades determinadas, e as autorizações genéricas para o tratamento de dados pessoais serão nulas." Art. 8º, § 2º: "Cabe ao controlador o ônus da prova de que o consentimento foi obtido em conformidade com o disposto nesta Lei." O art. 9º pede informação clara sobre a finalidade específica, a forma e a duração do tratamento. O art. 7º lista o consentimento como uma das hipóteses, ao lado de outras, como a execução de contrato (inciso V).

**FATO, pela leitura do código.** A gravação pedida pelo técnico fica no computador dele. A permissão "Habilitar gravação da sessão" pode ser desligada do lado atendido e vem ligada. O programa tem também a opção "Automatically record incoming sessions", que grava no computador atendido e, em `src/server/video_service.rs`, não consulta aquela permissão. Pelo teste do Manfred de 04/11/2026, as configurações ficam bloqueadas durante o acesso remoto, então essa opção se liga no próprio computador. Decisão do Manfred em 05/11/2026: travar como desligada essa opção do computador atendido, em `src/mt_config.rs`, e manter a gravação iniciada pelo técnico. Até 05/11/2026, nada disso tinha sido testado em execução com gravação. Nota de 06/11/2026: no teste do Manfred de 05/11/2026, numa máquina que ele não informou, a caixa dessa opção aceitou o clique e ficou marcada na tela, e ele relatou que a sessão recebida não foi gravada. Pela leitura do código, a caixa deveria recusar o clique, e a causa não foi encontrada. Decisão do Manfred em 06/11/2026: publicar assim, com a página dizendo o que acontece, e corrigir a caixa na `1.5.0-mt.2`. Não foi conferido se a pessoa atendida vê aviso de gravação. A gravação automática aparece desmarcada no print da estação de 04/11/2026, e as outras máquinas não foram conferidas.

**INTERPRETAÇÃO.** Uma finalidade como "gravar este processo para o curso interno da empresa X" é determinada, e "gravar para melhorar o atendimento" fica genérica. O aceite da empresa não resolve sozinho o caso do funcionário dela, nem o de terceiros que apareçam na tela.

**Segundo uso, pedido pelo Manfred em 04/11/2026.** Gravar para guardar o registro do que o técnico fez a pedido do cliente, como instalar um programa ou apagar um arquivo. A regra é a mesma: combinado prévio por escrito. INTERPRETAÇÃO: "registro do serviço pedido" é finalidade determinada, e o combinado pode ser uma mensagem ou uma cláusula do contrato, desde que diga isso, quem assiste e o prazo de guarda. Consentimento pode não ser a melhor base aqui, porque a pessoa pode retirá-lo. Execução de contrato e exercício regular de direitos são candidatas, e a escolha fica para o advogado.

**RECOMENDAÇÃO.** Gravar com dados fictícios ou só as telas necessárias, editar o vídeo antes de entregar e combinar por escrito a finalidade, quem pode assistir e por quanto tempo o vídeo fica guardado.

**REVISÃO PROFISSIONAL.** A base legal da gravação para curso e o caso do funcionário que aparece na tela ficam para o advogado. O modelo do combinado ainda não existe, e nenhuma gravação de atendimento sai antes dele.

**O que esta verificação não cobriu.** Direito de imagem e direito autoral do material gravado, nem uso do vídeo fora da empresa atendida.

Autor: Manfred Heil Junior
