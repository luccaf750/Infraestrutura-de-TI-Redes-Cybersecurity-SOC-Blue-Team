# Windows Security Log Analysis

Projeto voltado à análise e correlação de eventos do Windows Security Log aplicáveis à rotina de SOC e investigação de incidentes.

O objetivo é documentar não apenas o significado de cada Event ID, mas também os campos relevantes, hipóteses de investigação, possíveis falsos positivos e formas de correlacionar eventos.

## Eventos documentados

| Event ID | Descrição | Uso na investigação |
|---|---|---|
| 4624 | Successful Logon | Identificação de autenticações bem-sucedidas |
| 4625 | Failed Logon | Investigação de falhas de autenticação |
| 4688 | Process Creation | Análise de processos e command line |
| 4720 | User Account Created | Identificação de criação de contas |
| 1102 | Audit Log Cleared | Investigação de limpeza do Security Log |

## Fluxo de análise

```text
Event Collection
      |
Filtering
      |
Field Analysis
      |
Event Correlation
      |
Timeline
      |
Investigation
      |
Classification
      |
Incident Report
```

## Conteúdo

- [Event ID 4624](event-analysis/event-4624.md)
- [Event ID 4625](event-analysis/event-4625.md)
- [Event ID 4688](event-analysis/event-4688.md)
- [Event ID 4720](event-analysis/event-4720.md)
- [Event ID 1102](event-analysis/event-1102.md)
- [Suspicious Account Activity Investigation](investigations/suspicious-account-activity.md)

## Observação

Os cenários e exemplos deste repositório são dados de laboratório destinados ao desenvolvimento e documentação de técnicas de análise.
