# SOC Lab

Laboratório voltado à rotina de um SOC Analyst N1, com foco em triagem de alertas, análise de eventos de autenticação, correlação de logs, classificação e resposta a incidentes.

## Projeto em destaque

### Brute Force Detection & Investigation

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

## Conteúdo

- [INC-001 - Brute Force Detection & Investigation](incident-reports/INC-001-Brute-Force.md)
- [Windows Event ID 4625 - Sample Dataset](sample-logs/windows-4625.md)
- [Brute Force Detection Logic](detection-rules/brute-force.md)
