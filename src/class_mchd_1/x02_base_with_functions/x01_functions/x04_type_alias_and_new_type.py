# %%


from typing import Final, NewType

# from typing import TypeAlias


# Name: TypeAlias = str


type Name = str
"""Name of person."""

# DRY: Don't Repeat Yourself. Avoid repeating the same code.
# WET: Write Everything Twice. The opposite of DRY. Avoid it.

Color = NewType("Color", str)
"""Favorite color of person."""


COLOR_DEFAULT: Final[Color] = Color("Blue")
"""Default color."""

Message = NewType("Message", str)
"""Message to output."""


def greeting_function(
    name: Name,
    color: Color = COLOR_DEFAULT,
) -> Message:
    """Greeting function.

    Create a greeting message.

    Example:
        >>> greeting_function(name="Aleksandr", color=Color("Yellow"))
        Message("Hello, Aleksandr. Your color is Yellow.")
    """
    return Message(f"Hello, {name}. Your color is {color}.")


# %%

print(greeting_function("Aleksandr", Color("Yellow")))

# %%

# Note: Error will be during checking, not during execution.
# print(greeting_function(Color("Yellow"), "Aleksandr"))
