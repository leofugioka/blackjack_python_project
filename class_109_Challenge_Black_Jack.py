import os
import art
import random

cards_in_deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def print_logo():
    os.system('cls')
    print(art.logo)

def check_keep_playing(user_entry):
    if user_entry == "y":
        keep_playing = True
    else:
        keep_playing = False
    
    return keep_playing

def start_game(): 
    print_logo()
    
    play_game = input("Do you want to play Black Jack? 'y' or 'n'\n")
    
    return check_keep_playing(play_game)

def new_game():
    new_game1 = input("Do you want to play again? 'y' or 'n'\n")
    
    return check_keep_playing(new_game1)

def draw_card(cards_in_hand):
    
    cards_in_hand.append(cards_in_deck[random.randint(0, 12)])

def deal_cards(cards_in_hand):
    draw_card(cards_in_hand)
    draw_card(cards_in_hand)

def calculate_points(cards_in_hand):
    if sum(cards_in_hand) > 21 and 11 in cards_in_hand:
        return sum(cards_in_hand) - 10
    else:
        return sum(cards_in_hand)

def print_hand_and_score(dealer_hand, dealer_points, player_hand, player_points, finish_game):
    print_logo()
    if not finish_game:
        print(f"Dealer's hand: [*, {dealer_hand[1]}] || Total points: {dealer_hand[1]}")
    else:
        print(f"Dealer's hand: {dealer_hand} || Total points: {dealer_points}")
    print(f"Player's hand: {player_hand} || Total points: {player_points}")

def calculate_result(dealer_points, player_points):
    if (dealer_points > 21 and player_points > 21) or (dealer_points == player_points):
        print("Draw")
    elif (dealer_points > 21 and player_points <= 21) or (dealer_points <= 21 and (dealer_points < player_points and player_points <= 21)):
        print("You win!")
    else:
        print("Dealer wins!")

def blackjack_game():
    dealer_hand = []
    player_hand = []
    finish_game = False
    
    deal_cards(dealer_hand)
    deal_cards(player_hand)
    
    player_points = calculate_points(player_hand)
    dealer_points = calculate_points(dealer_hand)
    
    print_hand_and_score(dealer_hand = dealer_hand, dealer_points = dealer_points, player_hand = player_hand, player_points = player_points, finish_game = finish_game)
    
    while player_points <= 21:
        wants_to_draw_a_card = input("Do you want to draw a card? 'y' or 'n'\n")

        if wants_to_draw_a_card == 'y':
            draw_card(player_hand)
            player_points = calculate_points(player_hand)
            print_hand_and_score(dealer_hand = dealer_hand, dealer_points = dealer_points, player_hand = player_hand, player_points = player_points, finish_game = finish_game)
        else:
            break
    
    finish_game = True
    
    if dealer_points < 17:
        draw_card(dealer_hand)
        dealer_points = calculate_points(dealer_hand)

    print_hand_and_score(dealer_hand = dealer_hand, dealer_points = dealer_points, player_hand = player_hand, player_points = player_points, finish_game = finish_game)
    calculate_result(dealer_points = dealer_points, player_points = player_points)


keep_playing_blackjack = start_game()

while keep_playing_blackjack:
    blackjack_game()
    keep_playing_blackjack = new_game()

print_logo()
print("Thank you for playing!")
