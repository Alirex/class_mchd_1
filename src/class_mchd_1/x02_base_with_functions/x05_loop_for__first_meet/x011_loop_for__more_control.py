# You can use extra control for your loop.
#   - "continue" operator: Go to next iteration now
#   - "break" operator: Stop loop now
#   - "else" block: Executed, if not used "break".

# %%
def make_output(
    string: str,
    break_at: str = "7",
    continue_at: str = "3",
) -> None:
    print(f"String: '{string}'. '{continue_at=}', '{break_at=}'")

    for character in string:
        if character == continue_at:
            print("continue")
            continue

        if character == break_at:
            print("break")
            break

        print(character)
    else:
        print("else")

    print("===")


# %%
my_string = "0123456789"
make_output(my_string)

# %%
my_another_string = "012345"
make_output(my_another_string)

# %%
my_empty_string = ""
make_output(my_empty_string)
