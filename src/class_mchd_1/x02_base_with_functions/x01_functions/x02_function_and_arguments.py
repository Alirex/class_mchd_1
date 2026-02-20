# %%

# Function can accept some arguments. And arguments can have default values.


def greeting_function(
    name: str,
    color: str = "Blue",
) -> str:
    """Greeting function.

    Create a greeting message.

    Example:
        >>> greeting_function(name="Aleksandr", color="Yellow")
        "Hello, Aleksandr. Your color is Yellow."
    """
    return f"Hello, {name}. Your color is {color}."


# %%

# You can send arguments by "position".
print(greeting_function("Aleksandr", "Yellow"))

# %%

# If the sequence is wrong, there will be a bad result.
print(
    greeting_function(
        "Red",
        "Aleksandr",
    ),
)

# %%

# Or you can send arguments by "keys".
print(greeting_function(name="Aleksandr", color="Green"))
print(greeting_function(color="Orange", name="Aleksandr"))

# %%

# Also, you can use "default values".
print(greeting_function(name="Aleksandr"))

# %%

# If you don't send an argument without a default value, there will be an error.
# print(greeting_function(color="Yellow")) --- IGNORE ---


# %%
