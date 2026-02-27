import sys


def main() -> None:
    print("Hello, World!")
    print(f"Python version: {sys.version}")

    # Print paths
    print("Python paths:")
    for path in sys.path:
        print(f"  {path}")


# https://packaging.python.org/en/latest/guides/writing-pyproject-toml/#creating-executable-scripts

if __name__ == "__main__":
    main()
