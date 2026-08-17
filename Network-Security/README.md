# 🌐 Network Security — VLAN, Firewall & Segmentation

Projeto de laboratório voltado para segurança de redes, segmentação lógica e controle de acesso entre diferentes zonas da infraestrutura.

## 🎯 Objetivos

- Planejar segmentação por VLAN
- Definir regras de firewall
- Separar usuários, administração e CFTV
- Aplicar princípio do menor privilégio
- Documentar fluxo de tráfego e regras

## 🏗️ Arquitetura proposta

```text
Internet
   │
Firewall / MikroTik
   │
   ├── VLAN 10 — Administração
   ├── VLAN 20 — Usuários
   ├── VLAN 30 — CFTV
   └── VPN — Acesso Remoto
```

## 🔐 Controles de segurança

- Bloqueio de tráfego lateral desnecessário
- Regras específicas entre VLANs
- Acesso administrativo restrito
- VPN para acesso remoto
- Registro de eventos de firewall
- Segmentação de dispositivos de CFTV

## 🧰 Tecnologias e conceitos

`MikroTik` `TCP/IP` `VLAN` `VPN` `Firewall` `Routing` `Network Segmentation` `Least Privilege`
