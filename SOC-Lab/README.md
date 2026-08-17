# SOC Lab

Laboratório voltado à rotina de um SOC Analyst N1, com foco em triagem de alertas, análise de eventos de autenticação, correlação de logs, classificação e resposta a incidentes.

## Projeto em destaque

### Brute Force Detection & Investigation

Cenário de laboratório com múltiplas falhas de autenticação em endpoint Windows monitorado por SIEM.

- Endpoint: `WIN11-FINANCE-01`
- SIEM de referência: `Wazuh`
- Evento principal: `4625`
- Conta alvo: `administrator`
- Origem: `192.168.10.57`
- Falhas observadas: `127`
- Janela: `14:03 - 14:11`
- Classificação: `Suspected Brute Force`
- MITRE ATT&CK: `T1110 - Brute Force`
- Subtécnica: `T1110.001 - Password Guessing`

## Fluxo

```text
Windows Endpoint
      |
Windows Security Logs
      |
Wazuh / SIEM
      |
Security Alert
      |
SOC Triage
      |
Investigation
      |
Classification
      |
Incident Response
```

## Estrutura

```text
SOC-Lab/
├── README.md
├── incident-reports/
│   └── INC-001-Brute-Force.md
├── sample-logs/
│   └── windows-4625.md
└── detection-rules/
    └── brute-force.md
```

## Pontos analisados

- volume de falhas de autenticação;
- usuário alvo e IP de origem;
- janela temporal;
- Event ID 4625;
- correlação com Event ID 4624;
- falsos positivos;
- MITRE ATT&CK;
- contenção e mitigação.

## Referências

- Microsoft Learn — Windows Security Auditing
- MITRE ATT&CK — T1110 Brute Force
- Wazuh Documentation — Brute-force attack detection
