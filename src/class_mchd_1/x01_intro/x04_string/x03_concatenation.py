# %%

# You can build a string by "concatenation".
#   But usually, it is bad practice.

my_string = "This is " + "text" + "," + "what built by concatenation."

print(f"{my_string=}")

# %%

# More complex example:
name = "Aleksandr"
text = "Some text"

# %%

# Usually, a bad way.

# sourcery skip: use-fstring-for-concatenation
another_string_bad = "Hello, " + name + ". " + text + "! Concatenated text."
print(f"{another_string_bad=}")

# %%

# Usually, a better way.

another_string_good = f"Hello, {name}. {text}! Concatenated text."
print(f"{another_string_good=}")

# %%

# Build by format.

another_string_template = "Hello, {name}. {text}! Concatenated text."
another_string_template_substitution = another_string_template.format(
    name=name,
    text=text,
)
print(f"{another_string_template_substitution=}")

# %%

# Build by join.
#   Better way, if you have a lot of parts to concatenate.

temp = ["Hello", "My", "World"]
message = " ".join(temp)
print(f"{message=}")
