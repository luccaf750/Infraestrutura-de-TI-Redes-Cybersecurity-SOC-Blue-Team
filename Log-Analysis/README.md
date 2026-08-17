# Windows Security Log Analysis

Área dedicada à análise e correlação de eventos de segurança do Windows.

## Eventos de interesse

- Event ID 4624 - Successful Logon
- Event ID 4625 - Failed Logon
- Event ID 4688 - Process Creation
- Event ID 4720 - User Account Created
- Event ID 1102 - Audit Log Cleared

## Fluxo de análise

```text
Evento -> Coleta -> Filtragem -> Correlação -> Investigação -> Classificação -> Relatório
```

O objetivo é desenvolver capacidade de identificar padrões relevantes, distinguir atividade legítima de comportamento suspeito e documentar conclusões.
