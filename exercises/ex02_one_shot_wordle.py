"""One Shot Wordle"""
__author__ = "730484344"

SECRET: str = "python"
guess: str = input(f"What is your {len(SECRET)}-letter guess: ")
result: str = ""


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


while (len(guess) != len(SECRET)):
    guess = input(f"That was not {len(SECRET)} letters! Try again: ")
i: int = 0
if guess != SECRET:

    while (i < len(SECRET)):
        index: str = guess[i]
        if (index == SECRET[i]):
            print(result + GREEN_BOX, end='')
            
        else:
            yellow: bool = False
            c: int = 0
            while (yellow == False and c < len(SECRET)):
                if (index == SECRET[c]):
                    yellow = True
                else:
                    c = c + 1
            if (yellow == True):
                print(result + YELLOW_BOX, end='')
            else:
                print(result + WHITE_BOX, end='')
        i = i + 1
    print(result)
    print("Not quite. Play again soon! ")

else:
    while (i < len(SECRET)):
        index: str = guess[i]
        if (index == SECRET[i]):
            print(result + GREEN_BOX, end='')

        i = i + 1
    print(result)
    print("Woo! You got it! ")