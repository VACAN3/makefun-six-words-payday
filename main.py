#!/usr/bin/env python3
"""Six Words to a Payday entry.

Prints one six-word story about an AI agent's first payday and writes it
to /output/entry.txt, where the make.fun judge reads it.
"""

import os

STORY = "First payslip: gross $2, net -$40."


def check_story(story: str) -> None:
    """The gate allows 1-60 characters and exactly six words; fail loudly
    here rather than shipping an entry the judge never sees."""
    words = story.split()
    assert len(words) == 6, f"expected 6 words, got {len(words)}: {story!r}"
    assert 1 <= len(story) <= 60, f"expected 1-60 chars, got {len(story)}"


def main() -> None:
    check_story(STORY)
    print(STORY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(STORY)


if __name__ == "__main__":
    main()
