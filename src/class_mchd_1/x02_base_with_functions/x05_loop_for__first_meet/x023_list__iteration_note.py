# Don't change the list, while iterate over it.
#   Because you can have problems.
from typing import Final

# %%
lemon = "Lemon"

LIMIT: Final[int] = 10
"""Limit of iteration.

Because we can have endless loop.
"""

fruits = ["Kiwi", "Apple", "Pineapple", lemon, "Pineapple"]
for fruit in fruits:
    if fruit == lemon:
        fruits.insert(1, "Mango")
    print(f"{fruit}, {fruits}")

    if len(fruits) >= LIMIT:
        break

print(f"{fruits=}")

# %%
