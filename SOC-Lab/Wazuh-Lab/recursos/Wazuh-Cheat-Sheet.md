# Wazuh Cheat Sheet

## Triagem básica
1. Identifique o alerta e o Event ID.
2. Verifique agente/host.
3. Verifique usuário e IP de origem.
4. Analise timestamp e sequência temporal.
5. Procure eventos relacionados.
6. Valide contexto.
7. Classifique severidade e disposition.
8. Documente evidências.

## Campos úteis
- `agent.name`
- `agent.id`
- `agent.ip`
- `rule.id`
- `rule.level`
- `rule.description`
- `data.win.system.eventID`
- `data.win.eventdata.subjectUserName`
- `data.win.eventdata.targetUserName`
- `data.win.eventdata.ipAddress`

Os campos disponíveis variam conforme o evento e a configuração do agente.
