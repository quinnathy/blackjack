"""
Objective: Beat the dealer without busting.
Your goal is to have a hand value closer to 21 than the dealer's.

Card Values: (Don't worry about this, it's calculated for you.)
Number cards are worth their face value.
Face cards (Kings, Queens, Jacks) are each worth 10.
Aces can be worth 1 or 11, depending on what suits your hand best.

Dealing:
Both you and the dealer get two cards.
The dealer reveals one card and keeps the other face-down.

Player's Turn:
You decide whether to "hit" (take another card) or "stand"
(keep your current hand).
You can continue hitting until you either decide to stand
or your hand goes over 21 (bust).

Dealer's Turn:
The dealer reveals their face-down card.
They must hit until their hand reaches 17 or higher.

Winning:
If your hand is closer to 21 than the dealer's without busting, you win!
If the dealer busts, you win.
If you both have the same total, it's a push (nobody wins).

Have fun!
"""

import random
cards  = ['10 of Hearts', '9 of Hearts', '8 of Hearts', '7 of Hearts', '6 of Hearts', '5 of Hearts', '4 of Hearts', '3 of Hearts', '2 of Hearts', 'Ace of Hearts', 'King of Hearts', 'Queen of Hearts', 'Jack of Hearts', '10 of Diamonds', '9 of Diamonds', '8 of Diamonds', '7 of Diamonds', '6 of Diamonds', '5 of Diamonds', '4 of Diamonds', '3 of Diamonds', '2 of Diamonds', 'Ace of Diamonds', 'King of Diamonds', 'Queen of Diamonds', 'Jack of Diamonds', '10 of Clubs', '9 of Clubs', '8 of Clubs', '7 of Clubs', '6 of Clubs', '5 of Clubs', '4 of Clubs', '3 of Clubs', '2 of Clubs', 'Ace of Clubs', 'King of Clubs', 'Queen of Clubs', 'Jack of Clubs', '10 of Spades', '9 of Spades', '8 of Spades', '7 of Spades', '6 of Spades', '5 of Spades', '4 of Spades', '3 of Spades', '2 of Spades', 'Ace of Spades', 'King of Spades', 'Queen of Spades', 'Jack of Spades']
values = [10, 9, 8, 7, 6, 5, 4, 3, 2, [1,11], 10, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, [1,11], 10, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, [1,11], 10, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, [1,11], 10, 10, 10]

# returns values and ace status
def handvalue(hand):
    value = 0
    value_ace = 0
    ace = False
    for card in hand:
        if "ace" in card.lower():
            ace = True
            value += 1
            value_ace += 11
            continue
        value += values[cards.index(card)]
        value_ace += values[cards.index(card)]
    return value, value_ace, ace

# keep track of player/dealer wins
player_wins = 0
dealer_wins = 0

# for the betting system
bank_original = int(input("How much money are you starting off with? "))
bank = bank_original

while True:
    
    # check if you're broke!
    if bank <= 0:
        print("It looks like you don't have any money left...")
        print("Better luck next time!")
        break
    
    # reset it all
    hand = []
    dealer = []

    # place ya bets, place ya bets
    while True:
        bet = int(input("How much money are you betting? "))
        if bet > bank:
            print("You don't have enough money to bet that much! Try again.")
            continue
        else:
            break
    
    # to store initial two hands
    hand = random.choices(cards, k=2)
    dealer = random.choices(cards, k=2)
    used_cards = hand + dealer

    # and we're off!
    print("\nThe dealer flips one of their cards over:", dealer[0])

    # player's turn first...
    while True:
        used_cards = hand + dealer
        remaining_cards = [x for x in cards if x not in used_cards]
        value, value_ace, ace = handvalue(hand)
        print("Your hand is:", hand)
        if ace == True and value_ace < 22:
            print("Your hand is worth", value, "or", value_ace)
        else:
            print("Your hand is worth", value)
        if value == 21 or value_ace == 21 and value_ace < 22:
            print("Blackjack! Player wins!")
            bank += bet
            print("You now have $", bank, " in the bank!", sep="")
            player_wins += 1
            comp_turn = False
            break
        elif value > 21:
            print("Bust! Dealer wins!")
            bank -= bet
            print("You now have $", bank, " in the bank!", sep="")
            dealer_wins += 1
            comp_turn = False
            break
        turn = input("(h)it or (s)tand? ")
        if turn.lower() == "h":
            hand.append(random.choice(remaining_cards))
            continue
        elif turn.lower() == "s":
            if ace == True and value_ace < 22:
                print("You chose to stand! Your hand is worth", value_ace)
                value = value_ace
            else:
                print("You chose to stand! Your hand is worth", value)
            comp_turn = True
            break

    # goes into dealer's turn
    if comp_turn == True:
        print()
        print("The dealer flips their other card over:", dealer[1])

        while True:
            used_cards = hand + dealer
            remaining_cards = [x for x in cards if x not in used_cards]
            cvalue, cvalue_ace, ace = handvalue(dealer)
            print("Dealer's hand is:", dealer)
            if ace == True and cvalue_ace < 22:
                print("Dealer's hand is worth", cvalue, "or", cvalue_ace)
            else:
                print("Dealer's hand is worth", cvalue)
            if cvalue == 21 or cvalue_ace == 21 and cvalue_ace < 22:
                print("Blackjack! Dealer wins!")
                bank -= bet
                print("You now have $", bank, " in the bank!", sep="")
                dealer_wins += 1
                break
            elif cvalue > 21:
                print("Bust! Player wins!")
                bank += bet
                print("You now have $", bank, " in the bank!", sep="")
                player_wins += 1
                break
            elif cvalue > value:
                print("Dealer got more points than player! Dealer wins!")
                bank -= bet
                print("You now have $", bank, " in the bank!", sep="")
                dealer_wins += 1
                break
            elif cvalue == value:
                print("Push! It's a draw!")
                break
            dealer.append(random.choice(remaining_cards))
            print("Dealer drew", dealer[-1])

    print()
    
    cont = input("Would you like to go another round? (y/n): ")
    if cont.lower() == "y":
        print()
        continue
    else:
        print("\nYou've chosen to end the game!")

        # sums up your stats
        if bank > bank_original:
            print("You've won $", bank-bank_original," :)", sep="")
            print("That brings your total to $", bank,"!", sep="")
        elif bank < bank_original:
            print("You've lost $", bank_original-bank," :(", sep="")
            print("That brings your total to $", bank,"!", sep="")
        else:
            print("Your bank balance stayed at $", bank, "!", sep="")
        print("Player:", player_wins, "|| Dealer:", dealer_wins)
        if player_wins > dealer_wins:
            print("Player won more than dealer! Congratulations!")
        elif player_wins < dealer_wins:
            print("Dealer won more than player! Better luck next time!")
        else:
            print("It was a tie!")
        break
