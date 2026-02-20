# %%
import logging

# Note: `loguru` can be used instead of `logging` for better logging experience.

# %%

my_dict = {"name": "Luke"}
my_list = ["a", "b"]

logger = logging.getLogger(__name__)

# %%
try:
    my_dict["nickname"]
except KeyError as exc:
    print(f"{type(exc)}, {exc}")

    logger.warning("this is my_log")
    # Catches exception and shows traceback
    logger.exception("Error")

# %%
try:
    my_list[10]
except IndexError as exc:
    print(f"{type(exc)}, {exc}")

# %%
# [base_exception]-[BEGIN]
try:
    my_list[10]
except LookupError as exc:
    print(f"{type(exc)}, {exc}")

try:
    my_dict["nickname"]
except LookupError as exc:
    print(f"{type(exc)}, {exc}")
# [base_exception]-[END]

# %%

# Better to not blindly catch all exceptions, but if you need to:
try:
    my_list[10]
except Exception as exc:  # noqa: BLE001
    print(f"{type(exc)}, {exc}")
