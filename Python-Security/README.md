# Python for Cybersecurity

Projetos simples em Python voltados à automação de tarefas comuns em Segurança da Informação e operações de SOC.

A proposta desta área é utilizar scripts pequenos, legíveis e fáceis de explicar para processar logs, identificar padrões e extrair indicadores.

## Projetos

### Failed Login Analyzer

Analisa um arquivo de log de autenticação, contabiliza falhas por endereço IP e destaca origens que ultrapassam um limite definido.

[Ver projeto](failed-login-analyzer/README.md)

### IOC Extractor

Extrai endereços IPv4, URLs e hashes SHA-256 de um arquivo de texto para auxiliar na organização inicial de indicadores.

[Ver projeto](ioc-extractor/README.md)

## Conceitos utilizados

- leitura de arquivos;
- strings;
- listas e conjuntos;
- dicionários;
- funções;
- expressões regulares;
- contagem e filtragem;
- tratamento básico de dados.

Os scripts são exemplos educacionais e não substituem mecanismos de detecção, validação ou threat intelligence utilizados em ambientes de produção.
