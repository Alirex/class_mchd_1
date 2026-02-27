# Object, Class, Instance.
#
# Object is as a box.
#   It can contain:
#   - "variables" (called "attributes"/"fields")
#   - "functions" (called "methods") for work with these variables.
#
# Class is as "custom type". As `int`, `str`, etc.
# In general, class is as blueprint for creating objects.
#
# Instance for "class" is an "object", created by this "class".

# "CamelCase"/"PascalCase" for the `class` name.
# "snake_case" for `method` name.

# %%


from typing import override


class HumanSimple:
    # This is a "class" with "attributes" and "methods"

    def __init__(self, name: str, age: int = 18) -> None:
        # This method used to initialize values of "instance"
        self.name: str = name
        self.age: int = age


def example_human_simple() -> None:
    # This is an "instance" of "class" `HumanSimple`
    human = HumanSimple(name="Alice", age=30)

    print(f"{human.name} is {human.age} years old")  # Alice is 30 years old

    human.age = 31  # We can change attributes of "instance"
    print(f"{human.name} is {human.age} years old")  # Alice is 31 years old

    print(human)  # <__main__.HumanSimple object at 0x7f8c8c8c8c8c>
    print(repr(human))  # <__main__.HumanSimple object at 0x7f8c8c8c8c8c>


class HumanExample:
    # https://realpython.com/python-classes/
    __slots__: tuple[str, ...] = ("_internal", "age", "name")

    # This method used to initialize values of "instance"
    def __init__(
        self,
        name: str,
        age: int = 18,
    ) -> None:
        self.name: str = name
        self.age: int = age
        self._internal: str = "internal"

    def change_age(self, new_age: int) -> None:
        # This method uses attributes from "instance"

        self.age = new_age

    def say(self) -> str:
        return f"Hello, my name is {self.name}. I'm {self.age} years old."

    @override
    def __repr__(self) -> str:
        return f'HumanExample(name="{self.name}", age={self.age})'

    @override
    def __str__(self) -> str:
        return f"{self.name}, {self.age} years old"


def example_human_example() -> None:
    human = HumanExample(name="Bob", age=25)

    print(human)  # Bob, 25 years old
    print(repr(human))  # HumanExample(name="Bob", age=25)

    human.change_age(26)
    print(human.say())  # Hello, my name is Bob. I'm 26 years


def main() -> None:
    example_human_simple()
    example_human_example()


if __name__ == "__main__":
    main()
