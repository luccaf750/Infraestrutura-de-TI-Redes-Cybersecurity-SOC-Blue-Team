# Persistência com Scheduled Task

## Objetivo
Detectar a criação de uma tarefa agendada e analisar seu potencial uso como mecanismo de persistência.

## Ambiente
- Wazuh SIEM/XDR
- Endpoint Windows monitorado pelo Wazuh Agent
- Laboratório local, isolado e autorizado
- Finalidade: treinamento SOC / Blue Team e portfólio técnico

## Cenário
Uma tarefa agendada inofensiva é criada no endpoint do laboratório, detectada e posteriormente removida.

## Eventos e telemetria
**4698** pode registrar criação de tarefa agendada quando a auditoria correspondente está habilitada. Logs do Task Scheduler também podem complementar a análise.

## MITRE ATT&CK
**T1053.005 — Scheduled Task/Job: Scheduled Task**

> O mapeamento ATT&CK deve permanecer associado ao comportamento realmente observado. A presença de uma técnica não significa, por si só, comprometimento.

## Execução / procedimento
No **Prompt de Comando como administrador**, crie uma tarefa inofensiva:

```cmd
schtasks /create /tn "SOC-Lab-Test" /tr "cmd.exe /c echo SOC-Lab > %TEMP%\soc-lab.txt" /sc ONCE /st 23:59 /f
```

Após coletar as evidências, remova-a:

```cmd
schtasks /delete /tn "SOC-Lab-Test" /f
```

Não execute a tarefa; o objetivo é observar a criação e a telemetria.

## Resultado esperado
O endpoint pode registrar a criação da tarefa e o Wazuh poderá ingerir os eventos disponíveis conforme a política de auditoria.

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
Scheduled Tasks são usadas legitimamente por administradores e aplicações, mas também permitem persistência. Analise nome da tarefa, comando executado, usuário criador, horário e caminho do binário. A tarefa `SOC-Lab-Test` é deliberadamente identificável e inofensiva.

## Registro técnico

| Campo | Resultado |
|---|---|
| MITRE ATT&CK | T1053.005 |
| Nome da tarefa | SOC-Lab-Test |
| Classificação esperada | Benigno — simulação controlada |
| Event ID/Rule ID | [VALIDAR NO AMBIENTE] |

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
O laboratório demonstra como alterações no Task Scheduler podem ser investigadas. Em produção, tarefas recém-criadas com executáveis em diretórios temporários, nomes enganosos ou contas incomuns merecem escalonamento.

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
