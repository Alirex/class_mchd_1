# %%

# "input" ask for input of data via the console.
#   It is always string.
user_input = input("Please, enter number:\n")

print(f"{user_input=}, {type(user_input)=}")

# %%

# If you want, you can convert value.
user_input_as_int = int(user_input)
print(f"{user_input_as_int=}, {type(user_input_as_int)=}")
