# %%
name = "Aleksandr"


# Build string by "f-string" (formatted string). Use "f" character before string.
message = f"Your name is {name}. Nice :)"

print(message)

# %%

# Alternative way to build string with substitution.
message_with_substitution = "Your name is {name}. Nice :)".format(name=name)  # noqa: UP032
print(message_with_substitution)


# %%
# Interesting usage of "f-string".
# Can be useful for light debugging or logging.
another_message = f"Text. {name=}. Text again."
print(another_message)

# Docs: https://docs.python.org/3/library/string.html#format-specification-mini-language
