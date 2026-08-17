"""Extrai padrões de IPv4, URLs e SHA-256 de um arquivo de texto."""

from pathlib import Path
import re
import sys


IP_PATTERN = re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b")
URL_PATTERN = re.compile(r"https?://[^\s]+")
SHA256_PATTERN = re.compile(r"\b[a-fA-F0-9]{64}\b")


def unique_matches(pattern: re.Pattern, text: str) -> list[str]:
    return sorted(set(pattern.findall(text)))


def main() -> None:
    if len(sys.argv) != 2:
        print("Uso: python ioc_extractor.py <arquivo.txt>")
        raise SystemExit(1)

    source = Path(sys.argv[1])

    if not source.exists():
        print(f"Arquivo não encontrado: {source}")
        raise SystemExit(1)

    text = source.read_text(encoding="utf-8")

    indicators = {
        "IPv4": unique_matches(IP_PATTERN, text),
        "URLs": unique_matches(URL_PATTERN, text),
        "SHA-256": unique_matches(SHA256_PATTERN, text),
    }

    for category, values in indicators.items():
        print(f"\n{category}")
        print("-" * 40)
        if not values:
            print("Nenhum indicador encontrado.")
            continue

        for value in values:
            print(value)


if __name__ == "__main__":
    main()
