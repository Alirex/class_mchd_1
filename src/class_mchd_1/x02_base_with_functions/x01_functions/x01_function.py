# %%
# Function allows you to:
#   - group some actions together.
#   - decompose your code into smaller parts.
#   - reuse your code.


# At first, you define a function. It didn't execute now.
def print_hello() -> None:
    print("Hello from function")
    print("Hello from function 123")


# %%

# Then, you need to "call" it.
print_hello()
print_hello()
print_hello()


# So, "print" is just a "built-in function"

# %%


# Also, a function can have "value to return".
def get_hello_message_by_return() -> str:
    return "Hello from function with return"


# %%

# You can assign this value to a variable or send it directly to another function.
output = get_hello_message_by_return()
print(output)

print(get_hello_message_by_return())

# %%

# Better if one function created for one purpose.
#   For example, one for calculation, another for output.
#   Thanks to this, you can change how you output your data. To the console, to a file, or something else.

# "Function" naming convention:
#   - as variable
