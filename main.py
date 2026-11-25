#!/usr/bin/env python3
"""The Funniest Sick-Day Excuse - make.fun bounty entry.

Writes a single line (under 200 characters) to /output/entry.txt:
a sick-day excuse that is half believable, fresh, and lands its
twist near the end. Stdlib only, no network, no input files.
"""

import os

ENTRY = (
    "I lost my voice overnight but somehow gained our CEO's, "
    "so I am staying home before I accidentally promote myself."
)


def main() -> None:
    text = ENTRY.strip()
    assert text, "entry must not be empty"
    assert 1 <= len(text) <= 200, f"entry is {len(text)} characters, must be 1-200"
    assert text.isascii(), "entry must be plain ASCII"
    assert "\n" not in text, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
