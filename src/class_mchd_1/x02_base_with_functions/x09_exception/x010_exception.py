# %%


def make_action(number: int) -> None:
    try:
        print("Before action")
        # noinspection PyStatementEffect
        2 / number  # pyright: ignore[reportUnusedExpression]
        print("After action")
    except ZeroDivisionError:
        print("Inside of handling")
    # except ZeroDivisionError as exc:
    #     print(f"{type(exc)=}, {exc=}")
    else:
        print("else")
    finally:
        print("finally")

    print("===")


# %%
make_action(10)

# %%
make_action(0)

# %%

# Show warning by IDE.
make_action(
    "Hello",  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]
    # "Hello",
)
