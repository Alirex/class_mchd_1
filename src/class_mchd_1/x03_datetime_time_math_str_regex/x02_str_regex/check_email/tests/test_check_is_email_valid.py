import pytest

from class_mchd_1.x03_datetime_time_math_str_regex.x02_str_regex.check_email.check_is_email_valid import (
    check_is_email_valid,
)

# pytest -v -k"test_check_is_email_valid"


@pytest.mark.parametrize(
    ("email", "expected"),
    [
        ("user@mail.com", True),
        pytest.param("user@mail.com", True, id="valid email"),
        pytest.param("invalid-email", False, id="invalid email"),
    ],
)
def test_valid_email(
    email: str,
    expected: bool,  # noqa: FBT001
) -> None:
    result = check_is_email_valid(email)
    assert result == expected, f"Expected {expected} for email '{email}', got {result}"
