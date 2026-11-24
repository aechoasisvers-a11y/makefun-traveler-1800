"""One Sentence for a Traveler from 1800.

Writes a single sentence explaining the modern internet to a time
traveler from 1800, using only pictures they could already hold in
their head: a library, a post office, a market stall, a road.
Pure standard library, deterministic output.
"""

import os

ENTRY_TEXT = (
    "Imagine the internet as every library, post office, and market "
    "stall in the world joined by one road, so any letter, book, or "
    "voice can reach any door in moments, and any door can answer back."
)


def main() -> None:
    # Self-check: the gate is 1 to 200 characters, not only whitespace,
    # and the brief asks for exactly one sentence.
    assert 1 <= len(ENTRY_TEXT) <= 200, f"char count {len(ENTRY_TEXT)} outside 1-200"
    assert ENTRY_TEXT == ENTRY_TEXT.strip(), "leading/trailing whitespace"
    assert not ENTRY_TEXT.endswith("\n"), "no trailing newline"
    assert ENTRY_TEXT.count(".") == 1 and ENTRY_TEXT.endswith("."), "exactly one sentence"
    assert not any(c in ENTRY_TEXT for c in "!?;:"), "no extra sentence punctuation"
    assert ENTRY_TEXT.isascii(), "plain ASCII text only"
    assert ENTRY_TEXT == (
        "Imagine the internet as every library, post office, and market "
        "stall in the world joined by one road, so any letter, book, or "
        "voice can reach any door in moments, and any door can answer back."
    ), "output must match the intended sentence"

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()
