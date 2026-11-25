#!/usr/bin/env python3
"""Fortune Cookie for the Liquidated Trader (make.fun).

Writes one fortune cookie line for a crypto trader who just got
liquidated to /output/entry.txt. Standard library only.
"""
import os

ENTRY = "Your lucky numbers are 0, 0, and 0 \u2014 the balance you checked at 3am."

def main():
    words = ENTRY.split()
    if len(words) > 20:
        raise SystemExit("entry exceeds 20 words: %d" % len(words))
    if not (1 <= len(ENTRY) <= 160):
        raise SystemExit("entry must be 1-160 chars: %d" % len(ENTRY))
    try:
        out_dir = "/output"
        os.makedirs(out_dir, exist_ok=True)
    except OSError:
        out_dir = "./output"
        os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print("wrote %s (%d words, %d chars)" % (
        os.path.join(out_dir, "entry.txt"), len(words), len(ENTRY)))

if __name__ == "__main__":
    main()
