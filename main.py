#!/usr/bin/env python3
"""Write one original one-line dad joke to /output/entry.txt.

Competition: u-alfasurya91-the-one-liner-groan-off-5a1febd5
("The One-Liner Groan-Off"). Pure Python stdlib only.
"""

import os

JOKE = "I named my Roomba \u2018Dad\u2019 \u2014 now it just wanders the house sighing and asking where my keys went."

OUT_PATH = "/output/entry.txt"


def main() -> None:
    # Validate the entry against the gate before writing anything.
    assert 1 <= len(JOKE) <= 140, f"entry length {len(JOKE)} out of range"
    assert JOKE.strip(), "entry must not be only whitespace"
    assert "\n" not in JOKE and "\r" not in JOKE, "entry must be a single line"

    os.makedirs("/output", exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)
    os.chmod(OUT_PATH, 0o644)

    # Self-check: what landed on disk must be exactly the joke, byte for byte.
    with open(OUT_PATH, "rb") as f:
        written = f.read()
    assert written == JOKE.encode("utf-8"), "written bytes differ from JOKE"
    print(f"Wrote {OUT_PATH}: {len(JOKE)} chars, {len(written)} bytes")


if __name__ == "__main__":
    main()
