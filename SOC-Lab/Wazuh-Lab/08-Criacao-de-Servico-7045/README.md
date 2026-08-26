# Criação de Serviço Windows — Event ID 7045

## Objetivo
Detectar e investigar a instalação de um novo serviço Windows.

## Ambiente
- Wazuh SIEM/XDR
- Endpoint Windows monitorado pelo Wazuh Agent
- Laboratório local, isolado e autorizado
- Finalidade: treinamento SOC / Blue Team e portfólio técnico

## Cenário
Um serviço de laboratório é criado apontando para um binário nativo e não é iniciado. Depois da coleta, ele é removido.

## Eventos e telemetria
**7045 — A service was installed in the system** (System log). Outros eventos podem complementar a criação conforme a auditoria.

## MITRE ATT&CK
**T1543.003 — Create or Modify System Process: Windows Service**

> O mapeamento ATT&CK deve permanecer associado ao comportamento realmente observado. A presença de uma técnica não significa, por si só, comprometimento.

## Execução / procedimento
No **Prompt de Comando como administrador**:

```cmd
sc create SOCLabService binPath= "C:\Windows\System32\cmd.exe /c exit" start= demand
```

Não inicie o serviço. Após a coleta:

```cmd
sc delete SOCLabService
```

## Resultado esperado
A criação deve gerar Event ID 7045 no Windows. O Wazuh Rule ID e o nível efetivamente gerados dependem da configuração instalada.

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
Serviços permitem execução privilegiada e persistência. Analise Service Name, ImagePath/binPath, conta, horário e origem da criação. Binários em caminhos temporários, nomes semelhantes a serviços legítimos ou criação fora de janela de mudança aumentam a suspeita.

## Registro técnico

| Campo | Resultado |
|---|---|
| Event ID esperado | 7045 |
| Serviço | SOCLabService |
| MITRE ATT&CK | T1543.003 |
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
O laboratório demonstra a detecção de criação de serviço. Em ambiente corporativo, um serviço desconhecido deve ser validado contra inventário, mudança autorizada, assinatura/hash do binário e atividade relacionada.

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
