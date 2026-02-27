# %%
from dataclasses import dataclass
from typing import ClassVar, NamedTuple

from pydantic import BaseModel, ConfigDict


# Base class.
#   Very simple.
#   Verbose.
class Human:
    def __init__(
        self,
        name: str,
        age: int,
    ) -> None:
        self.name: str = name
        self.age: int = age


# Dataclass. Nice when need built-in features.
@dataclass(frozen=True, slots=True)
class Human1:
    name: str
    age: int


@dataclass
class Human1Alternative:
    name: str
    age: int


# NamedTuple. Good for some cases.
#   But fewer features than dataclass.
#   Worse refactoring (field names)
class Human2(NamedTuple):
    name: str
    age: int


# Pydantic. Best if you can use it.
#   Runtime type checking and validation.
#   JSON serialization/deserialization.
#   Can require more resources.
class Human3(BaseModel):
    name: str
    age: int


class Human3Alternative(BaseModel):
    name: str
    age: int

    model_config: ClassVar[ConfigDict] = ConfigDict(
        frozen=True,
    )


# Note: Alternative class constructors.

# Pydantic
# https://docs.pydantic.dev/latest/

# dataclasses
# https://docs.python.org/3/library/dataclasses.html

# attrs
# https://www.attrs.org/en/stable/


def main() -> None:
    human_0 = Human("Tony", 42)
    print(f"{human_0=}")

    human = Human(name="Tony", age=42)
    print(f"{human=}")

    human1 = Human1(name="Tony", age=42)
    print(f"{human1=}")

    human2 = Human2(name="Tony", age=42)
    print(f"{human2=}")

    human3 = Human3(name="Tony", age=42)
    print(f"{human3=}")


if __name__ == "__main__":
    main()
