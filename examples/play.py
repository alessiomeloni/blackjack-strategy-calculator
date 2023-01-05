# This code imports the `BlackjackStrategy` class from the blackjack_strategy 
# module.
# The `sys` module is also imported in order to modify the system path.
# The system path is a list of directories that Python searches when looking 
# for modules to import.
# By modifying the system path, we can import modules from a different 
# directory than the current one.
# In this case, the system path is modified to include the parent directory of 
# the current directory.
# This allows us to import the `BlackjackStrategy` class, which is located in
# the parent directory.

import sys
sys.path.insert(0, '../')

from blackjack_strategy import BlackjackStrategy

# Once the `BlackjackStrategy` class is imported, we create a new object of 
# that class and assign it to the `strategy` variable.
# This object can be used to access the methods and attributes of the
# `BlackjackStrategy` class.

strategy = BlackjackStrategy()


# This code is a loop that allows a user to input a player's hand, a dealer's hand, and a current bet,
# and then calculates the optimal move for the player based on the provided hands and bet.
# The loop also handles the case where the optimal move is to split the player's hand into two separate hands.

while True:
    # Get the player's hand, dealer hand and current bet
    player_hand_str = str(input(f"Hi-Lo[{strategy.HI_LO_COUNT}] [New Hand] Enter your hand (comma-separated): "))
    dealer_hand_str = str(input(f"Hi-Lo [{strategy.HI_LO_COUNT}] [New Hand] Enter the dealer's hand (comma-separated): "))
    current_bet = float(input(f"Hi-Lo [{strategy.HI_LO_COUNT}] [New Hand] Enter the current bet: "))

    # Convert the input strings to lists of strings
    player_hand = [str(card) for card in player_hand_str.split(',')]
    dealer_hand = [str(card) for card in dealer_hand_str.split(',')]
    
    # Inner loop to handle the case where the optimal move is to split the player's hand into two separate hands
    while True:
        # Get the optimal move and next bet size
        optimal_move, next_hand_bet = strategy.get_optimal_move(current_bet, dealer_hand, player_hand)

        # If the optimal move is to hit, get a new card from the user and add it to the player's hand
        if optimal_move == "hit":
            new_card = str(input(f"{player_hand} -> [{optimal_move}] Enter the new card: "))
            player_hand.append(new_card)
        
        # If the optimal move is to split the hand, get two new hands from the user and calculate the optimal moves for each hand
        elif optimal_move == "split":
            first_hand_str = str(input(f"[{optimal_move}] Enter the first hand: "))
            second_hand_str = str(input(f"[{optimal_move}] Enter the second hand: "))
            first_hand = [str(card) for card in first_hand_str.split(',')]
            second_hand = [str(card) for card in second_hand_str.split(',')]

            # Inner loop to calculate the optimal moves for the first hand
            while True:
                first_hand_optimal_move, next_hand_bet = strategy.get_optimal_move(current_bet, dealer_hand, first_hand, no_split=True)
                if first_hand_optimal_move == "hit":
                    new_card = str(input(f"First hand {first_hand} -> [{first_hand_optimal_move}] Enter the new card: "))
                    first_hand.append(new_card)
                # If the optimal move for the first hand is to stand or double, print the move and break out of the inner loop
                elif (first_hand_optimal_move == "stand"
                      or first_hand_optimal_move == "double"):
                    print(f"First hand {first_hand} -> [{first_hand_optimal_move}]")
                    break
        
            # Inner loop to calculate the optimal moves for the second hand
            while True:
                second_hand_optimal_move, next_hand_bet = strategy.get_optimal_move(current_bet, dealer_hand, second_hand, no_split=True)
                if second_hand_optimal_move == "hit":
                    new_card = str(input(f"Second hand {second_hand} -> [{second_hand_optimal_move}] Enter the new card: "))
                    second_hand.append(new_card)
                # If the optimal move for the second hand is to stand or double, print the move and break out of the inner loop
                elif (second_hand_optimal_move == "stand"
                    or second_hand_optimal_move == "double"):
                    print(f"Second hand {second_hand} -> [{second_hand_optimal_move}]")
                    break

            # Print the optimal bet for the next hand
            print(f"Next hand optimal bet -> [{next_hand_bet}]")
            # Break out of the outer
            break
        elif optimal_move == "stand" or optimal_move == "double":
            print(f"{player_hand} -> [{optimal_move}]")
            # Print the optimal bet for the next hand
            print(f"Next hand optimal bet -> [{next_hand_bet}]")
            # Break out of the outer loop
            break

    # Prompt the user to play another hand
    play_again = input("Play another hand (y/n)? ")
    if play_again.lower() != "y":
        break




