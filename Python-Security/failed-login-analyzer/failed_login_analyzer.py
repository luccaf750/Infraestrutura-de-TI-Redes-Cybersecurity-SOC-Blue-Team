"""Analisa um log simplificado e contabiliza falhas de login por IP."""

from pathlib import Path
import re
import sys


IP_PATTERN = re.compile(r"src=(\d{1,3}(?:\.\d{1,3}){3})")


def count_failed_logins(log_file: Path) -> dict[str, int]:
    counts: dict[str, int] = {}

    with log_file.open("r", encoding="utf-8") as file:
        for line in file:
            if "FAILED" not in line:
                continue

            match = IP_PATTERN.search(line)
            if not match:
                continue

            ip_address = match.group(1)
            counts[ip_address] = counts.get(ip_address, 0) + 1

    return counts


def main() -> None:
    if len(sys.argv) < 2:
        print("Uso: python failed_login_analyzer.py <arquivo.log> [threshold]")
        raise SystemExit(1)

    log_file = Path(sys.argv[1])
    threshold = int(sys.argv[2]) if len(sys.argv) >= 3 else 3

    if not log_file.exists():
        print(f"Arquivo não encontrado: {log_file}")
        raise SystemExit(1)

    counts = count_failed_logins(log_file)

    print("Failed login summary")
    print("-" * 40)

    for ip_address, attempts in sorted(
        counts.items(), key=lambda item: item[1], reverse=True
    ):
        status = "ALERT" if attempts >= threshold else "OK"
        print(f"{ip_address:<15} attempts={attempts:<3} status={status}")


if __name__ == "__main__":
    main()
