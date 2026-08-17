# Network Segmentation

## Objetivo

Separar ativos com funções e níveis de confiança diferentes.

## Exemplo

```text
VLAN 10 - Management
VLAN 20 - Corporate Users
VLAN 30 - CCTV
VLAN 40 - Guest
```

## Política conceitual

| Origem | Destino | Política |
|---|---|---|
| Management | Network Devices | Allow required management |
| Users | CCTV | Deny by default |
| Guest | Internal Networks | Deny |
| CCTV | Users | Deny by default |
| CCTV | Required Services | Allow only required traffic |

## Benefícios

- redução de movimento lateral;
- menor superfície de comunicação;
- separação de dispositivos IoT/CFTV;
- controle de acesso entre zonas;
- melhor capacidade de monitoramento;
- aplicação de políticas específicas por segmento.

## Princípio

A existência de VLANs por si só não representa controle de segurança completo. O tráfego entre segmentos precisa ser controlado por roteamento, ACLs ou firewall conforme a arquitetura.
