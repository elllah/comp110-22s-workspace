"""Structered Wordle."""
__author__ = 730484344


def contains_char(word: str, single: str) -> bool: 
    """Find the single character string in the word string."""
    assert len(single) == 1
    i = 0
    while i < len(word): 
        if single == word[i]:
            return (True)
        else:
            i = i + 1
    return (False)  


def emojified(guess: str, secret: str) -> None:
    """Return a string that is the yellow or white emoji box"""
    assert len(guess) == len(secret)

    result: str = ""

    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    i = 0

    while i < len(secret):
        if (guess[i] == secret[i]):
            print(result + GREEN_BOX, end='')
            i = i + 1
        elif contains_char(secret, guess[i]) is not False:
            print(result + YELLOW_BOX, end='')
            i = i + 1
        else:
            print(result + WHITE_BOX, end='')
            i = i + 1


def input_guess(expected_length: int):
    """The guess length has to match the secret length"""
    guess: str = input(f"Enter a {expected_length} character word: ")
    while len(guess) != expected_length:
        guess = input("That wasn't {expected_length} chars! Try again: ")
    else:
        return(guess)


def main() -> None:
    """The entrypoint of the program and main game loop"""
    secret: str = "codes"
    n = 1
    won: bool = False

    while n < 6 and won is not True: 
        print(f" === Turn {n}/6 ===")
        new_guess = str(input_guess)
        emojified(new_guess, secret)
        if new_guess == secret:
            print(f" You won in {n} turns!")
            won = True
        else:
            n = n + 1
    if n > 6:
        quit(" X/6 - Sorry, try again tomorrow!")


if __name__ == main():
    main()