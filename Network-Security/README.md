# Network Security

Documentação técnica voltada à segurança de redes e infraestrutura, baseada em cenários compatíveis com atividades de conectividade, segmentação, troubleshooting e proteção de ambientes IP.

O objetivo desta área é demonstrar como conhecimentos de infraestrutura podem ser aplicados à Segurança da Informação por meio de segmentação, controle de tráfego, redução de superfície de ataque e disponibilidade.

## Projeto em destaque

### Secure Remote CCTV Infrastructure

Cenário de infraestrutura remota utilizando conectividade via Starlink, roteamento MikroTik, segmentação lógica, firewall e dispositivos CFTV/IP.

O projeto aborda:

- segmentação de dispositivos;
- regras de firewall;
- princípio do menor privilégio;
- acesso remoto;
- isolamento de CFTV/IP;
- redundância de conectividade;
- monitoramento e troubleshooting.

[Ver documentação do projeto](projects/secure-remote-cctv.md)

## Arquitetura de referência

```text
                    Internet
                       |
                  Starlink WAN
                       |
                   MikroTik
                 /     |      \
                /      |       \
        Management    Users    CCTV VLAN
           VLAN        VLAN        |
                                  Switch
                               /    |    \
                           Camera Camera NVR
```

## Conceitos abordados

- TCP/IP
- MikroTik
- VLAN
- Firewall
- VPN
- DHCP
- Routing
- NAT
- Network Segmentation
- Least Privilege
- Defense in Depth
- CFTV/IP
- Starlink
- Redundância de conectividade

## Conteúdo

- [Secure Remote CCTV Infrastructure](projects/secure-remote-cctv.md)
- [Network Segmentation](projects/network-segmentation.md)
- [Firewall Policy](config-examples/firewall-policy.md)
- [VLAN Design](config-examples/vlan-design.md)
- [Network Diagram](diagrams/network-topology.md)

## Nota

A documentação utiliza endereços, nomes e topologias genéricas. Nenhuma informação de cliente, credencial ou configuração sensível de ambiente real é publicada.
