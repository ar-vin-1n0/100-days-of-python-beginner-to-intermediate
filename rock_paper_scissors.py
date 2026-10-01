
import random

def r_p_s():
    list_choice = ["rock","paper","scissors"]
    computer_choice = random.choice(list_choice)
    print("choose ur play")
    print("enter |rock|paper|scissors|")
    player_choice =  input("enter your choice  ")

    if player_choice == computer_choice:
        print(f"{computer_choice}  its a draw")
    elif player_choice == "rock"  and computer_choice == "paper" or player_choice == "paper" and computer_choice == "scissors" or player_choice == "scissors" and computer_choice == "rock":
        print(f"{computer_choice}   you loose")
    else:
        print(f"{computer_choice}  you win")


print(r_p_s())