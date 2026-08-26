# Investigação Completa de Incidente SOC

## Objetivo
Aplicar o fluxo completo de triagem, escopo, correlação, classificação, resposta e documentação.

## Ambiente
- Wazuh SIEM/XDR
- Endpoint Windows monitorado pelo Wazuh Agent
- Laboratório local, isolado e autorizado
- Finalidade: treinamento SOC / Blue Team e portfólio técnico

## Cenário
Um caso é montado exclusivamente com evidências reais produzidas nos laboratórios anteriores.

## Eventos e telemetria
Selecionar eventos reais já coletados.

## MITRE ATT&CK
**Definido pelas técnicas efetivamente presentes no caso.**

> O mapeamento ATT&CK deve permanecer associado ao comportamento realmente observado. A presença de uma técnica não significa, por si só, comprometimento.

## Execução / procedimento
Fluxo de investigação:

1. Identificar alerta inicial.
2. Validar host, usuário e timestamp.
3. Buscar eventos anteriores/posteriores.
4. Construir timeline.
5. Determinar escopo.
6. Mapear técnicas ATT&CK suportadas.
7. Avaliar severidade e impacto.
8. Definir disposition.
9. Recomendar contenção/remediação proporcional.
10. Produzir resumo executivo e análise técnica.

## Resultado esperado
Um relatório de incidente sustentado por evidências, com hipóteses claramente separadas de fatos.

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
O foco é demonstrar processo SOC: evidência, contexto, decisão e comunicação. Nenhuma conclusão deve depender de dados inventados.

## Registro técnico

| Campo | Resultado |
|---|---|
| Caso | [SELECIONAR EVIDÊNCIAS REAIS] |
| Severidade | [DEFINIR] |
| Disposition | [DEFINIR] |

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
Será preenchida após a consolidação das evidências dos laboratórios anteriores.

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
