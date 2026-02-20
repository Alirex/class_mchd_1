# ruff: noqa: PLR0133, PLR2004

# %%

# sourcery skip: equality-identity
this_is_true = True
this_is_false = False

print(f"{this_is_true=}, {type(this_is_true)}")
print(f"{this_is_false=}, {type(this_is_false)}")

# %%

print(f"not True: {not True}")
print(f"not False: {not False}")

# %%

print(f"2 > 3: {2 > 3}")
print(f"2 == 2: {2 == 2}")  # "= =" - equal
print(f"2 != 3: {2 != 3}")  # type: ignore[comparison-overlap] # "! =" - not equal  # pyright: ignore[reportUnnecessaryComparison]

# %%

print(f"(2 == 2) and (2 > 3): {(2 == 2) and (2 > 3)}")
print(f"(2 == 2) or (2 > 3): {(2 == 2) or (2 > 3)}")

# %%
# Ranges

a = 10
b = 1
print(f"2 < {a} < 20: {2 < a < 20}")
print(f"2 < {b} < 20: {2 < b < 20}")

# %%
# Save to the variable

message = f"2 < {a} < 20: {2 < a < 20}"
print(message)


expression_result = 2 < a < 20
print(expression_result)

# %%
# Types ignoring

c: int = 10
d: int = "10"  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
print(f"{a=}, {type(a)}")
print(f"{c=}, {type(c)}")
print(f"{d=}, {type(d)}")

# %%
# Strings comparison

string = "NOTEbook"
second_string = "noteBOOK"
print(f"{string} == {second_string}: {string == second_string}")  # pyright: ignore[reportUnnecessaryComparison]
print(
    f"{string.lower()} == {second_string.lower()}: {string.lower() == second_string.lower()}",
)

# %%
# Compare different types

my_string = "10"
my_integer = 10
print(f"{my_string} == {my_integer}: {my_string == my_integer}")  # type: ignore[comparison-overlap]  # pyright: ignore[reportUnnecessaryComparison]

my_float = 10.0
print(f"{my_integer} == {my_float}: {my_integer == my_float}")

# %%
