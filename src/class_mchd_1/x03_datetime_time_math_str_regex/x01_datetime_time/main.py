import calendar
import datetime
import time
import zoneinfo
from typing import Final

import dateutil

# import locale

type Weekday = int

MY_WEDNESDAY_WEEKDAY: Final[Weekday] = 2

ALLOWED_WEEKDAYS: Final[set[Weekday]] = {
    calendar.WEDNESDAY,
    calendar.FRIDAY,
}


def example_datetime() -> None:
    dt = datetime.datetime(2024, 6, 1, 12, 30, 45, tzinfo=datetime.UTC)
    print("Original datetime:", dt)

    # region datetime_components
    date_example = dt.date()
    print("Date part:", date_example)

    time_example = dt.time()
    print("Time part:", time_example)
    # endregion datetime_components

    # Adding time
    dt_plus = dt + datetime.timedelta(days=1, hours=2)
    print("After adding 1 day and 2 hours:", dt_plus)

    # Subtracting time
    dt_minus = dt - datetime.timedelta(minutes=15)
    print("After subtracting 15 minutes:", dt_minus)

    # Relative delta using dateutil
    dt_relative = dt + dateutil.relativedelta.relativedelta(months=1)
    print("After adding 1 month:", dt_relative)

    today = datetime.datetime.now(datetime.UTC)

    weekday = today.weekday()
    print("Weekday (0=Monday, 6=Sunday):", weekday)

    if weekday == calendar.WEDNESDAY:
        print("It's Wednesday!")

    if weekday in ALLOWED_WEEKDAYS:
        print("It's an allowed weekday!")

    now_by_kyiv = datetime.datetime.now(zoneinfo.ZoneInfo("Europe/Kyiv"))
    print("Current time in Kyiv:", now_by_kyiv)

    datetime_via_half_year = now_by_kyiv + dateutil.relativedelta.relativedelta(months=6)
    print("Current time in Kyiv after 6 months:", datetime_via_half_year)


def example_time(
    number_of_repeats: int = 3,
) -> None:
    start_time_performance = time.perf_counter()
    start_time = time.time()
    for i in range(number_of_repeats):
        print(f"Repeat {i + 1}/{number_of_repeats}")
        print(f"Current time: {datetime.datetime.now(datetime.UTC)}")
        # time.sleep(1)  # Simulate some work by sleeping for 1 second
    end_time = time.time()
    end_time_performance = time.perf_counter()
    elapsed_time = end_time - start_time
    print(f"Elapsed time: {elapsed_time:.2f} seconds")

    elapsed_time_performance = end_time_performance - start_time_performance
    print(f"Elapsed time (performance counter): {elapsed_time_performance:.6f} seconds")


FORMAT_DATETIME_WITH_WEEKDAY = "%Y-%m-%d (%A) %H:%M:%S %Z"
"""Datetime format with weekday.

e.g., "2024-06-01 (Saturday) 12:30:45 UTC".
"""

# https://docs.python.org/3.14/library/datetime.html#format-codes


def example_datetime_conversion() -> None:
    dt = datetime.datetime.now(datetime.UTC)
    print("Original datetime:", dt)

    # region datetime_to_timestamp
    timestamp = dt.timestamp()
    print("Timestamp:", timestamp)

    dt_from_timestamp = datetime.datetime.fromtimestamp(timestamp, tz=datetime.UTC)
    print("Datetime from timestamp:", dt_from_timestamp)
    # endregion datetime_to_timestamp

    # region datetime_to_iso
    iso_format = dt.isoformat()
    print("ISO format:", iso_format)

    dt_from_iso = datetime.datetime.fromisoformat(iso_format)
    print("Datetime from ISO format:", dt_from_iso)
    # endregion datetime_to_iso

    # region datetime_to_strftime
    # # Set Ukrainian locale for demonstration (you may need to have it installed on your system)
    # locale.setlocale(locale.LC_TIME, "uk_UA.UTF-8")

    formatted_str = dt.strftime(FORMAT_DATETIME_WITH_WEEKDAY)
    print("Formatted datetime string:", formatted_str)

    dt_from_str = datetime.datetime.strptime(formatted_str, FORMAT_DATETIME_WITH_WEEKDAY)  # noqa: DTZ007
    print("Datetime from formatted string:", dt_from_str)
    # endregion datetime_to_strftime


def main() -> None:
    example_datetime()
    example_time()
    example_datetime_conversion()


if __name__ == "__main__":
    main()
