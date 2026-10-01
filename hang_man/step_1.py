import random

hangman_art = [
    """
     +---+
         |
         |
         |
        ===
    """,

    """
     +---+
     O   |
         |
         |
        ===
    """,

    """
     +---+
     O   |
     |   |
         |
        ===
    """,

    """
     +---+
     O   |
    /|   |
         |
        ===
    """,

    """
     +---+
     O   |
    /|\\  |
         |
        ===
    """,

    """
     +---+
     O   |
    /|\\  |
    /    |
        ===
    """,

    """
     +---+
     O   |
    /|\\  |
    / \\  |
        ===
    """
]


words = ["nigga","sybau","tung tung sahur"]


chosen_word = random.choice(words)



placeholder = ""

for i in range(0,len(chosen_word)):
    placeholder += "_"
guessed = []
lives = 6

print(placeholder)
while lives >0:
     guessed_letter = input("guess the letter in word : ").lower()
     if len(guessed_letter) != 1:
         print("please enter one letter at a time")
         continue

     display = ""

     if guessed_letter not in chosen_word:
         lives -= 1
     for i in chosen_word:
         if i == guessed_letter:
             display += guessed_letter
             guessed.append(guessed_letter)
         elif i in guessed:
             display += i
         else:
             display += "_"

     if display in chosen_word:
         print(display)
         print("YOU WON MY N WORD")
         break

     print(display)

     print(f"{lives}/6")
if lives == 0:
    print("YOU LOST")
    print("Ur lives are finished u r getting hanged")


