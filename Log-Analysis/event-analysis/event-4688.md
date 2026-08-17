# Event ID 4688 - Process Creation

## Descrição

O Event ID `4688` indica a criação de um novo processo quando a auditoria correspondente está habilitada.

## Campos relevantes

- New Process Name
- New Process ID
- Creator Process ID
- Creator Process Name
- Subject User Name
- Token Elevation Type
- Process Command Line, quando disponível/configurada

## O que analisar

O nome do executável sozinho raramente é suficiente.

Perguntas úteis:

- Quem iniciou o processo?
- Qual foi o processo pai?
- O caminho do executável é esperado?
- Qual command line foi utilizada?
- O processo é comum para aquele usuário?
- Houve autenticação suspeita antes da execução?
- O processo iniciou outros processos?

## Exemplo de cenário

```text
Parent Process:
explorer.exe

New Process:
powershell.exe

Command Line:
powershell.exe -ExecutionPolicy Bypass ...
```

Esse exemplo não deve ser classificado automaticamente como malicioso. PowerShell é uma ferramenta legítima de administração. O contexto, os argumentos, o usuário, a origem e as atividades posteriores precisam ser analisados.

## Possíveis usos na investigação

- execução de PowerShell;
- ferramentas administrativas;
- scripts;
- LOLBins;
- processos iniciados após comprometimento;
- comportamento anormal de aplicações.
