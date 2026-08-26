# Detecção e Investigação de PowerShell Suspeito

## Objetivo
Identificar execução de PowerShell e avaliar command line, usuário, processo e contexto para diferenciar administração legítima de comportamento suspeito.

## Ambiente
- Wazuh SIEM/XDR
- Endpoint Windows monitorado pelo Wazuh Agent
- Laboratório local, isolado e autorizado
- Finalidade: treinamento SOC / Blue Team e portfólio técnico

## Cenário
Uma execução controlada do PowerShell gera telemetria para investigação no endpoint Windows e no Wazuh.

## Eventos e telemetria
Eventos úteis podem incluir **4688** (criação de processo) e logs operacionais do PowerShell, conforme a auditoria habilitada no endpoint.

## MITRE ATT&CK
**T1059.001 — Command and Scripting Interpreter: PowerShell**

> O mapeamento ATT&CK deve permanecer associado ao comportamento realmente observado. A presença de uma técnica não significa, por si só, comprometimento.

## Execução / procedimento
Execute apenas no endpoint do laboratório:

```powershell
powershell.exe -NoProfile -Command "Get-Process | Select-Object -First 5"
```

Depois pesquise no Wazuh por eventos do host no intervalo da execução e procure referências a `powershell.exe`, criação de processo e command line. Caso a auditoria de criação de processos/PowerShell não esteja habilitada, registre essa limitação antes de alterar a configuração.

## Resultado esperado
A execução deve produzir telemetria de processo/PowerShell quando a auditoria correspondente estiver habilitada. O Event ID e a Rule ID efetivamente observados devem ser registrados como evidência real.

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
PowerShell é ferramenta administrativa legítima e também é amplamente abusada. A triagem deve considerar command line, processo pai, usuário, horário, codificação/ofuscação, download de conteúdo e relação com outros alertas. O comando deste laboratório é benigno e controlado; o objetivo é aprender a reconhecer a telemetria.

## Registro técnico

| Campo | Resultado |
|---|---|
| MITRE ATT&CK | T1059.001 |
| Classificação esperada | Benigno — atividade controlada de laboratório |
| Event ID real | [COLETAR NO WAZUH] |
| Wazuh Rule ID | [COLETAR NO WAZUH] |

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
A conclusão final deve validar se o Wazuh recebeu telemetria suficiente para reconstruir a execução. Em produção, PowerShell com parâmetros incomuns, conteúdo codificado ou download/execução exigiria investigação adicional.

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
