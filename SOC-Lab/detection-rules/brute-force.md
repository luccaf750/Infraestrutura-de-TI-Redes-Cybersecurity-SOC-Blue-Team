# Brute Force Detection Logic

## Objetivo

Identificar concentração anormal de falhas de autenticação em uma janela curta.

## Lógica conceitual

```text
IF
    Event ID = 4625
AND
    failures >= threshold
AND
    events occur within defined time window
THEN
    generate authentication brute-force alert
```

## Exemplo

```text
Event ID: 4625
Threshold: 10 failed logons
Window: 5 minutes
Grouping: Source IP + Target User
```

O threshold deve ser ajustado ao ambiente para reduzir falsos positivos.

## Correlação

```text
4625 + 4625 + 4625 + ... + 4624
```

Um `4624` após diversas falhas pode aumentar a prioridade da investigação.

## Possíveis falsos positivos

- usuário com senha incorreta;
- serviço com credencial desatualizada;
- tarefa agendada com senha antiga;
- dispositivo com credencial inválida;
- erro de configuração;
- atividade administrativa autorizada.

## MITRE ATT&CK

- Tactic: Credential Access
- Technique: T1110 - Brute Force
- Sub-technique: T1110.001 - Password Guessing
