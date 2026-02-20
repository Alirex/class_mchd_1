# ruff: noqa: PLR2004

# %%

# With if-elif-else you can control the flow of execution.


def make_decision(number: int) -> str:
    # sourcery skip: lift-return-into-if
    if number == 7:
        message = f"{number} Equal 7"
    elif number >= 20:
        message = f"{number} bigger then 20"
    elif number != 5:
        message = f"{number} not equal 5"
    else:
        message = "Else"

    return message


# %%
print(make_decision(7))
# %%
print(make_decision(25))
# %%
print(make_decision(8))
# %%
print(make_decision(5))
