# Failed Login Analyzer

Script Python para analisar registros simplificados de falhas de autenticação.

## Objetivo

Contabilizar tentativas de login malsucedidas por endereço IP e identificar origens que atingem um threshold.

## Exemplo de entrada

```text
2026-08-17 14:03:12 FAILED user=administrator src=192.168.10.57
2026-08-17 14:03:18 FAILED user=administrator src=192.168.10.57
2026-08-17 14:04:02 FAILED user=finance src=192.168.10.22
```

## Execução

```bash
python failed_login_analyzer.py sample.log
```

Threshold opcional:

```bash
python failed_login_analyzer.py sample.log 3
```

## O que o código demonstra

- abertura e leitura de arquivo;
- identificação de eventos `FAILED`;
- extração de endereço de origem;
- uso de dicionário para contagem;
- ordenação dos resultados;
- aplicação de threshold.

## Observação

O formato de log é propositalmente simples para tornar o raciocínio do script fácil de acompanhar.
