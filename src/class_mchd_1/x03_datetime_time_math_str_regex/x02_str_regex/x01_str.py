"""Example for string."""


def example_str() -> None:
    """Example for string."""
    s = "Hello, World!"
    print(s)
    print(f"{s[0]=}")  # H
    print(f"{s[7:12]=}")  # World
    print(f"{s.lower()=}")  # hello, world!
    print(f"{s.casefold()=}")  # hello, world!
    print(f"{s.upper()=}")  # HELLO, WORLD!
    print(f"{s.capitalize()=}")  # Hello, world!

    print(f"{s.split(', ')=}")  # ['Hello', 'World!']

    print(f"{s.strip('!')=}")  # Hello, World

    print(f"{s.startswith('Hello')=}")  # True
    print(f"{s.endswith('!')=}")  # True

    print(f"{s.replace('World', 'Python')=}")  # Hello, Python!

    # Finding substrings
    print(f"{s.find('World')=}")  # 7
    print(f"{s.find('Python')=}")  # -1 (not found)

    if "World" in s:
        print("Found 'World' in the string.")

    # region special_characters
    # sourcery skip: extract-duplicate-method, inline-variable
    s_with_newline = "Hello,\nWorld!"
    print(s_with_newline)

    s_with_tab = "Hello,\tWorld!"
    print(s_with_tab)

    s_with_quote = 'She said, "Hello, World!"'
    print(s_with_quote)

    s_with_backslash = "This is a backslash: \\"
    print(s_with_backslash)

    s_with_unicode = "Unicode example: \u03a9"  # Omega symbol
    print(s_with_unicode)

    # emoji: ❤️
    s_with_emoji = "I love Python! ❤️"
    print(s_with_emoji)
    # endregion special_characters


def main() -> None:
    """Main function."""
    example_str()


if __name__ == "__main__":
    main()
