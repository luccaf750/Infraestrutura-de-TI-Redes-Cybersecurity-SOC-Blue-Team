# Firewall Policy - Conceptual Example

## Princípio

A política é baseada em `deny by default` entre segmentos sensíveis, liberando apenas comunicações necessárias.

## Exemplo conceitual

```text
1. Allow ESTABLISHED, RELATED
2. Allow Management -> Network Devices (required management ports)
3. Allow CCTV -> required monitoring/services
4. Deny Users -> CCTV unless explicitly required
5. Deny Guest -> Internal Networks
6. Deny unauthorized inter-VLAN traffic
7. Log selected denied traffic
```

## Cuidados

Regras reais devem ser construídas de acordo com os serviços utilizados e testadas antes da implantação.

Uma regra excessivamente ampla pode eliminar o benefício da segmentação. Uma regra excessivamente restritiva pode interromper serviços legítimos.

## Boas práticas

- documentar motivo de cada regra;
- evitar `allow any` sem justificativa;
- limitar administração por origem;
- registrar bloqueios relevantes;
- revisar regras obsoletas;
- manter backup da configuração;
- testar mudanças de forma controlada.
