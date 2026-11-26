#!/usr/bin/env python3
"""The Robot Vacuum's Funniest Excuse — one-line robot vacuum excuse (make.fun entry).

Writes the entry text to /output/entry.txt (exactly 98 characters, no
trailing newline).
"""

import os

ENTRY = "That spot is pure static. I touched it once and my sensors saw 1997. I don't time-travel for dust."
OUT_PATH = "/output/entry.txt"


def validate_entry(entry):
    if not isinstance(entry, str):
        raise ValueError("entry must be a string")
    if not 1 <= len(entry) <= 120:
        raise ValueError("entry must be 1-120 characters")
    if not entry.strip():
        raise ValueError("entry must not be blank")


def main():
    validate_entry(ENTRY)
    if not ENTRY.startswith("That spot is pure static"):
        raise ValueError("entry must start with 'That spot is pure static'")
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(OUT_PATH, 0o644)
    with open(OUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    if written != ENTRY or len(written.encode("utf-8")) != len(ENTRY.encode("utf-8")):
        raise ValueError("written entry does not match ENTRY")


if __name__ == "__main__":
    main()
