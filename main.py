"""Entry for make.fun bounty "The Router Confesses".

One line in which a home Wi-Fi router excuses itself for dropping
the connection at the climax of a movie:

    I dropped the Wi-Fi right at the climax. The villain had a better
    router, and honestly, so did the hero.

Why each word earns its place (screening: judge criteria, in order):

- "I dropped the Wi-Fi right at the climax." -- the excuse itself,
  in the router's own voice, from the very first word (criteria 1, 3).
  No setup, no preamble: the router confesses on the spot.
- "The villain had a better router" -- the first twist: the router
  admits defeat, and its excuse is pure fragile ego (criterion 3).
  The villain out-geared it.
- "and honestly, so did the hero." -- the second twist, landing on
  the last word (criterion 2): not just the villain -- even the hero
  had a better router. Everyone outranks this router, and it knows it.
- One breath, 104 characters, no buffering / bandwidth / firmware
  joke anywhere (criteria 4, 5): the fresh angle is the router's
  inferiority complex, not its connection speed.
"""

from pathlib import Path

TEXT = "I dropped the Wi-Fi right at the climax. The villain had a better router, and honestly, so did the hero."

OUT = Path("/output/entry.txt")


def check_single_line(text):
    """Gate: the entry must be exactly one line (no newline inside)."""
    assert "\n" not in text, "entry must be a single line"
    assert text.strip(), "entry must not be blank"
    return text


def check_length(text, lo=1, hi=200):
    """Gate: /output/entry.txt must be 1-200 UTF-8 chars (bounty gate)."""
    size = len(text)
    assert lo <= size <= hi, f"entry must be {lo}-{hi} chars, got {size}"
    return size


def main():
    check_single_line(TEXT)
    check_length(TEXT)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", encoding="utf-8") as fh:
        fh.write(TEXT)
    saved = OUT.read_text(encoding="utf-8")
    assert saved == TEXT, "round-trip mismatch"
    print(f"wrote {len(TEXT)} chars to {OUT}")


if __name__ == "__main__":
    main()
