# Reconhecimento e Varredura de Portas

## Objetivo
Observar sinais de descoberta de serviços e discutir quais fontes de telemetria são necessárias para detectar um port scan.

## Ambiente
- Wazuh SIEM/XDR
- Endpoint Windows monitorado pelo Wazuh Agent
- Laboratório local, isolado e autorizado
- Finalidade: treinamento SOC / Blue Team e portfólio técnico

## Cenário
Uma varredura limitada é realizada exclusivamente contra o host do laboratório, em rede própria/autorizada.

## Eventos e telemetria
Não existe um único Event ID Windows universal para port scan. A detecção normalmente depende de firewall, IDS/IPS, EDR/NDR ou logs de rede ingeridos pelo SIEM.

## MITRE ATT&CK
**T1046 — Network Service Discovery**

> O mapeamento ATT&CK deve permanecer associado ao comportamento realmente observado. A presença de uma técnica não significa, por si só, comprometimento.

## Execução / procedimento
Use apenas o IP do endpoint de laboratório. Se o Nmap estiver disponível:

```cmd
nmap -sT -Pn --top-ports 20 <IP-DO-ENDPOINT-LAB>
```

Não use redes ou ativos de terceiros. No Wazuh, procure eventos de firewall/rede no mesmo intervalo e registre se a fonte atual fornece ou não visibilidade suficiente.

## Resultado esperado
O resultado depende das fontes habilitadas. A ausência de alerta também é um achado válido: demonstra uma lacuna de telemetria que deve ser documentada.

## Roteiro de investigação
1. Confirmar o endpoint e a janela temporal.
2. Identificar o evento/alerta que iniciou a análise.
3. Examinar usuário, host, origem, processo/comando e demais campos disponíveis.
4. Buscar eventos imediatamente anteriores e posteriores.
5. Validar se existe relação entre os eventos.
6. Comparar a atividade com o cenário autorizado do laboratório.
7. Registrar fatos separadamente de hipóteses.
8. Definir severidade e classificação com base no contexto.
9. Salvar evidências reais.
10. Documentar a conclusão.

## Análise SOC
Uma sequência de conexões a múltiplas portas em curto intervalo pode indicar reconhecimento. Analise IP origem/destino, quantidade de portas, duração, portas abertas e legitimidade do scanner. Em SOC, é essencial diferenciar ferramenta administrativa/vulnerability scanner de reconhecimento não autorizado.

## Registro técnico

| Campo | Resultado |
|---|---|
| MITRE ATT&CK | T1046 |
| Origem | [COLETAR] |
| Destino | [COLETAR] |
| Resultado Wazuh | [VALIDAR TELEMETRIA] |

## Critérios de escalonamento
Em ambiente corporativo, considerar escalonamento quando houver, conforme o cenário:
- atividade sem mudança/ticket autorizado;
- conta privilegiada ou ativo crítico;
- origem inesperada;
- execução ou persistência sem justificativa;
- múltiplos eventos correlacionados aumentando a confiança;
- evidência de impacto, propagação ou comprometimento;
- necessidade de contenção além da atribuição do SOC L1.

## Contenção e remediação
A resposta deve ser proporcional ao caso e seguir procedimentos organizacionais. Possíveis ações incluem validar a mudança com o proprietário do ativo, preservar evidências, desabilitar/restringir contas quando autorizado, remover mecanismos não autorizados, isolar endpoint quando necessário e escalar para resposta a incidentes. **Não executar contenção destrutiva no laboratório apenas para produzir evidência.**

## Evidências para o GitHub
Adicionar somente evidências reais e sanitizadas à pasta `evidencias/`.

Sugestão:
- `01-execucao.png`
- `02-alerta-wazuh.png`
- `03-campos-relevantes.png`
- `04-correlacao.png`
- `05-resultado-final.png`

Não publicar senhas, tokens, dados pessoais, IP público sensível ou informação confidencial.

## Conclusão
A investigação deve concluir se a telemetria atual permite detectar reconhecimento. Caso não permita, documentar a necessidade de ingestão de firewall/IDS é parte válida do resultado.

## Competências demonstradas
- Wazuh SIEM
- Windows Event Logs
- Triagem de alertas
- Correlação e construção de contexto
- MITRE ATT&CK
- Documentação de investigação
- Fundamentos de resposta a incidentes
- SOC / Blue Team

---
**Observação de integridade:** campos marcados como `[COLETAR]`, `[VALIDAR]` ou equivalentes dependem da execução real e não devem ser substituídos por dados presumidos.
