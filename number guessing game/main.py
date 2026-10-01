import random

number = random.randint(1,100)

difficulty = input("choose difficulty  [easy,hard] : ")
chance = 0
if difficulty == "easy":
    chance = 10
elif difficulty == "hard":
    chance = 5

while chance > 0:
    print(f"u have {chance} chances to guess")

    guess = int(input("your guess : "))

    if guess == number:
        print("you guessed the number")
        break
    elif guess < number:
        print("your guess is too low")
    else:
        print("your guess is too high")

    chance -= 1

if chance == 0:
    print("you did not guessed the number ur out of chances")


