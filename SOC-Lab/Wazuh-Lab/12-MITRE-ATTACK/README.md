# Mapeamento de Evidências ao MITRE ATT&CK

## Objetivo
Relacionar comportamentos efetivamente observados nos laboratórios a técnicas ATT&CK sem mapear apenas por palavra-chave.

## Ambiente
- Wazuh SIEM/XDR
- Endpoint Windows monitorado pelo Wazuh Agent
- Laboratório local, isolado e autorizado
- Finalidade: treinamento SOC / Blue Team e portfólio técnico

## Cenário
Eventos dos laboratórios anteriores são revisados e associados a técnicas com base no comportamento observado.

## Eventos e telemetria
Utilizar evidências reais dos Labs 02–11.

## MITRE ATT&CK
**T1078, T1098, T1059.001, T1053.005, T1543.003 e T1046, quando suportados pelas evidências.**

> O mapeamento ATT&CK deve permanecer associado ao comportamento realmente observado. A presença de uma técnica não significa, por si só, comprometimento.

## Execução / procedimento
Revise as evidências e preencha uma matriz:

| Evidência | Comportamento | Técnica ATT&CK | Justificativa |
|---|---|---|---|
| 4732 | Alteração de associação privilegiada | T1098 | Manipulação de conta |
| PowerShell | Execução via PowerShell | T1059.001 | Interpretador PowerShell |
| Scheduled Task | Criação de tarefa | T1053.005 | Scheduled Task |
| Serviço | Criação de serviço | T1543.003 | Windows Service |
| Port scan | Descoberta de serviços | T1046 | Network Service Discovery |

Só mantenha linhas suportadas pela execução real.

## Resultado esperado
Uma matriz ATT&CK defensável, vinculada às evidências do portfólio.

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
ATT&CK descreve comportamento adversário; não é um sistema de severidade nem prova de ataque. Um comportamento de laboratório pode mapear tecnicamente para uma técnica mesmo sendo benigno no contexto controlado.

## Registro técnico

| Campo | Resultado |
|---|---|
| Fonte | Labs anteriores |
| Resultado | Matriz de técnicas suportadas por evidência |

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
O laboratório consolida a capacidade de traduzir telemetria técnica em linguagem padronizada de detecção e threat-informed defense.

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
