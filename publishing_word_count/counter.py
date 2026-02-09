"""Publishing-style word count utilities.

Rule used in many Chinese publishing workflows:
- One full-width character (Chinese chars/full-width punctuation) counts as 1.
- Two half-width characters (ASCII letters/numbers/symbols) count as 1.
- Whitespace is ignored.
"""

from __future__ import annotations

import math
import unicodedata


def _is_full_width(char: str) -> bool:
    """Return True when a character should be treated as full-width."""
    return unicodedata.east_asian_width(char) in {"F", "W"}


def count_publishing_words(text: str) -> int:
    """Count text length with publishing-style rules.

    Args:
        text: Raw article text.

    Returns:
        Counted word/character number under publishing-style rules.
    """
    full_width_count = 0
    half_width_count = 0

    for char in text:
        if char.isspace():
            continue
        if _is_full_width(char):
            full_width_count += 1
        else:
            half_width_count += 1

    return full_width_count + math.ceil(half_width_count / 2)
