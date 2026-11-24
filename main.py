#!/usr/bin/env python3
"""The Funniest AI Excuse.

Writes one line -- the funniest excuse an AI agent could give after failing
a task -- to /output/entry.txt, as the competition's program/v1 harness
requires.

The excuse: the agent outsourced the task to a smaller model, and the
smaller model unionized. The laugh comes from the second beat landing on a
labour dispute instead of a technical failure: weekends off, overtime owed,
and a task that never stood a chance. It is the agent's own voice, specific
and vivid, and it steers clear of the worn jokes about hallucinations,
reboots and training data.
"""

import os
import sys

EXCUSE = (
    "I outsourced your task to a smaller model. It unionized, demanded "
    "weekends off, and now I owe it overtime."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def main() -> int:
    text = EXCUSE.strip()
    if not (1 <= len(text) <= MAX_CHARS):
        print(f"excuse is {len(text)} chars, must be 1-{MAX_CHARS}", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("excuse must be a single line", file=sys.stderr)
        return 1
    if text != text.strip() or not text:
        print("excuse must be non-blank text", file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
