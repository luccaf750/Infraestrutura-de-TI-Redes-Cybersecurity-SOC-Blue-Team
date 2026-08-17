# Brute Force Detection Logic

## Objetivo

Identificar concentração anormal de falhas de autenticação em uma janela curta.

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

Exemplo: 10 falhas em 5 minutos, agrupadas por Source IP + Target User.

Após o alerta, a correlação com Event ID `4624` ajuda a verificar eventual autenticação bem-sucedida.

## Possíveis falsos positivos

- senha incorreta;
- serviço com credencial desatualizada;
- tarefa agendada com senha antiga;
- erro de configuração;
- atividade administrativa autorizada.

## MITRE ATT&CK

- Credential Access
- T1110 - Brute Force
- T1110.001 - Password Guessing
