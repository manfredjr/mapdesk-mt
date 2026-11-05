# Verificação: o que a página diz sobre o servidor

Data: 04/11/2026. Projeto MAPDESK-MT. Feito com a skill `legal-br`. Base: conferência do VPS-MT de 04/11/2026, só com leitura, e o painel da HostGator.

**Premissa.** A LGPD se aplica porque ID e IP de computador podem identificar pessoas, e a MT é controladora desses registros (`verificacao-privacidade-cliente-2026-10-05.md`, item 4.4).

**FATO, pelo VPS-MT.** O `hbbs` grava ID, IP e horário no cadastro e na troca de IP. O `hbbr` grava IP, horário e identificador da sessão, sem o ID, só nas sessões por repasse. A guarda tem teto de 6 meses, que ainda não foi visto na prática. O banco guarda ID e último IP sem prazo (leitura no laboratório, sem nova leitura em produção). O suporte da HostGator tem acesso de administrador. Não há resposta da HostGator sobre a origem dos acessos (chamado 2783814).

**FATO, pelo painel.** IP 143.95.168.101, em São Paulo, Brasil.

**FATO LEGAL.** LGPD, art. 15, I e III: o tratamento termina quando os dados "deixaram de ser necessários" e na "comunicação do titular". Art. 16: "Os dados pessoais serão eliminados após o término de seu tratamento". Art. 9º, II: o titular tem direito à informação sobre "forma e duração do tratamento". Biblioteca da `legal-br`, LGPD EM DIA no relatório de 02/11/2026.

**INTERPRETAÇÃO.** Para o banco, "enquanto o computador usar o serviço" descreve a duração, e o pedido de exclusão pelo canal atende ao término por comunicação do titular. Isso obriga a MT a apagar o registro quando receber o pedido, e hoje isso é trabalho manual no servidor. O acesso do suporte fica declarado na página, com a origem indicada como ainda em conferência, porque não há fonte para dizer que há ou que não há transferência internacional.

**RISCO.** Médio na transferência internacional, até a resposta da HostGator. A frase da página informa a dúvida e não a resolve.

**REVISÃO PROFISSIONAL.** Se o suporte acessar do exterior, a base da transferência (LGPD, art. 33) fica para o advogado.

**O que esta verificação não cobriu.** O teste cronometrado G5, os contratos da HostGator e os dados que o servidor guarda além dos lidos pelo VPS-MT.

Autor: Manfred Heil Junior
