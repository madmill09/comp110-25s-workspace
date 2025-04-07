"""Comp 110 exercise 2 wordle"""

__author__: str = "730573256"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def contains_char(secret_word: str, character_input: str) -> bool:
    """find the secret word to the wordle puzzle"""
    assert len(character_input) == 1, f"len('{secret_word}') is not 1"
    count = 0
    while count < len(secret_word):
        if secret_word[count] == character_input:
            return True
        else:
            count += 1
    else:
        return False


def emojified(guessed_word: str, secret_word: str) -> str:
    """find the secret word to the wordle puzzle with colors"""
    assert len(guessed_word) == len(secret_word), "Guess must be same length as secret"
    answer: str = ""
    count = 0
    while count < len(guessed_word):
        if guessed_word[count] == secret_word[count]:
            answer += GREEN_BOX
            count += 1

        elif contains_char(secret_word, guessed_word[count]):
            answer += YELLOW_BOX
            count += 1

        else:
            answer += WHITE_BOX
            count += 1
    return answer


def input_guess(expected_length: int) -> str:
    """Prompt the user to input a guess given correct length"""
    guess: str
    while True:
        guess = input(f"Enter a {expected_length} character word:")
        if len(guess) == expected_length:
            return guess
        else:
            print(f"That wasn't {expected_length} chars! Try again:")


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    TOTAL_TURNS: int = 6
    count = 1
    while count <= TOTAL_TURNS:
        print(f"=== Turn {count}/{TOTAL_TURNS} ===")
        guess = input_guess(len(secret))
        print(emojified(guess, secret))
        if guess == secret:
            return print(f"You won in {count}/{TOTAL_TURNS}) turns!")
        else:
            count += 1
            print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
