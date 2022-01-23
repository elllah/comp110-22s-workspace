"""EX01 - CHARDLE - A cute step toward Wordle."""
__author__ = "730484344"

five_word: str = input("Enter a 5-character word ")
if (len(five_word) != 5):
    exit("Error: Word must contain five characters")

one_letter: str = input("Enter a single character ") 
if (len(one_letter) != 1):
    exit("Error: Character must be a single character")


print("Searching for " + one_letter + " in " + five_word)
count = 0 
if (one_letter == five_word[0]):
    print(one_letter + " found at index 0")
    count = count + 1
if (one_letter == five_word[1]):
    print(one_letter + " found at index 1") 
    count = count + 1
if (one_letter == five_word[2]):
    print(one_letter + " found at index 2")
    count = count + 1 
if (one_letter == five_word[3]):
    print(one_letter + " found at index 3")
    count = count + 1
if (one_letter == five_word[4]):
    print(one_letter + " found at index 4")
    count = count + 1 

if (count == 0):
    print("No instances of " + one_letter + " in " + five_word) 
if (count == 1):
    print("1 instance of " + one_letter + " in " + five_word)
if (count == 2):
    print("2 instances of " + one_letter + " in " + five_word)