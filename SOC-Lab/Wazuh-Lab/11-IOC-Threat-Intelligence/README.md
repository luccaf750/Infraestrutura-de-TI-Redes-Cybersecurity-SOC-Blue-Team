# Enriquecimento de IOC e Threat Intelligence

## Objetivo
Praticar enriquecimento de indicadores sem confundir reputação externa com prova de comprometimento.

## Ambiente
- Wazuh SIEM/XDR
- Endpoint Windows monitorado pelo Wazuh Agent
- Laboratório local, isolado e autorizado
- Finalidade: treinamento SOC / Blue Team e portfólio técnico

## Cenário
Um indicador proveniente de evidência do laboratório é selecionado e contextualizado usando fontes públicas de threat intelligence.

## Eventos e telemetria
Use um IP, domínio ou hash realmente observado e apropriado para consulta. Não invente um IOC para apresentar como evidência.

## MITRE ATT&CK
**Threat Intelligence / IOC Enrichment — o ATT&CK depende da atividade associada ao indicador.**

> O mapeamento ATT&CK deve permanecer associado ao comportamento realmente observado. A presença de uma técnica não significa, por si só, comprometimento.

## Execução / procedimento
1. Escolha um indicador real observado em um laboratório.
2. Registre tipo e origem do IOC.
3. Consulte fontes públicas apropriadas (por exemplo, reputação de IP/domínio/hash).
4. Compare múltiplas fontes quando possível.
5. Registre data da consulta, reputação, contexto e limitações.
6. Não envie arquivos confidenciais para serviços públicos.

## Resultado esperado
Produzir um enriquecimento contextualizado e uma decisão analítica, sem tratar score de reputação isolado como veredito.

## Roteiro de investigação
1. Confirmar o endpoint e a janela temporal.
2. Identificar o evento/alerta que iniciou a análise.
3. Examinar usuário, host, origem, processo/comando e demais campos disponíveis.
4. Buscar eventos imediatamente anteriores e posteriores.
5. Validar se existe relação entre os eventos.
6. Comparar a atividade com o cenário autorizado do laboratório.
7. Registrar fatos separadamente de hipóteses.
8. Definir severidade e classificação com base no contexto.
9. Salvar evidências reais.
10. Documentar a conclusão.

## Análise SOC
IOC pode envelhecer, ser compartilhado por múltiplos serviços ou gerar falso positivo. A decisão deve combinar reputação, contexto interno, prevalência, timeline e comportamento.

## Registro técnico

| Campo | Resultado |
|---|---|
| IOC | [SELECIONAR DE EVIDÊNCIA REAL] |
| Tipo | [IP/DOMÍNIO/HASH] |
| Classificação | [APÓS ENRIQUECIMENTO] |

## Critérios de escalonamento
Em ambiente corporativo, considerar escalonamento quando houver, conforme o cenário:
- atividade sem mudança/ticket autorizado;
- conta privilegiada ou ativo crítico;
- origem inesperada;
- execução ou persistência sem justificativa;
- múltiplos eventos correlacionados aumentando a confiança;
- evidência de impacto, propagação ou comprometimento;
- necessidade de contenção além da atribuição do SOC L1.

## Contenção e remediação
A resposta deve ser proporcional ao caso e seguir procedimentos organizacionais. Possíveis ações incluem validar a mudança com o proprietário do ativo, preservar evidências, desabilitar/restringir contas quando autorizado, remover mecanismos não autorizados, isolar endpoint quando necessário e escalar para resposta a incidentes. **Não executar contenção destrutiva no laboratório apenas para produzir evidência.**

## Evidências para o GitHub
Adicionar somente evidências reais e sanitizadas à pasta `evidencias/`.

Sugestão:
- `01-execucao.png`
- `02-alerta-wazuh.png`
- `03-campos-relevantes.png`
- `04-correlacao.png`
- `05-resultado-final.png`

Não publicar senhas, tokens, dados pessoais, IP público sensível ou informação confidencial.

## Conclusão
O resultado deve explicar não apenas o que uma fonte externa informou, mas como essa informação altera — ou não — a avaliação do incidente.

## Competências demonstradas
- Wazuh SIEM
- Windows Event Logs
- Triagem de alertas
- Correlação e construção de contexto
- MITRE ATT&CK
- Documentação de investigação
- Fundamentos de resposta a incidentes
- SOC / Blue Team

---
**Observação de integridade:** campos marcados como `[COLETAR]`, `[VALIDAR]` ou equivalentes dependem da execução real e não devem ser substituídos por dados presumidos.
