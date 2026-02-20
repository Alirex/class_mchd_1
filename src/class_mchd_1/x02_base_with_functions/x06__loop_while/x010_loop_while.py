# %%
my_limit = 10

# %%

# while bool(limit):
while my_limit:
    print(my_limit, bool(my_limit))
    my_limit -= 1

print("end", my_limit, bool(my_limit))

# %%

my_limit_2 = 10

while my_limit_2 > 0:
    print(my_limit_2, bool(my_limit_2))
    my_limit_2 -= 1

print("end", my_limit_2, bool(my_limit_2))
