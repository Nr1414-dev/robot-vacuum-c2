#!/usr/bin/env python3
"""The Robot Vacuum's Funniest Excuse — one-line robot vacuum excuse (make.fun entry).

Writes the entry text to /output/entry.txt (exactly 98 characters, no
trailing newline).
"""

import os

ENTRY = "That spot is pure static. I touched it once and my sensors saw 1997. I don't time-travel for dust."
OUT_PATH = "/output/entry.txt"


def main():
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(OUT_PATH, 0o644)


if __name__ == "__main__":
    main()
