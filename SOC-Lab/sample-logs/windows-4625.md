# Windows Event ID 4625 - Sample Dataset

Dados de laboratório para a investigação INC-001.

```text
Time: 14:03:12
Computer: WIN11-FINANCE-01
EventID: 4625
AccountName: administrator
SourceNetworkAddress: 192.168.10.57
Status: Logon Failure

Time: 14:03:18
Computer: WIN11-FINANCE-01
EventID: 4625
AccountName: administrator
SourceNetworkAddress: 192.168.10.57
Status: Logon Failure

Time: 14:03:25
Computer: WIN11-FINANCE-01
EventID: 4625
AccountName: administrator
SourceNetworkAddress: 192.168.10.57
Status: Logon Failure

...

Time: 14:11:04
Computer: WIN11-FINANCE-01
EventID: 4625
AccountName: administrator
SourceNetworkAddress: 192.168.10.57
Status: Logon Failure
```

## Campos relevantes

- Timestamp
- Event ID
- Account Name
- Computer
- Source Network Address
- Logon Type
- Status / SubStatus

Os eventos podem ser correlacionados com o Event ID `4624` para verificar possível autenticação bem-sucedida após uma sequência de falhas.
