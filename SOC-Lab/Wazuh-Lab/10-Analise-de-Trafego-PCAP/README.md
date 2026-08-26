# Análise de Tráfego de Rede com PCAP

## Objetivo
Praticar triagem de tráfego usando Wireshark e correlacionar observações de rede com o contexto do endpoint.

## Ambiente
- Wazuh SIEM/XDR
- Endpoint Windows monitorado pelo Wazuh Agent
- Laboratório local, isolado e autorizado
- Finalidade: treinamento SOC / Blue Team e portfólio técnico

## Cenário
Uma captura curta do próprio endpoint é analisada para identificar DNS, TCP e conexões observáveis sem gerar tráfego malicioso.

## Eventos e telemetria
PCAP não possui Event IDs Windows. As evidências principais são frames, endpoints, protocolos, portas e timestamps.

## MITRE ATT&CK
**Network Traffic Analysis — exercício de análise; o mapeamento ATT&CK depende do comportamento encontrado.**

> O mapeamento ATT&CK deve permanecer associado ao comportamento realmente observado. A presença de uma técnica não significa, por si só, comprometimento.

## Execução / procedimento
No Wireshark, selecione a interface ativa e faça uma captura curta durante navegação normal/controlada. Pare a captura e use filtros como:

```text
dns
tcp
tcp.flags.syn == 1
```

Não publique PCAP contendo dados sensíveis. Para o GitHub, prefira screenshots sanitizados e conclusões.

## Resultado esperado
Identificação de consultas DNS, sessões TCP, IPs e portas observados durante a captura.

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
Registre origem/destino, protocolo, porta, sequência temporal e o motivo pelo qual o tráfego é esperado ou merece investigação. O objetivo é desenvolver leitura de rede, não classificar tráfego normal como ataque.

## Registro técnico

| Campo | Resultado |
|---|---|
| Ferramenta | Wireshark |
| Artefato | PCAP local |
| Classificação | [DEFINIR APÓS ANÁLISE] |

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
O laboratório deve demonstrar capacidade de aplicar filtros, identificar conversações e explicar o tráfego observado de maneira reproduzível.

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
