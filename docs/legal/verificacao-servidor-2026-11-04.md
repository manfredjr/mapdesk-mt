# Verificação: o que a página diz sobre o servidor

Data: 04/11/2026. Projeto MAPDESK-MT. Feito com a skill `legal-br`. Base: conferência do VPS-MT de 04/11/2026, só com leitura, e o painel da HostGator.

**Premissa.** A LGPD se aplica porque ID e IP de computador podem identificar pessoas, e a MT é controladora desses registros (`verificacao-privacidade-cliente-2026-10-05.md`, item 4.4).

**FATO, pelo VPS-MT.** O `hbbs` grava ID, IP e horário no cadastro e na troca de IP. O `hbbr` grava IP, horário e identificador da sessão, sem o ID, só nas sessões por repasse. A guarda tem teto de 6 meses, que ainda não foi visto na prática. Os registros do `hbbs` trazem também o UUID e a chave pública da máquina. O banco em produção, lido em 04/11/2026 sem ver valores, guarda ID, UUID, chave pública, data do cadastro e último IP, com os campos de usuário, situação e nota vazios. Não há limpeza no cron nem no systemd, e o código do ramo `master` do `hbbs` não tem DELETE, o que não cobre a versão 1.1.16 instalada. O banco tem 3 dias. Sobre tela e conteúdo, nada gravado no que foi lido: o compose não tem opção para isso, e a pasta de dados tem 280 KB, com banco e chaves. O código não foi auditado e os pacotes não foram analisados. O suporte da HostGator tem acesso de administrador. Não há resposta da HostGator sobre a origem dos acessos (chamado 2783814).

**FATO, pelo painel.** IP 143.95.168.101, em São Paulo, Brasil.

**FATO LEGAL.** LGPD, art. 15, I e III: o tratamento termina quando os dados "deixaram de ser necessários" e na "comunicação do titular". Art. 16: "Os dados pessoais serão eliminados após o término de seu tratamento". Art. 9º, II: o titular tem direito à informação sobre "forma e duração do tratamento". Biblioteca da `legal-br`, LGPD EM DIA no relatório de 02/11/2026.

**INTERPRETAÇÃO.** A página diz o que acontece com o banco: sem exclusão automática, e com exclusão a pedido, que atende ao término por comunicação do titular (art. 15, III). Isso obriga a MT a apagar o registro quando receber o pedido, e hoje isso é trabalho manual no servidor. O art. 15, I, encerra o tratamento também quando o dado deixa de ser necessário, sem depender de pedido, e nada apaga o registro de quem parou de usar. A limpeza por inatividade fica como pendência no VPS-MT. O acesso do suporte fica declarado na página, com a origem indicada como ainda em conferência, porque o VPS-MT só deduz a origem pelos nomes das chaves, e não há fonte para dizer que há ou que não há transferência internacional.

**RISCO.** Médio na transferência internacional, até a resposta da HostGator, e médio na guarda sem prazo do banco, até a limpeza por inatividade. As frases da página informam e não resolvem.

**REVISÃO PROFISSIONAL.** Se o suporte acessar do exterior, a base da transferência (LGPD, art. 33) fica para o advogado.

**O que esta verificação não cobriu.** O teste cronometrado G5, os contratos da HostGator, o acesso de empresas da infraestrutura, como a Oracle Cloud citada em `VPS-MT/docs/contratacao-hostgator.md`, o resto do disco e os dados que o servidor guarda além dos lidos pelo VPS-MT.

Autor: Manfred Heil Junior
