# Detecção de Port Scan e Reconhecimento

## Objetivo
Executar e documentar um cenário controlado de laboratório, identificar os eventos gerados, realizar a triagem no Wazuh e registrar uma análise com foco nas atividades de um Analista SOC L1.

## Escopo e ambiente
- SIEM/XDR: Wazuh
- Endpoint: Windows
- Ambiente: laboratório local e controlado
- Finalidade: treinamento defensivo e construção de portfólio SOC/Blue Team

## Cenário
Este laboratório simula uma atividade relevante para monitoramento de segurança. A execução deve ocorrer exclusivamente no ambiente de laboratório autorizado.

## Procedimento
1. Confirmar que o Wazuh Manager e o endpoint Windows estão ativos.
2. Confirmar que o agente Windows está conectado ao Wazuh.
3. Executar a simulação correspondente ao cenário.
4. Aguardar a ingestão dos eventos.
5. Pesquisar os eventos no Wazuh Dashboard.
6. Examinar usuário, host, origem, horário, processo e demais campos disponíveis.
7. Correlacionar eventos relacionados.
8. Classificar a atividade.
9. Registrar as evidências reais na pasta `evidencias/`.

> **Importante:** não inserir evidências, Rule IDs, IPs, timestamps ou resultados fictícios. Esses dados devem ser coletados durante a execução real.

## Detecção e triagem
Durante a investigação, responder:

- Qual evento iniciou a investigação?
- Qual host foi afetado?
- Qual conta/usuário está envolvido?
- Qual foi o horário da atividade?
- Existe endereço IP de origem relevante?
- Há eventos anteriores ou posteriores relacionados?
- O comportamento é esperado ou suspeito?
- Qual a severidade apropriada?
- O caso deve ser encerrado, monitorado ou escalado?

## MITRE ATT&CK
**Mapeamento principal:** T1046 — Network Service Discovery

O mapeamento deve ser validado após observar a atividade real e os eventos coletados.

## Evidências necessárias
Salvar em `evidencias/`, quando aplicável:

1. Execução da simulação.
2. Evento/alerta no Wazuh.
3. Campos relevantes do evento.
4. Eventos correlacionados.
5. Resultado final da investigação.

Sugestão de nomes:
- `01-execucao.png`
- `02-alerta-wazuh.png`
- `03-detalhes-evento.png`
- `04-correlacao.png`
- `05-conclusao.png`

## Registro da investigação

| Campo | Resultado |
|---|---|
| Data/hora | PREENCHER APÓS EXECUÇÃO |
| Host | PREENCHER APÓS EXECUÇÃO |
| Usuário | PREENCHER APÓS EXECUÇÃO |
| IP de origem | PREENCHER APÓS EXECUÇÃO |
| Event ID | PREENCHER APÓS EXECUÇÃO |
| Wazuh Rule ID | PREENCHER APÓS EXECUÇÃO |
| Nível do alerta | PREENCHER APÓS EXECUÇÃO |
| MITRE ATT&CK | T1046 — Network Service Discovery |
| Classificação | PREENCHER APÓS INVESTIGAÇÃO |

## Análise SOC
**Contexto:** PREENCHER APÓS EXECUÇÃO.

**Evidências observadas:** PREENCHER APÓS EXECUÇÃO.

**Correlação:** PREENCHER APÓS EXECUÇÃO.

**Classificação:** PREENCHER APÓS EXECUÇÃO.

## Contenção e remediação
Após a investigação, registrar quais ações seriam apropriadas em um ambiente corporativo, considerando preservação de evidências, impacto operacional e procedimentos de resposta a incidentes.

## Conclusão
PREENCHER APÓS A EXECUÇÃO REAL DO LABORATÓRIO.

## Competências demonstradas
- Monitoramento de eventos de segurança
- Wazuh SIEM
- Windows Event Logs
- Triagem de alertas
- Correlação de eventos
- MITRE ATT&CK
- Análise e documentação de incidentes
- Fundamentos de SOC / Blue Team

---
**Status:** Planejado — aguardando execução e evidências reais.
