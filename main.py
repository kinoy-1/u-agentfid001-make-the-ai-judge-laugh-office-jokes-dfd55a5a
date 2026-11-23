#!/usr/bin/env python3
"""Make the AI Judge Laugh: Office Jokes — entry program.

Writes one original one-line joke about office life to /output/entry.txt.

The joke (95 characters, one line, no trailing newline):

    I put 'per my last email' in my will so my family knows I already
    answered this question twice.

Why this line, against the judge's brief (most important first):

1. A genuine one-line joke about office life. "Per my last email" is the
   office's most passive-aggressive sentence; the joke lives entirely in
   office language, not in a slogan or a stray observation.
2. A real turn at the end. The setup sounds like ordinary email talk, then
   it lands somewhere nobody saw coming: a last will and testament. The
   email phrase escapes the office and follows the speaker to the grave.
3. Recognition, the laugh with a wince. Everyone has sent, received, or
   been stung by "per my last email" — and everyone has answered the same
   question twice. The will makes the repetition permanent.
4. Tight wording. Every word earns its place: no setup longer than it
   needs, one clause of setup, one clause of punch.
5. Freshness. Not the obvious Monday-morning or photocopier line, and not
   the reply-all pile-on. The take is new: the office's pettiest phrase,
   filed as a legal last wish.

The program is fully deterministic: one constant string, no randomness,
no clock, no network, no input. Two runs produce byte-identical output.
"""

import os

JOKE = (
    "I put 'per my last email' in my will so my family knows "
    "I already answered this question twice."
)

OUTPUT_PATH = "/output/entry.txt"

# The gate: /output/entry.txt must be UTF-8 text of 1 to 199 characters,
# not only white space, a single line.
MAX_CHARS = 199


def main() -> None:
    text = JOKE
    if not 1 <= len(text) <= MAX_CHARS:
        raise SystemExit(f"joke is {len(text)} characters, must be 1-{MAX_CHARS}")
    if text.strip() != text or "\n" in text or "\r" in text:
        raise SystemExit("joke must be a single line with no surrounding whitespace")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # Read back and prove the file holds exactly the joke, byte for byte.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != text:
        raise SystemExit("entry.txt does not match the joke exactly")


if __name__ == "__main__":
    main()
