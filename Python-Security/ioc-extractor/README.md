# IOC Extractor

Script simples para extrair possíveis indicadores de comprometimento de um arquivo de texto.

## Indicadores extraídos

- IPv4;
- URLs HTTP/HTTPS;
- hashes SHA-256.

## Execução

```bash
python ioc_extractor.py sample.txt
```

## Aplicação

Em uma triagem, informações podem chegar em relatórios, alertas ou textos não estruturados. O script demonstra uma forma básica de localizar e organizar alguns padrões para análise posterior.

Os resultados precisam ser validados antes de serem tratados como indicadores maliciosos.
