# %%
# Dictionary. Store data as "key: value" pairs. Mutable. Keys must be unique.
from typing import Any, TypedDict

# %%
# Define like this.
my_dict = {}  # type: ignore[var-annotated]

# %%

# sourcery skip: dict-literal
another_my_dict = dict()  # type: ignore[var-annotated]  # noqa: C408  # pyright: ignore[reportUnknownVariableType]

# %%

# You can create it populated.
# Usually bad to use as an object representation.
user_info: dict[str, Any] = {  # pyright: ignore[reportExplicitAny]
    "name": "Bruce",
    "age": 35,
    "married": True,
}

# %%


class UserAsTypedDict(TypedDict):
    name: str
    age: int
    married: bool


user_info_2: UserAsTypedDict = UserAsTypedDict(
    name="Bruce",
    age=35,
    married=True,
)

print(f"{user_info=}")

# %%

# Get value by key:
name = user_info["name"]  # pyright: ignore[reportAny]
print(f"{name=}")

# # Don't show warning for dict. Show a warning for TypedDict.
# name_2 = user_info["name123"]
# name_3 = user_info_2["name123"]

print(f"{user_info=}")

# %%

# Better usage for dicts.

type T_PHONE_NUMBER = str
type T_NAME = str

better_dict_usage_as_registry: dict[T_PHONE_NUMBER, T_NAME] = {
    "+380123456789": "Bruce",
    "+380987654321": "Anna",
}

# %%

# Anyway, show some examples.

# Add keys:
user_info["hobbies"] = [
    "Programming",
    "Running",
]

print(f"{user_info=}")

# %%

# Change values by keys:
user_info["age"] += 10
print(f"{user_info=}")

# %%

# Create a new dict by merging with another dict:
another_info = {
    "age": 17,
    "nickname": "Batman",
}
new_info = user_info | another_info
print(f"{user_info=}, {another_info=}")
print(f"{new_info=}")

# %%

# Update values by other dict:
user_info.update(another_info)
print(f"{user_info=}, {another_info=}")

# %%

# Delete key with value:
del user_info["hobbies"]

print(f"{user_info=}")

# %%

# Alternative for structures like this:
titles = [
    "name",
    "age",
    "married",
]

values = [
    (
        "Bruce",
        35,
        True,
    ),
    (
        "Anna",
        25,
        False,
    ),
]
