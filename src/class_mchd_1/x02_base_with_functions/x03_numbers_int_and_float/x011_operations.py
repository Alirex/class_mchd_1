# %%

a = 13
b = 4

print(f"Numbers: {a=} ({type(a)}), {b=} ({type(b)})")

# %%

addition = a + b
print(f"{addition=}; {type(addition)}")

# %%

subtraction = a - b
print(f"{subtraction=}; {type(subtraction)}")

# %%

division = a / b
print(f"{division=}; {type(division)}")
print(f"{int(division)=}")

# %%

division_to_int = int(division)
print(f"{division_to_int=}; {type(division_to_int)}")

# %%

multiplication = a * b
print(f"{multiplication=}; {type(multiplication)}")

# %%

exponent = a**b  # a ** b
print(f"{exponent=}; {type(exponent)}")

# %%

modulus = a % b  # Remainder of the division
# 13 = 3 * 4 + 1
print(f"{modulus=}; {type(modulus)}")

# %%

floor_division = a // b  # The integer part of the division
# 13 // 4 = 3
print(f"{floor_division=}; {type(floor_division)}")

# %%

# Note: math module has more functions for numbers. You can import it and use it.
# import math
