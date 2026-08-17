# Event ID 4625 - Failed Logon

## Descrição

O Event ID `4625` é registrado quando uma tentativa de logon falha no Windows.

## Campos relevantes

- Account Name
- Account Domain
- Logon Type
- Workstation Name
- Source Network Address
- Source Port
- Failure Reason
- Status
- SubStatus
- Authentication Package

## O que analisar

- quantidade de falhas;
- intervalo entre eventos;
- usuário alvo;
- endereço de origem;
- múltiplas contas atingidas;
- Logon Type;
- motivo da falha;
- autenticação bem-sucedida posterior.

## Hipóteses de investigação

- Brute Force
- Password Guessing
- Password Spraying
- senha digitada incorretamente
- credencial expirada
- serviço utilizando senha antiga
- tarefa agendada com credencial inválida
- tentativa de acesso não autorizado

## Correlação

Muitas ocorrências de `4625` para uma mesma conta e origem em curto período podem justificar um alerta.

A correlação com `4624` é importante para verificar se houve sucesso após as falhas.
