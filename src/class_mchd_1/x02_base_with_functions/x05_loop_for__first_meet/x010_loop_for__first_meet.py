# %%
# With "for" loop you can "iterate" over any "iterable". For example, over string.

my_string = "Hello world"


# %%
# Pattern "Iterator" in Python.
# https://refactoring.guru/design-patterns/iterator
# Base way.
for character in my_string:
    print(character)

# %%
# Not Pythonic way.
# for(i=0; i < my_string.length; i++)
for index in range(len(my_string)):
    character = my_string[index]
    print(character)

# %%
# Pythonic way, if you need an index.
for index, character in enumerate(my_string):
    print(index, character)

# %%
# Pythonic way, if you need an index, and you want to start from some number.
for index, character in enumerate(my_string, start=1):
    print(index, character)

# %%
