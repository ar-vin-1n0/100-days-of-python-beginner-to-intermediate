from art import vs,higher_lower
from data import data

import random

def display(compare,against):
    print(higher_lower)
    print()

    print(f"A : {compare["name"]}, A {compare["description"]} from {compare['country']}")
    print()
    print(vs)
    print()
    print(f"B : {against["name"]}, A {against["description"]} from {against['country']}")



def main():
    data_c = data.copy()
    compare = random.choice(data_c)
    data_c.remove(compare)
    score = 0

    alive = True
    while alive:

        if not data_c:
            print(f"Game complete! Final score: {score}")
            break

        against = random.choice(data_c)
        data_c.remove(against)

        display(compare,against)

        answer = input(f"who has more followers {compare["name"]} or {against["name"]} [A/B] ").lower()

        if answer == "a":
            if compare["follower_count"] > against["follower_count"]:
                score += 1
                print(f"you were right ur score is {score}")
            else:
                print(f"you were wrong ur score is {score}")
                print("ur run ended")
                alive = False

        elif answer == "b":
            if compare["follower_count"] < against["follower_count"]:
                score += 1
                print(f"you were right ur score is {score}")
            else:
                print(f"you were wrong ur score is {score}")
                print("ur run ended")
                alive = False

        compare = against



main()




