# Adição de Usuário ao Grupo Administradores — Event ID 4732

## Objetivo
Detectar e investigar a inclusão de uma conta em um grupo local privilegiado do Windows.

## Ambiente
- Wazuh SIEM/XDR
- Endpoint Windows monitorado pelo Wazuh Agent
- Laboratório local, isolado e autorizado
- Finalidade: treinamento SOC / Blue Team e portfólio técnico

## Cenário
A conta `soc-test` é adicionada ao grupo local **Administradores**. Em um SOC, essa alteração exige validação porque pode representar elevação de privilégio ou alteração administrativa legítima.

## Eventos e telemetria
**4732 — A member was added to a security-enabled local group.**

## MITRE ATT&CK
**T1098 — Account Manipulation**

> O mapeamento ATT&CK deve permanecer associado ao comportamento realmente observado. A presença de uma técnica não significa, por si só, comprometimento.

## Execução / procedimento
O cenário já foi executado no laboratório. A investigação observou a inclusão do usuário `soc-test` no grupo **Administradores**.

## Resultado esperado
O Windows registra o Event ID 4732 e o Wazuh ingere o evento para análise.

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
A alteração concede privilégios administrativos à conta adicionada. Durante a investigação realizada, o usuário alvo foi `soc-test`, o grupo foi `Administradores` e a ação foi associada ao usuário `Lucas`. O Wazuh correlacionou o evento à regra **60154**. Esse tipo de alteração deve ser confrontado com mudança autorizada, ticket e contexto do endpoint.

## Registro técnico

| Campo | Resultado |
|---|---|
| Event ID | 4732 |
| Usuário alvo | soc-test |
| Grupo | Administradores |
| Usuário responsável | Lucas |
| Wazuh Rule ID | 60154 |
| Classificação | Atividade controlada de laboratório |

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
O evento demonstrou como uma alteração de associação a grupo privilegiado pode ser identificada e triada no Wazuh. Em produção, uma inclusão não autorizada em Administradores justificaria escalonamento e investigação da origem da alteração.

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
