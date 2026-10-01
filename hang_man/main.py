from hangman_art import hangman_art


import random

from words import words,place_holder


chosen_word = random.choice(words)

guessed = []
lives = 6

print(place_holder(chosen_word))
while lives >0:
     guessed_letter = input("guess the letter in word : ").lower()
     if len(guessed_letter) != 1:
         print("please enter one letter at a time")
         continue

     display = ""

     if guessed_letter not in chosen_word:
         lives -= 1
         if lives == 0:
             print("YOU LOST")
             print("Ur lives are finished u r getting hanged")
             print(hangman_art[lives])
             break


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
     print(hangman_art[lives])

     print(f"{lives}/6")
