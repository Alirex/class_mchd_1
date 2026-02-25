import re
from re import Pattern
from typing import Final

# Use verbose regex pattern with comments for better readability
WORD_PATTERN: Final[Pattern[str]] = re.compile(
    r"""
    \b          # Word boundary
    \w+         # One or more word characters
    \b          # Word boundary
""",
    re.VERBOSE,
)


def get_all_words(text: str) -> list[str]:
    """Get all words from a string."""
    return WORD_PATTERN.findall(text)
