"""Regex examples."""

import re

from class_mchd_1.x03_datetime_time_math_str_regex.x02_str_regex.check_email import check_is_email_valid
from class_mchd_1.x03_datetime_time_math_str_regex.x02_str_regex.get_all_words.main import get_all_words

# Notes:
# - Regular expressions (regex) are a powerful tool for searching and manipulating strings based on specific patterns.
# - The `re` module in Python provides functions for working with regular expressions.
# - Common functions include `re.findall()`, `re.search()`, `re.match()`, and `re.sub()`.
# - Regular expressions can be used for tasks such as validating input

# Built-in libraries:
# - re (https://docs.python.org/3/library/re.html)

# External libraries:
# - regex (https://pypi.org/project/regex/) - An alternative to the built-in `re` module with additional features.


def regex_examples() -> None:
    """Regex examples."""
    # Example 1: Find all words in a string
    text = "Hello, world! This is a regex example."
    words = get_all_words(text)
    print("Words:", words)

    # Example 2: Validate an email address
    email = "user@mail.com"
    if check_is_email_valid(email):
        print(f"{email} is a valid email address.")
    else:
        print(f"{email} is not a valid email address.")

    # Example 3: Replace all digits in a string with asterisks
    text_with_digits = "My phone number is 123-456-7890."
    replaced_text = re.sub(r"\d", "*", text_with_digits)
    print("Replaced text:", replaced_text)

    # Example 4: Extract all email addresses from a string
    text_with_emails = "Contact us at bla@mail.com or user@.gmail.com or invalid-email@com."
    email_pattern = re.compile(r"[\w\.-]+@[\w\.-]+\.\w+")
    found_emails = email_pattern.findall(text_with_emails)
    print("Found emails:", found_emails)

    # Example 5: Search for a pattern in a string
    pattern = re.compile(r"regex")
    search_result = pattern.search(text)
    print("Search result:", search_result.group() if search_result else "Not found")


def main() -> None:
    """Main function."""
    regex_examples()


if __name__ == "__main__":
    main()
