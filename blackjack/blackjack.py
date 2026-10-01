import random


def play_or_not():
    answer = input("Do you want to play? [Y/N] ").lower()
    return answer == "y"


def create_deck():
    return [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def check_ace(cards):
    total = sum(cards)

    while total > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
        total = sum(cards)

    return total


def starting_game(live_cards):
    player_cards = []
    computer_cards = []

    for i in range(2):
        player_card = random.choice(live_cards)
        player_cards.append(player_card)
        live_cards.remove(player_card)

    for i in range(2):
        computer_card = random.choice(live_cards)
        computer_cards.append(computer_card)
        live_cards.remove(computer_card)

    return player_cards, computer_cards


def hit_or_stand(live_cards, player_cards):

    while True:

        player_total = check_ace(player_cards)

        if player_total > 21:
            return player_total

        choice = input("Do you want to hit or stand? [hit/stand] ").lower()

        if choice == "stand":
            return player_total

        card = random.choice(live_cards)
        player_cards.append(card)
        live_cards.remove(card)

        print(f"YOUR CARDS: {player_cards}")
        print(f"YOUR TOTAL: {check_ace(player_cards)}")


def computer_turn(live_cards, computer_cards):

    computer_total = check_ace(computer_cards)

    while computer_total < 17:

        card = random.choice(live_cards)

        computer_cards.append(card)
        live_cards.remove(card)

        computer_total = check_ace(computer_cards)

    return computer_total


def determine_winner(player_total, computer_total):

    if player_total > 21:
        return "You lose!"

    if computer_total > 21:
        return "You win!"

    if player_total > computer_total:
        return "You win!"

    if player_total < computer_total:
        return "You lose!"

    return "Draw!"


def play_game():

    live_cards = create_deck()

    player_cards, computer_cards = starting_game(live_cards)

    player_total = check_ace(player_cards)
    computer_total = check_ace(computer_cards)

    print(f"YOUR CARDS: {player_cards}")
    print(f"YOUR TOTAL: {player_total}")

    print(f"COMPUTER CARDS: {computer_cards}")
    print(f"COMPUTER TOTAL: {computer_total}")

    # Blackjack
    if player_total == 21:
        print("You hit Blackjack!")
        return

    if computer_total == 21:
        print("Dealer hit Blackjack!")
        return

    # Player turn
    player_total = hit_or_stand(live_cards, player_cards)

    if player_total > 21:
        print("You lose! You busted.")
        return

    # Computer turn
    computer_total = computer_turn(live_cards, computer_cards)

    print(f"COMPUTER CARDS: {computer_cards}")
    print(f"COMPUTER TOTAL: {computer_total}")

    # Winner
    result = determine_winner(player_total, computer_total)

    print(result)


def blackjack():

    while play_or_not():

        play_game()

        print()


blackjack()


















