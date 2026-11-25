#!/usr/bin/env python3
"""Entry for The One-Liner Groan-Off.

Writes one original one-line dad joke to /output/entry.txt.
Deterministic: the line is a fixed literal, no network, no randomness,
no reads outside this repository.
"""

import os
import sys

JOKE = "I told the fridge to chill, and now it won't stop giving me the cold shoulder."


def main() -> int:
    # Guard the gate at build time: the entry must be 1-140 chars, one line.
    if not (1 <= len(JOKE) <= 140) or "\n" in JOKE or not JOKE.strip():
        print("entry line fails the 1-140 char gate", file=sys.stderr)
        return 1
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
