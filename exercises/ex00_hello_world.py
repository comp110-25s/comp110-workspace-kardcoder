"""My first excercise in COMP 110!"""

__author__ = "730822339"


def greet(name: str) -> str:
    """A welcoming first function definition."""
    return "Hello, " + name + "!"


if __name__ == "__main__":
    print(greet(name=input("What is your name?")))
