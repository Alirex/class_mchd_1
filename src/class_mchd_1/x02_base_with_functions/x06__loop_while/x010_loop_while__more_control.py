#  Note: Remember about "endless loop".
#   If you do this, your app never stops. Don't do this.

# %%
def make_output(
    number: int,
    break_at: int = 7,
    continue_at: int = 3,
) -> None:
    print(f"Number: {number}. {continue_at=}, {break_at=}")

    count = 0
    while count <= number:
        if count == continue_at:
            print("continue")
            count += 1
            continue

        if count == break_at:
            print("break")
            break

        print(count)
        count += 1
    else:
        print("else")

    print("===")


# %%
make_output(20)

# %%
make_output(6)

# %%
make_output(-10)
