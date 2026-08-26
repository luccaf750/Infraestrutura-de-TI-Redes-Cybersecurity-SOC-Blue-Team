# Correlação de Eventos e Construção de Timeline

## Objetivo
Correlacionar múltiplos eventos para transformar alertas isolados em uma narrativa investigativa.

## Ambiente
- Wazuh SIEM/XDR
- Endpoint Windows monitorado pelo Wazuh Agent
- Laboratório local, isolado e autorizado
- Finalidade: treinamento SOC / Blue Team e portfólio técnico

## Cenário
São usados eventos já coletados — criação de conta, mudança de privilégio, autenticação e demais labs — para construir uma timeline.

## Eventos e telemetria
Exemplos disponíveis no portfólio incluem 4720, 4732, 4624 e 4625, além dos eventos validados nos Labs 06–09.

## MITRE ATT&CK
**Múltiplas técnicas — conforme os eventos correlacionados.**

> O mapeamento ATT&CK deve permanecer associado ao comportamento realmente observado. A presença de uma técnica não significa, por si só, comprometimento.

## Execução / procedimento
1. Defina uma janela temporal.
2. Ordene os eventos por timestamp.
3. Registre host, usuário, origem, Event ID e ação.
4. Identifique relações de causa/efeito.
5. Separe coincidência temporal de correlação sustentada por evidência.
6. Produza uma timeline final.

## Resultado esperado
Timeline que mostre como diferentes fontes/eventos mudam a interpretação do alerta.

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
Correlação reduz o risco de analisar um Event ID fora de contexto. Falhas de autenticação seguidas por sucesso, criação de conta seguida de privilégio e execução subsequente podem aumentar a prioridade — mas apenas quando os campos sustentam a relação.

## Registro técnico

| Campo | Resultado |
|---|---|
| Fontes | Eventos reais dos laboratórios |
| Produto final | Timeline investigativa |
| Classificação | [APÓS CORRELAÇÃO] |

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
O laboratório deve demonstrar raciocínio temporal e capacidade de justificar por que eventos pertencem — ou não — ao mesmo caso.

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
