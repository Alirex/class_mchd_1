# %%
from typing import Final

# Pseudo-constant. Checked by linter.
NAME: Final[str] = "Bob"

# # Must show warning/error during checking.
# NAME = "Alice"


def greeting_function() -> str:
    # NAME = "Alice"  # noqa: N806, RUF100

    return f"Hello, {NAME}!"


print(greeting_function())

# %%
