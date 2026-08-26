# Laboratório 05 — Detecção de Força Bruta no Wazuh

## Objetivo

Este laboratório tem como objetivo simular e detectar múltiplas falhas de autenticação em um endpoint Windows utilizando o Wazuh SIEM.

A partir de eventos reais de falha de logon do Windows, foi criada uma regra customizada de correlação no Wazuh para identificar várias tentativas de autenticação malsucedidas direcionadas ao mesmo usuário dentro de uma janela de tempo definida.

O objetivo é reproduzir uma situação compatível com uma tentativa de força bruta e gerar um alerta de maior severidade para investigação por um analista SOC.

---

## Ambiente

- SIEM: Wazuh 4.14.7
- Endpoint: Windows
- Agente monitorado: `soc-lab-windows`
- Fonte dos eventos: Windows Security Event Log
- Event ID monitorado: `4625`
- Regra Wazuh original: `60122`
- Regra customizada: `100100`
- Nível do alerta customizado: `10`

---

## Evento base — Windows Event ID 4625

O Windows Event ID `4625` é gerado quando ocorre uma tentativa de logon que não é concluída com sucesso.

Durante o laboratório foram realizadas múltiplas tentativas controladas de autenticação utilizando uma senha incorreta.

Os eventos foram coletados pelo agente Wazuh instalado no endpoint Windows.

### Informações observadas

| Campo | Valor |
|---|---|
| Event ID | 4625 |
| Usuário alvo | Lucas |
| Tipo de Logon | 2 |
| Endereço de origem | 127.0.0.1 |
| Processo | `C:\Windows\System32\svchost.exe` |
| Status | `0xC000006D` |
| Substatus | `0xC000006A` |
| Regra Wazuh | 60122 |
| Nível | 5 |

O código `0xC000006D` indica falha de autenticação, enquanto o substatus `0xC000006A` está relacionado à utilização de senha incorreta.

O Logon Type `2` representa uma tentativa de logon interativo no próprio equipamento.

---

## Identificação das múltiplas falhas

Inicialmente, cada tentativa malsucedida foi identificada individualmente pelo Wazuh através da regra `60122`:

```text
Logon Failure - Unknown user or bad password
```

Nível do alerta:

```text
5
```

Uma ocorrência isolada desse evento pode representar apenas um erro legítimo do usuário.

Entretanto, múltiplas falhas direcionadas ao mesmo usuário em um curto intervalo de tempo podem indicar uma tentativa de descoberta de credenciais por força bruta.

---

## Criação da regra customizada

Para correlacionar as falhas consecutivas de autenticação, foi criada uma regra personalizada no arquivo:

```text
/var/ossec/etc/rules/local_rules.xml
```

Regra utilizada:

```xml
<group name="windows,authentication_failed,">

  <rule id="100100" level="10" frequency="5" timeframe="60">
    <if_matched_sid>60122</if_matched_sid>
    <same_field>data.win.eventdata.targetUserName</same_field>
    <description>Possível ataque de força bruta: múltiplas falhas de logon para o mesmo usuário</description>
    <mitre>
      <id>T1110</id>
    </mitre>
  </rule>

</group>
```

---

## Lógica da detecção

A regra customizada utiliza os seguintes parâmetros:

### `if_matched_sid`

```xml
<if_matched_sid>60122</if_matched_sid>
```

Determina que a regra customizada será baseada nos eventos previamente identificados pela regra Wazuh `60122`.

### `frequency`

```text
5
```

Define a quantidade de ocorrências necessárias para a correlação.

### `timeframe`

```text
60
```

Define a janela temporal de 60 segundos para análise das ocorrências.

### `same_field`

```text
data.win.eventdata.targetUserName
```

Determina que as falhas devem estar relacionadas ao mesmo usuário alvo.

### `level`

```text
10
```

Eleva a severidade do alerta após a identificação do padrão de múltiplas falhas de autenticação.

---

## Validação da configuração

Após a criação da regra, a configuração do Wazuh foi validada antes da reinicialização do serviço.

Foi utilizado:

```bash
sudo /var/ossec/bin/wazuh-analysisd -t
```

Em seguida, o Wazuh Manager foi reiniciado:

```bash
sudo systemctl restart wazuh-manager
```

O estado do serviço foi verificado com:

```bash
sudo systemctl status wazuh-manager
```

O serviço permaneceu:

```text
active (running)
```

---

## Simulação

Foram realizadas múltiplas tentativas de autenticação com senha incorreta no endpoint Windows.

O Wazuh registrou sucessivamente eventos correspondentes à regra `60122`.

Após atingir o critério de correlação definido na regra personalizada, o Wazuh gerou o alerta:

```text
Possível ataque de força bruta: múltiplas falhas de logon para o mesmo usuário
```

---

## Resultado da detecção

O alerta customizado apresentou:

| Campo | Valor |
|---|---|
| Regra | 100100 |
| Nível | 10 |
| Frequência | 5 |
| Usuário correlacionado | Mesmo usuário alvo |
| MITRE ATT&CK | T1110 |
| Tática | Credential Access |
| Técnica | Brute Force |

Isso demonstra que o SIEM conseguiu correlacionar eventos individuais de autenticação e transformar várias ocorrências de menor severidade em um alerta de maior prioridade.

---

## Evidência

A captura abaixo apresenta o alerta gerado pelo Wazuh após a correlação das falhas de autenticação.

![Alerta de força bruta detectado pela regra 100100](./evidencia-regra-100100-brute-force.png)

**Evidência 01 — Regra customizada `100100`, nível `10`, identificando múltiplas falhas de logon e associando a detecção à técnica MITRE ATT&CK `T1110 — Brute Force`.**

---

## MITRE ATT&CK

A detecção foi associada à técnica:

**T1110 — Brute Force**

Tática:

**Credential Access**

Essa técnica representa tentativas de obtenção de acesso a contas através de múltiplas tentativas de autenticação.

---

## Perspectiva de análise SOC

Em um ambiente corporativo, um alerta semelhante exigiria investigação adicional.

O analista SOC deveria avaliar fatores como:

- quantidade de tentativas;
- intervalo entre as autenticações;
- usuário alvo;
- origem das tentativas;
- equipamento envolvido;
- histórico de autenticação;
- ocorrência de logon bem-sucedido após as falhas;
- outros alertas relacionados ao mesmo endpoint ou usuário.

Um logon bem-sucedido imediatamente após uma sequência de falhas também poderia elevar a prioridade da investigação, pois poderia indicar comprometimento das credenciais.

---

## Possíveis ações de resposta

Dependendo do contexto e da política de segurança da organização, algumas ações poderiam incluir:

1. validar a atividade com o usuário;
2. analisar os eventos de autenticação relacionados;
3. verificar a origem das tentativas;
4. avaliar outros endpoints associados;
5. bloquear temporariamente a conta ou origem, quando aplicável;
6. solicitar redefinição de senha;
7. verificar a existência de outros indicadores de comprometimento;
8. documentar e escalar o incidente conforme o procedimento do SOC.

---

## Conclusão

O laboratório demonstrou a criação de uma detecção customizada no Wazuh para identificar múltiplas falhas de autenticação relacionadas ao mesmo usuário.

Durante o exercício foram realizadas:

- análise de eventos Windows;
- identificação do Event ID `4625`;
- análise da regra Wazuh `60122`;
- criação da regra customizada `100100`;
- correlação de eventos;
- definição de frequência e janela temporal;
- ajuste de severidade;
- associação com MITRE ATT&CK;
- validação da configuração;
- geração e análise do alerta.

O exercício demonstra como eventos aparentemente isolados podem ser correlacionados por um SIEM para identificar padrões de comportamento potencialmente malicioso, aproximando o laboratório de atividades executadas em operações de SOC e Blue Team.
