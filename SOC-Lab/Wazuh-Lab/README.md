Laboratório Wazuh — SOC / Blue Team

Laboratório prático de monitoramento, detecção e investigação de eventos de segurança utilizando o Wazuh SIEM em um ambiente Windows controlado.

O projeto foi desenvolvido para consolidar conhecimentos relacionados à rotina de um Analista SOC / Blue Team, passando por análise de eventos do Windows, autenticação, privilégios, persistência, PowerShell, reconhecimento, indicadores de comprometimento, correlação de eventos, engenharia de detecção e investigação de incidentes.

Objetivos

Praticar monitoramento e análise de eventos em SIEM.

Desenvolver raciocínio de triagem e investigação SOC.

Interpretar eventos de segurança do Windows.

Correlacionar múltiplos eventos para identificar comportamentos suspeitos.

Relacionar atividades observadas com o MITRE ATT&CK.

Trabalhar com IOC, hashes, FIM e regras personalizadas.

Documentar evidências, hipóteses, conclusões e recomendações.

Construir um portfólio prático voltado a SOC, Blue Team e Cybersecurity.

Ambiente do laboratório

Componente

Utilização

Wazuh SIEM

Coleta, correlação e análise de eventos

Wazuh Dashboard

Investigação e visualização dos alertas

Wazuh Agent

Monitoramento do endpoint

Windows

Endpoint monitorado

Windows Security Event Logs

Fonte principal de eventos

PowerShell

Simulações controladas e análise de execução

VirtualBox

Ambiente virtualizado

MITRE ATT&CK

Classificação de técnicas e comportamentos

Fluxo de investigação

O processo utilizado nos laboratórios segue uma abordagem semelhante à rotina de triagem de um SOC:

Atividade no endpoint
        ↓
Geração de evento
        ↓
Coleta pelo Wazuh Agent
        ↓
Processamento / regra
        ↓
Alerta no Wazuh
        ↓
Triagem
        ↓
Investigação
        ↓
Correlação com outros eventos
        ↓
MITRE ATT&CK / IOC / contexto
        ↓
Classificação
        ↓
Conclusão e documentação

Durante cada investigação são analisados, quando disponíveis:

Event ID

Rule ID

nível do alerta

usuário

hostname

processo

linha de comando

endereço IP

timestamp

origem do evento

eventos anteriores e posteriores

possíveis indicadores de comprometimento

técnica MITRE ATT&CK relacionada

Laboratórios

Fundamentos — Windows Event Logs e autenticação

01 — Criação de usuário — Event ID 4720

Detecção e investigação da criação de uma nova conta local no Windows.

Foco: gerenciamento de contas, identificação do responsável pela ação e contexto do evento.

Ver laboratório

02 — Inclusão em grupo privilegiado — Event ID 4732

Análise da inclusão de uma conta no grupo local Administradores.

Foco: alteração de privilégios e identificação de possíveis ações de privilege escalation.

Ver laboratório

03 — Logon bem-sucedido — Event ID 4624

Investigação de autenticação bem-sucedida no Windows.

Foco: usuário, SID, Logon ID, tipo de logon e contexto da autenticação.

Ver laboratório

04 — Falha de logon — Event ID 4625

Análise de tentativas malsucedidas de autenticação.

Foco: motivo da falha, usuário, origem e identificação de padrões anômalos.

Ver laboratório

05 — Detecção de força bruta

Correlação de múltiplas falhas de autenticação para identificar comportamento compatível com tentativa de força bruta.

Foco: frequência, janela temporal, origem e correlação de eventos.

Ver laboratório

Execução, persistência e comportamento suspeito

06 — PowerShell suspeito

Monitoramento e análise de execução de comandos PowerShell.

MITRE ATT&CK: T1059.001 — PowerShell

Ver laboratório

07 — Persistência por Scheduled Task

Análise de criação de tarefa agendada como possível mecanismo de persistência.

MITRE ATT&CK: T1053.005 — Scheduled Task/Job: Scheduled Task

Ver laboratório

08 — Criação de serviço — Event ID 7045

Investigação da instalação de um novo serviço no Windows.

Foco: persistência, nome do serviço, executável associado e contexto da criação.

Ver laboratório

Reconhecimento e análise de rede

09 — Port Scan / Reconhecimento

Identificação de comportamento de reconhecimento e varredura de portas.

MITRE ATT&CK: T1046 — Network Service Discovery

Ver laboratório

10 — Análise de tráfego PCAP

Análise de tráfego de rede a partir de captura PCAP.

Foco: protocolos, hosts, conexões e identificação de comportamento anômalo.

Ver laboratório

Threat Intelligence, MITRE e correlação

11 — IOC / Threat Intelligence

Utilização de indicadores de comprometimento para enriquecer uma investigação.

Foco: IP, domínio, hash e contexto de ameaça.

Ver laboratório

12 — MITRE ATT&CK

Mapeamento de comportamentos observados no laboratório para técnicas e táticas do MITRE ATT&CK.

Foco: transformar eventos técnicos em contexto de ataque.

Ver laboratório

13 — Correlação de eventos

Análise conjunta de diferentes eventos para identificar uma sequência potencialmente suspeita.

Foco: timeline, contexto e redução da análise isolada de alertas.

Ver laboratório

14 — Investigação de incidente

Investigação estruturada de um alerta utilizando evidências coletadas no ambiente.

Foco: triagem, análise, classificação e conclusão.

Ver laboratório

15 — Desafio Final SOC L1

Cenário consolidado para aplicação dos conhecimentos desenvolvidos nos laboratórios anteriores.

Foco: análise semelhante ao fluxo de trabalho de um Analista SOC Nível 1.

Ver laboratório

Engenharia de detecção e investigação avançada

16 — File Integrity Monitoring (FIM)

Monitoramento de criação e alteração de arquivos em diretórios acompanhados pelo Wazuh.

Foco: integridade de arquivos, hashes e alterações não autorizadas.

Ver laboratório

17 — Detecção por IOC / Hash

Análise de hash de arquivo e comparação com indicador de comprometimento controlado.

Foco: SHA-256, IOC e enriquecimento de alerta.

Ver laboratório

18 — Regra personalizada no Wazuh

Desenvolvimento e validação de regra local para identificação de comportamento específico.

Foco: detection engineering, lógica de regras e redução de falsos positivos.

Ver laboratório

19 — Investigação completa de incidente

Investigação estruturada utilizando alerta, contexto, timeline e eventos relacionados.

Foco: responder o que aconteceu, quando, onde, com quem e como.

Ver laboratório

20 — Incidente correlacionado

Construção de uma narrativa de incidente a partir da correlação de múltiplos eventos.

Exemplo de cadeia analisada:

4625 → 4624 → 4720 → 4732

Falhas de logon
      ↓
Autenticação bem-sucedida
      ↓
Criação de nova conta
      ↓
Inclusão em grupo privilegiado

Foco: correlação temporal, hipótese de comprometimento, impacto e resposta.

Ver laboratório

Competências desenvolvidas

Este laboratório trabalha, de forma prática, competências relacionadas a:

SOC / Security Operations Center

Blue Team

SIEM

Wazuh

Windows Security Event Logs

Log Analysis

Incident Triage

Incident Investigation

Event Correlation

Threat Intelligence

Indicators of Compromise — IOC

File Integrity Monitoring — FIM

Detection Engineering

PowerShell Monitoring

Network Analysis

PCAP Analysis

MITRE ATT&CK

documentação técnica de incidentes

Metodologia

Cada laboratório procura seguir o mesmo ciclo operacional:

Definir o comportamento ou evento a ser analisado.

Gerar ou documentar uma atividade controlada.

Identificar a telemetria disponível.

Localizar o evento ou alerta no SIEM.

Analisar campos relevantes.

Buscar contexto e eventos relacionados.

Relacionar a atividade com MITRE ATT&CK quando aplicável.

Avaliar possíveis falsos positivos.

Classificar o comportamento.

Documentar evidências e conclusão.

Observação sobre as evidências

Os primeiros laboratórios foram construídos a partir da análise do ambiente Wazuh e dos eventos produzidos durante as atividades práticas.

Alguns materiais adicionados posteriormente incluem imagens demonstrativas explicitamente identificadas como SIMULAÇÃO / DEMO. Essas imagens têm finalidade de documentação e representação visual do fluxo analítico e não são apresentadas como capturas reais do ambiente.

Essa distinção é mantida para preservar a transparência técnica do portfólio.

Resultado do projeto

Ao final da sequência, o laboratório cobre diferentes etapas encontradas em operações de segurança:

Coleta
  ↓
Detecção
  ↓
Triagem
  ↓
Investigação
  ↓
Correlação
  ↓
Threat Intelligence
  ↓
Mapeamento MITRE ATT&CK
  ↓
Classificação
  ↓
Documentação

O objetivo não é apenas gerar alertas, mas desenvolver a capacidade de interpretar evidências, correlacionar eventos e explicar tecnicamente uma investigação de segurança.

Finalidade

Projeto desenvolvido como parte de um portfólio prático em Cybersecurity, SOC e Blue Team, com foco no desenvolvimento de competências aplicáveis a posições iniciais de SOC Analyst / Security Analyst / Blue Team.
