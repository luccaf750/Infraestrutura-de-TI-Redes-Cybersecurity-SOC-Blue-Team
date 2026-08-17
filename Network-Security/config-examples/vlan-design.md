# VLAN Design

## Exemplo de segmentação

```text
VLAN 10 - Management - 192.168.10.0/24
VLAN 20 - Users      - 192.168.20.0/24
VLAN 30 - CCTV       - 192.168.30.0/24
VLAN 40 - Guest      - 192.168.40.0/24
```

## Management

Destinada à administração de roteadores, switches e outros ativos de infraestrutura.

## Users

Estações e dispositivos corporativos de usuários.

## CCTV

Câmeras, NVRs e equipamentos associados ao sistema de monitoramento.

## Guest

Dispositivos sem necessidade de acesso aos recursos internos.

## Segurança

VLAN é um mecanismo de segmentação lógica. O controle efetivo de comunicação entre segmentos depende da política aplicada no equipamento responsável pelo roteamento entre as VLANs.
