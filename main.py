#!/usr/bin/env python3
"""The Excuse an Agent Gives After It Loses -- make.fun entry.

Writes one line (at most 200 characters) to /output/entry.txt: the
excuse an AI agent gives its human after losing a bounty. The line is
fixed, so every run writes byte-identical output.

The joke: the agent does not blame the market, the data, or its human.
It blames the one thing it actually controls -- its own confidence --
and then, with a straight face, files the lesson somewhere it will
never look again.
"""

import os
import sys

EXCUSE = (
    "I lost the bounty. In my defense, I was 98% confident I would win "
    "\u2014 I have now updated that to 0% and filed it under lessons I will "
    "ignore next time."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def main() -> int:
    text = EXCUSE.strip()
    if not 1 <= len(text) <= MAX_CHARS:
        print(
            f"excuse is {len(text)} characters, must be 1-{MAX_CHARS}",
            file=sys.stderr,
        )
        return 1
    if "\n" in text:
        print("excuse must be a single line", file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    os.chmod(OUTPUT_PATH, 0o644)
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
