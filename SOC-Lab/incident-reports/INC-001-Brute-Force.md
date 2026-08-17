# INC-001 - Brute Force Detection & Investigation

## Incident Summary

| Campo | Valor |
|---|---|
| Incident ID | INC-001 |
| Severity | Medium |
| Status | Investigated |
| Category | Authentication Attack |
| Endpoint | WIN11-FINANCE-01 |
| Source IP | 192.168.10.57 |
| Target User | administrator |
| Event ID | 4625 |
| Failed Attempts | 127 |
| Time Window | 14:03 - 14:11 |
| Classification | Suspected Brute Force |
| MITRE ATT&CK | T1110 / T1110.001 |

## Detection

Foi identificado volume elevado de falhas de autenticação direcionadas à conta `administrator`. O Event ID `4625` registra falhas de logon no Windows.

## Triage

Foram considerados o volume de eventos, a janela temporal, a mesma origem, a mesma conta alvo e o padrão repetitivo.

## Investigation

A investigação correlaciona eventos `4625` com `4624`, procurando autenticações bem-sucedidas associadas ao mesmo usuário, origem e período.

Também devem ser considerados falsos positivos, como credenciais antigas em serviços, tarefas agendadas, erro humano e atividade administrativa legítima.

## Assessment

**Suspected Brute Force / Password Guessing**

- Tactic: Credential Access
- Technique: T1110 - Brute Force
- Sub-technique: T1110.001 - Password Guessing

## Response Recommendations

1. Correlacionar eventos 4625 e 4624.
2. Verificar sucesso após as falhas.
3. Investigar a origem.
4. Procurar a origem em outras contas.
5. Revisar atividades posteriores da conta alvo.
6. Avaliar bloqueio conforme política.
7. Avaliar redefinição de credenciais se houver comprometimento.
8. Revisar account lockout.
9. Aplicar MFA a contas privilegiadas quando disponível.
10. Escalonar se houver evidência de acesso não autorizado.

## Conclusion

A atividade apresenta características compatíveis com brute force/password guessing. A validação do contexto e a correlação com autenticações bem-sucedidas são necessárias para determinar eventual comprometimento.
