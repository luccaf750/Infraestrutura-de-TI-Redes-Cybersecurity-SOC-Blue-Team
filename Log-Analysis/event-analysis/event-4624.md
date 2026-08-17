# Event ID 4624 - Successful Logon

## Descrição

O Event ID `4624` é registrado quando uma sessão de logon é criada com sucesso no sistema Windows.

## Campos relevantes

- Account Name
- Account Domain
- Logon ID
- Logon Type
- Workstation Name
- Source Network Address
- Source Port
- Authentication Package
- Process Name

## O que analisar

Um logon bem-sucedido não representa, isoladamente, uma atividade maliciosa. O contexto determina sua relevância.

Perguntas úteis:

- Qual usuário realizou o logon?
- A origem é conhecida?
- O horário é compatível com o comportamento esperado?
- Qual foi o Logon Type?
- Houve diversas falhas antes do sucesso?
- A conta possui privilégios elevados?
- Houve atividade suspeita após a autenticação?

## Correlação

Uma sequência como:

```text
4625
4625
4625
4625
4624
```

pode indicar que uma sequência de falhas foi seguida por autenticação bem-sucedida e merece investigação.

## Possíveis cenários

- autenticação legítima;
- acesso remoto autorizado;
- sucesso após erro de senha;
- comprometimento de credencial;
- brute force bem-sucedido.

A conclusão depende da correlação com outros eventos e do contexto do ambiente.
