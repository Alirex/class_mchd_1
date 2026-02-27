from dataclasses import dataclass
from typing import Protocol


@dataclass
class Human:
    name: str
    age: int

    def say(self) -> str:
        return f"Hello, my name is {self.name}. I'm {self.age} years old."


@dataclass
class Dog:
    name: str

    def say(self) -> str:
        return f"{self.name} says: Woof!"


@dataclass
class Table:
    name: str


class SayProtocol(Protocol):
    def say(self) -> str: ...


def make_action(sayable: SayProtocol) -> str:
    return sayable.say()


def main() -> None:
    human = Human(name="Alice", age=30)
    dog = Dog(name="Buddy")
    print(make_action(human))  # Hello, my name is Alice. I'm 30 years old.
    print(make_action(dog))  # Buddy says: Woof!

    # table = Table(name="MyTable")
    # print(make_action(table))  # Error: Table does not have method `say`


if __name__ == "__main__":
    main()
