# ruff: noqa: PERF401
# sourcery skip: for-append-to-extend, list-comprehension

# %%
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# %%
my_list_comprehension = [item**2 for item in my_list]

# %%
my_list_comprehension_2: list[int] = []
for item in my_list:
    my_list_comprehension_2.append(item**2)


# %%
# List comprehension.
my_list_2 = [item**2 for item in my_list if item % 2 == 0]

# %%

# sourcery skip: list-comprehension
my_list_3: list[int] = []
for item in my_list:
    if item % 2 == 0:
        new_item = item**2
        my_list_3.append(new_item)

# %%
