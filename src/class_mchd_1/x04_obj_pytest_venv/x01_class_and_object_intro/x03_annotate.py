from dataclasses import dataclass


@dataclass
class Human:
    name: str
    age: int

    def say(self) -> str:
        return f"Hello, my name is {self.name}. I'm {self.age} years old."


def make_action(human: Human) -> str:
    return human.say()


def main() -> None:
    human = Human(name="Alice", age=30)
    print(make_action(human))  # Hello, my name is Alice. I'm 30 years old.


if __name__ == "__main__":
    main()
