# SOC Lab — Brute Force Detection & Investigation

Projeto de laboratório voltado para atividades de **Security Operations Center (SOC)**, com foco em monitoramento de eventos, análise de logs, triagem de alertas e investigação de atividades suspeitas em endpoints Windows.

## Objetivos

- Monitoramento de eventos de segurança
- Triagem de alertas
- Análise de Windows Event Logs
- Investigação de falhas de autenticação
- Correlação de eventos
- Classificação de incidentes
- Recomendações de contenção
- Documentação de incidentes

## Arquitetura do Laboratório

```text
Windows 11
   │
   │ Security Events
   ▼
Wazuh SIEM
   │
   │ Alert
   ▼
SOC Analyst
   │
   ├── Triage
   ├── Investigation
   ├── Classification
   └── Incident Response
```

# Incident #001 — Multiple Failed Authentication Attempts

## Informações do alerta

| Campo | Informação |
|---|---|
| Incident ID | INC-001 |
| Categoria | Authentication Attack |
| Severidade | Medium |
| SIEM | Wazuh |
| Endpoint | WIN11-FINANCE-01 |
| Windows Event ID | 4625 |
| Source IP | 192.168.10.57 |
| Target User | administrator |
| Failed Attempts | 127 |
| Time Window | 14:03 – 14:11 |
| Classification | Suspected Brute Force |

## Detecção

Durante o monitoramento dos eventos de autenticação do endpoint `WIN11-FINANCE-01`, foi identificado um volume elevado de falhas de logon associado à conta `administrator`.

O evento **Windows Event ID 4625** indica uma tentativa de autenticação que não foi concluída com sucesso.

Foram observadas **127 falhas de autenticação em aproximadamente oito minutos**, originadas do endereço `192.168.10.57`.

## Triagem

- Alto volume de falhas de autenticação
- Repetição do Windows Event ID 4625
- Mesmo endereço IP de origem
- Curto intervalo entre as tentativas
- Conta administrativa como alvo
- Padrão repetitivo de autenticação

## Investigação

### Origem
`192.168.10.57`

### Usuário afetado
`administrator`

### Evento relacionado
`Event ID 4625 — An account failed to log on`

### Frequência
`127 failed authentication attempts`

Janela: `14:03 – 14:11`

### Correlação
Eventos **4625** devem ser correlacionados com eventos **4624** para verificar se uma sequência de tentativas malsucedidas foi seguida por uma autenticação válida.

## Classificação

### Suspected Brute Force Attack

A combinação de múltiplas falhas de autenticação, curto intervalo de tempo, origem recorrente e utilização de uma conta administrativa caracteriza comportamento compatível com tentativa de **Brute Force**.

## Incident Response

1. Correlacionar eventos 4625 e 4624.
2. Verificar autenticações bem-sucedidas posteriores às tentativas.
3. Investigar o endereço IP de origem.
4. Identificar outras contas acessadas pela mesma origem.
5. Verificar atividades realizadas pela conta após eventual autenticação.
6. Avaliar bloqueio temporário do endereço IP.
7. Avaliar redefinição das credenciais da conta afetada.
8. Revisar políticas de bloqueio de contas.
9. Escalonar o incidente caso seja identificado comprometimento.

## Mitigações recomendadas

- MFA
- Políticas de senha robustas
- Account Lockout Policy
- Restrição de acesso a contas administrativas
- Monitoramento contínuo de autenticações
- Regras SIEM para múltiplas falhas de logon
- Segmentação de rede
- Princípio do menor privilégio

## MITRE ATT&CK

**T1110 — Brute Force**  
Tática: **Credential Access**

## Tecnologias e conceitos

`SOC` `Blue Team` `SIEM` `Wazuh` `Windows Event Logs` `Event ID 4625` `Event ID 4624` `Log Analysis` `Brute Force` `Incident Response` `Threat Detection` `MITRE ATT&CK`
