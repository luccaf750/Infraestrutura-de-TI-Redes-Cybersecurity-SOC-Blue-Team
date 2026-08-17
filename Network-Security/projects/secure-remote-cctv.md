# Secure Remote CCTV Infrastructure

## Visão geral

Este projeto documenta uma arquitetura de referência para operação segura de dispositivos CFTV/IP em uma localidade remota.

O cenário combina conectividade WAN, roteamento, segmentação, regras de firewall e mecanismos de acesso remoto.

## Requisitos

- conexão principal via Starlink;
- possibilidade de link de contingência;
- roteador/firewall MikroTik;
- switch de acesso;
- câmeras IP;
- NVR ou estação de monitoramento;
- acesso remoto controlado;
- isolamento dos dispositivos CFTV da rede de usuários.

## Objetivos de segurança

1. Separar dispositivos CFTV da rede de usuários.
2. Restringir comunicação desnecessária entre segmentos.
3. Permitir somente fluxos necessários ao funcionamento.
4. Reduzir exposição direta dos dispositivos.
5. Controlar acesso administrativo.
6. Manter possibilidade de contingência de conectividade.
7. Facilitar troubleshooting sem eliminar controles de segurança.

## Arquitetura

```text
                 Primary WAN
                  Starlink
                     |
                     |
                 MikroTik
              Router / Firewall
               /      |       \
              /       |        \
       VLAN 10     VLAN 20     VLAN 30
      Management    Users       CCTV
                                  |
                               Switch
                          /       |       \
                      Camera 1 Camera 2   NVR
```

Exemplo de endereçamento:

```text
VLAN 10 - Management
192.168.10.0/24

VLAN 20 - Users
192.168.20.0/24

VLAN 30 - CCTV
192.168.30.0/24
```

Os endereços acima são exclusivamente ilustrativos.

## Controles de segurança

### Segmentação

Câmeras e NVR permanecem em segmento dedicado, reduzindo comunicação lateral com estações de usuários.

### Firewall

A política segue a ideia de permitir somente fluxos necessários e negar tráfego inter-VLAN não autorizado.

### Administração

A interface de gerenciamento dos equipamentos deve ser acessível somente a partir da rede administrativa ou de um canal remoto autorizado.

### Acesso remoto

Sempre que aplicável, o acesso administrativo remoto deve utilizar VPN em vez de exposição direta de interfaces de gerenciamento à Internet.

### Credenciais

- remover credenciais padrão;
- utilizar senhas exclusivas;
- restringir contas administrativas;
- revisar acessos periodicamente.

## Disponibilidade

Um segundo link pode ser utilizado como contingência quando o cenário exigir maior disponibilidade.

A redundância deve ser planejada considerando roteamento, failover, monitoramento e impacto sobre sessões existentes.

## Troubleshooting

Em caso de indisponibilidade, a análise pode seguir:

```text
Physical Layer
      |
WAN Connectivity
      |
Routing
      |
VLAN
      |
Firewall
      |
Switching
      |
Endpoint / Camera
      |
Application / Monitoring
```

## Resultado esperado

A arquitetura reduz exposição desnecessária, separa ativos de CFTV dos demais usuários e cria pontos claros de controle para administração, conectividade e segurança.
