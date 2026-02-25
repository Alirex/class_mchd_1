import re
from dataclasses import dataclass
from typing import Final

EMAIL_PATTERN: Final[re.Pattern[str]] = re.compile(
    r"""
    ^                   # Start of the string
    (?P<local>[\w\.-]+)  # One or more word characters, dots, or hyphens (username)
    @                   # At symbol
    (?P<domain>[\w\.-]+) # One or more word characters, dots, or hyphens (domain)
    \.                  # Dot before the top-level domain
    (?P<tld>\w+)         # One or more word characters (top-level domain)
    $                   # End of the string
""",
    re.VERBOSE,
)


def check_is_email_valid(email: str) -> bool:
    """Validate an email address using a regex pattern."""
    return bool(EMAIL_PATTERN.match(email))


@dataclass
class EmailParsed:
    local: str
    domain: str
    tld: str


def parse_email(email: str) -> EmailParsed | None:
    """Parse an email address into its components."""
    match = EMAIL_PATTERN.match(email)
    if match:
        return EmailParsed(
            local=match.group("local"),
            domain=match.group("domain"),
            tld=match.group("tld"),
        )
    return None
