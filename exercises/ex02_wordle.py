"""Wordle guessing game COMP110."""

__author__ = "730822339"


def contains_char(word: str, char: str) -> bool:

    assert len(char) == 1, f"len('{char}') is not 1"

    idx = 0
    while idx < len(word):
        if word[idx] == char:
            return True
        idx += 1

    return False


def emojified(guess: str, secret: str) -> str:
    """"Returns emoji representation of the guesss compared ti the secret word.""" ""
    assert len(guess) == len(secret), "Guess must be same length as secret"

    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"

    emoji_result: str = ""
    idx: int = 0

    while idx < len(guess):
        if guess[idx] == secret[idx]:
            emoji_result += GREEN_BOX
        elif contains_char(secret, guess[idx]):
            emoji_result += YELLOW_BOX
        else:
            emoji_result += WHITE_BOX
        idx += 1

    return emoji_result


def input_guess(expected_length: int) -> str:
    """Prompts user for a guess of the expected length ensures correct input."""

    guess: str = input(f"Enter a {expected_length}-character word: ")

    while len(guess) != expected_length:
        guess = input(f"That wasnt {expected_length} chars! Try again: ")

    return guess


def main(secret: str) -> None:
    """The main game loop for Wordle."""

    max_turns: int = 6
    turn: int = 1
    won: bool = False

    while turn <= max_turns and not won:
        print(f"== Turn {turn}/{max_turns} ===")

        guess: str = input_guess(len(secret))

        print(emojified(guess, secret))

        if guess == secret:
            won = True
            print(f"You won in {turn}/{max_turns} turns!")

        turn += 1

    if not won:
        print(f"X/{max_turns} - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
