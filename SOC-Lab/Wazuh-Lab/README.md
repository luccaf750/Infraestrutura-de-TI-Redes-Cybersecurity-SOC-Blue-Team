# Laboratório Wazuh — SOC / Blue Team

## Objetivo

Este laboratório tem como objetivo praticar atividades de monitoramento e análise de eventos de segurança utilizando o Wazuh SIEM em um ambiente controlado.

Os testes são realizados em um endpoint Windows integrado ao Wazuh, simulando ações que podem ser encontradas durante a rotina de um Analista SOC.

## Ambiente do laboratório

- Wazuh SIEM
- Wazuh Dashboard
- Wazuh Agent
- Windows
- VirtualBox
- Windows Security Event Logs

## Atividades realizadas

### 1. Criação de usuário local — Event ID 4720

Criação da conta de laboratório `soc-test` no Windows e identificação do evento correspondente no Wazuh.

**Event ID:** 4720

Objetivo da análise: identificar a criação de novas contas e verificar quem realizou a ação.

---

### 2. Inclusão em grupo privilegiado — Event ID 4732

Inclusão da conta `soc-test` no grupo local `Administradores`.

**Event ID:** 4732  
**Wazuh Rule ID:** 60154  
**Nível do alerta:** 12

Objetivo da análise: identificar alterações em grupos privilegiados e avaliar possíveis casos de elevação de privilégios.

---

### 3. Logon bem-sucedido — Event ID 4624

Análise de evento de autenticação bem-sucedida no Windows.

**Event ID:** 4624  
**Wazuh Rule ID:** 60106

Durante a investigação foi identificado o SID:

`S-1-5-18`

correspondente à conta interna `SYSTEM` do Windows.

Também foi analisado o Logon ID:

`0x3E7`

A análise demonstrou a importância de diferenciar eventos associados a usuários comuns daqueles gerados pelo próprio sistema operacional.

## Metodologia

Para cada atividade do laboratório será utilizado o seguinte processo:

1. Gerar uma atividade controlada no endpoint.
2. Localizar o evento no Wazuh.
3. Identificar Event ID e regra acionada.
4. Analisar usuário, origem e contexto.
5. Avaliar o nível do alerta.
6. Classificar a atividade.
7. Registrar evidências.
8. Documentar a conclusão da investigação.

## Finalidade

Este laboratório faz parte de um portfólio prático voltado ao desenvolvimento de conhecimentos em SOC, Blue Team, análise de logs e investigação de eventos de segurança.
