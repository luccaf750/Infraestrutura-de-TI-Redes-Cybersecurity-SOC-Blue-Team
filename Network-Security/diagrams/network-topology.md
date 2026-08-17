# Network Topology

## Diagrama lógico

```text
                        Internet
                           |
                       Starlink
                           |
                    +--------------+
                    |   MikroTik   |
                    | Router / FW  |
                    +--------------+
                     /      |      \
                    /       |       \
             VLAN 10    VLAN 20    VLAN 30
            Management    Users       CCTV
                |           |           |
          Network Admin   Clients    +--------+
                                    | Switch |
                                    +--------+
                                     /  |   \
                                    /   |    \
                                  CAM1 CAM2  NVR
```

## Zonas

**Management:** administração da infraestrutura.

**Users:** dispositivos corporativos.

**CCTV:** dispositivos de monitoramento, tratados como uma zona separada.

## Fluxos

O firewall controla a comunicação entre as zonas. A existência de conectividade física não implica permissão irrestrita entre os segmentos.
