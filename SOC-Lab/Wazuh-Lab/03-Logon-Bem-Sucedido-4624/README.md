# Investigação de Logon Bem-Sucedido — Event ID 4624

## Objetivo
Analisar autenticações bem-sucedidas do Windows e distinguir atividade normal de um possível uso indevido de credenciais.

## Ambiente
- Wazuh SIEM/XDR
- Endpoint Windows monitorado pelo Wazuh Agent
- Laboratório local, isolado e autorizado
- Finalidade: treinamento SOC / Blue Team e portfólio técnico

## Cenário
Um Event ID 4624 é analisado no Wazuh para identificar conta, contexto de segurança e correlação com outros eventos.

## Eventos e telemetria
**4624 — An account was successfully logged on.**

## MITRE ATT&CK
**T1078 — Valid Accounts**

> O mapeamento ATT&CK deve permanecer associado ao comportamento realmente observado. A presença de uma técnica não significa, por si só, comprometimento.

## Execução / procedimento
O cenário já foi analisado no laboratório por meio dos eventos coletados do endpoint Windows.

## Resultado esperado
O Wazuh apresenta o Event ID 4624 e os campos de autenticação disponíveis no evento.

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
Na investigação realizada foi observado o contexto `SYSTEM`, SID `S-1-5-18`, Logon ID `0x3E7` e Wazuh Rule ID **60106**. O simples Event ID 4624 não caracteriza incidente; horário, tipo de logon, origem, conta e eventos adjacentes determinam a relevância.

## Registro técnico

| Campo | Resultado |
|---|---|
| Event ID | 4624 |
| Conta/contexto | SYSTEM |
| SID | S-1-5-18 |
| Logon ID | 0x3E7 |
| Wazuh Rule ID | 60106 |
| Classificação | Atividade observada e analisada no laboratório |

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
O laboratório demonstrou que um logon bem-sucedido deve ser interpretado em contexto. A correlação com falhas anteriores, origem incomum ou conta privilegiada pode transformar um evento rotineiro em indicador relevante.

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
