# Event ID 1102 - Audit Log Cleared

## Descrição

O Event ID `1102` indica que o Windows Security Audit Log foi limpo.

## Relevância

A limpeza pode ocorrer por atividade administrativa legítima, manutenção ou troubleshooting. Entretanto, também merece atenção porque a remoção de registros pode dificultar uma investigação.

## Campos relevantes

- Subject User Name
- Subject Domain Name
- Subject Logon ID
- Timestamp

## O que analisar

- Qual usuário realizou a ação?
- A ação estava autorizada?
- Houve atividade suspeita antes da limpeza?
- Existem logs centralizados preservados em SIEM?
- A conta envolvida apresentou outras atividades incomuns?

## Correlação

Exemplo de sequência que justificaria investigação:

```text
4625 - Multiple Failed Logons
4624 - Successful Logon
4688 - Suspicious Process Activity
4720 - New User Account
1102 - Security Audit Log Cleared
```

A sequência não prova comprometimento por si só. Ela fornece uma timeline que precisa ser validada com contexto e outras fontes de evidência.
