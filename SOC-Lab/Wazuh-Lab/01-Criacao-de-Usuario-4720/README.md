# Análise de Criação de Usuário — Event ID 4720

## Objetivo

Analisar no Wazuh a criação de uma nova conta de usuário local em um endpoint Windows e identificar as principais informações registradas no evento.

## Cenário do laboratório

Foi criada uma conta local denominada `soc-test` em um ambiente Windows controlado.

Após a criação da conta, os eventos de segurança do Windows foram enviados ao Wazuh para análise.

## Evento identificado

- **Event ID:** 4720
- **Evento:** Criação de uma conta de usuário
- **Conta criada:** `soc-test`
- **Ambiente:** Windows
- **SIEM:** Wazuh

## Análise

O Event ID `4720` indica que uma nova conta de usuário foi criada no Windows.

Durante a investigação no Wazuh foi possível identificar a conta `soc-test` como alvo da operação e analisar informações relacionadas ao usuário responsável pela criação.

A criação de uma conta, isoladamente, não significa necessariamente um incidente de segurança.

Em um ambiente corporativo, o analista deve verificar se a criação foi autorizada e correlacionar o evento com outras atividades realizadas posteriormente pela nova conta.

## Correlação

A investigação não deve terminar no Event ID 4720.

Após a criação da conta `soc-test`, outros eventos podem ajudar a entender o comportamento da conta, como:

- inclusão em grupos privilegiados;
- autenticações realizadas pela conta;
- alterações de privilégios;
- outras atividades administrativas.

No laboratório, a conta `soc-test` foi posteriormente adicionada ao grupo local `Administradores`, gerando o Event ID `4732`.

## Classificação

**Atividade legítima em ambiente controlado de laboratório.**

O evento foi gerado intencionalmente para fins de estudo e análise utilizando o Wazuh.

## Conclusão

O laboratório demonstrou como o Wazuh pode ser utilizado para identificar a criação de novas contas em endpoints Windows.

O Event ID 4720 é relevante para monitoramento porque a criação não autorizada de usuários pode representar uma etapa de persistência ou preparação para outras atividades maliciosas.

A análise também demonstrou a importância de correlacionar diferentes eventos em vez de avaliar cada alerta de forma isolada.

## Evidências

As evidências coletadas no Wazuh serão adicionadas nesta seção.
