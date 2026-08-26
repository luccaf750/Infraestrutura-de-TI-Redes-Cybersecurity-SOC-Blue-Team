# Desafio Final — Analista SOC L1

## Objetivo
Validar autonomia na triagem e investigação sem fornecer antecipadamente a conclusão do caso.

## Ambiente
- Wazuh SIEM/XDR
- Endpoint Windows monitorado pelo Wazuh Agent
- Laboratório local, isolado e autorizado
- Finalidade: treinamento SOC / Blue Team e portfólio técnico

## Cenário
O analista recebe evidências selecionadas dos laboratórios e deve conduzir a investigação como um ticket de SOC L1.

## Eventos e telemetria
Não informado antecipadamente — identificar nas evidências fornecidas.

## MITRE ATT&CK
**Não informado antecipadamente — deve ser identificado durante a análise.**

> O mapeamento ATT&CK deve permanecer associado ao comportamento realmente observado. A presença de uma técnica não significa, por si só, comprometimento.

## Execução / procedimento
O desafio deve ser executado sem consultar uma resposta pronta.

Entregáveis:
1. Resumo do alerta.
2. Evidências relevantes.
3. Timeline.
4. Hipótese principal e alternativas.
5. MITRE ATT&CK.
6. Severidade.
7. Disposition.
8. Decisão: fechar, monitorar ou escalar.
9. Justificativa.
10. Recomendações.

## Resultado esperado
Demonstrar capacidade de conduzir uma investigação L1 e defender tecnicamente a decisão.

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
**Reservado para o desafio.** Não preencher antes da execução para não eliminar o valor avaliativo.

## Registro técnico

| Campo | Resultado |
|---|---|
| Status | Aguardando execução |
| Avaliação | Autonomia, precisão, correlação e documentação |

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
A conclusão será escrita somente após o desafio, comparando a decisão do analista com as evidências disponíveis.

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
