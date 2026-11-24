#!/usr/bin/env python3
"""One Line, One Minute: The Vending Machine Pickup Line Contest.

Writes a single pickup line, spoken by a vending machine to a passing
human, to /output/entry.txt. No network, no dependencies, deterministic.
"""
import os

LINE = (
    "I've been humming since you walked by \u2014 press B7 and I'll drop "
    "my sweetest snack. Exact change only: I can't make change for a "
    "heart like yours."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
