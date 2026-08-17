# Investigation - Suspicious Account Activity

## Objetivo

Demonstrar a correlação de múltiplos Windows Security Events em uma investigação de atividade suspeita de conta.

## Cenário

Um endpoint Windows apresenta uma sequência de eventos que exige análise.

```text
09:14:02 - Event 4625 - Failed Logon
09:14:08 - Event 4625 - Failed Logon
09:14:15 - Event 4625 - Failed Logon
09:15:01 - Event 4624 - Successful Logon
09:17:34 - Event 4688 - powershell.exe created
09:22:11 - Event 4720 - New user account created
09:31:45 - Event 1102 - Security Audit Log cleared
```

## Etapa 1 - Authentication Analysis

As falhas `4625` são analisadas por usuário, origem, Logon Type, frequência e motivo.

O evento `4624` posterior é correlacionado para verificar se o mesmo usuário/origem conseguiu autenticar.

## Etapa 2 - Process Analysis

O evento `4688` é analisado para identificar:

- processo criado;
- processo pai;
- usuário responsável;
- caminho do executável;
- command line;
- relação temporal com o logon.

## Etapa 3 - Account Creation

O evento `4720` é analisado para determinar:

- qual conta foi criada;
- quem realizou a criação;
- se a ação era esperada;
- atividades posteriores da nova conta.

## Etapa 4 - Audit Log

O evento `1102` aumenta a relevância da investigação por indicar limpeza do Security Audit Log.

É necessário verificar se a ação fazia parte de uma atividade administrativa autorizada e se os eventos anteriores permanecem disponíveis em uma plataforma centralizada.

## Timeline

```text
Failed Logons
      |
Successful Logon
      |
Process Creation
      |
New Account
      |
Audit Log Cleared
```

## Assessment

**Classification:** Suspicious Account Activity  
**Priority:** High for investigation

A sequência apresenta múltiplos indicadores que, quando correlacionados, justificam investigação aprofundada. Entretanto, a timeline sozinha não é suficiente para afirmar comprometimento.

## Próximas ações

1. Identificar origem das autenticações.
2. Validar usuário e horário.
3. Revisar Logon Type.
4. Analisar processo pai e command line do Event 4688.
5. Investigar a conta criada.
6. Verificar alterações de privilégios/grupos.
7. Consultar logs centralizados.
8. Verificar atividade de rede e endpoint.
9. Confirmar se a limpeza do log era autorizada.
10. Escalonar caso existam evidências adicionais de comprometimento.

## Conclusão

A investigação demonstra como eventos isolados ganham significado quando analisados em conjunto. O trabalho do analista é validar contexto, construir uma timeline e diferenciar atividade administrativa legítima de comportamento potencialmente malicioso.
