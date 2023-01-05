from coach import BlackjackStrategy

strategy = BlackjackStrategy()

while True:
    # Get the player's hand, dealer hand and current bet
    player_hand_str = str(input(f"Hi-Lo[{strategy.HI_LO_COUNT}] [New Hand] Enter your hand (comma-separated): "))
    dealer_hand_str = str(input(f"Hi-Lo [{strategy.HI_LO_COUNT}] [New Hand] Enter the dealer's hand (comma-separated): "))
    current_bet = float(input(f"Hi-Lo [{strategy.HI_LO_COUNT}] [New Hand] Enter the current bet: "))

    # Convert the input strings to lists of strings
    player_hand = [str(card) for card in player_hand_str.split(',')]
    dealer_hand = [str(card) for card in dealer_hand_str.split(',')]
    
    while True:
        # Get the optimal move and next bet size
        optimal_move, next_hand_bet = strategy.get_optimal_move(current_bet, dealer_hand, player_hand)

        if optimal_move == "hit":
            new_card = str(input(f"{player_hand} -> [{optimal_move}] Enter the new card: "))
            player_hand.append(new_card)
        if optimal_move == "split":
            first_hand_str = str(input(f"[{optimal_move}] Enter the first hand: "))
            second_hand_str = str(input(f"[{optimal_move}] Enter the second hand: "))
            first_hand = [str(card) for card in first_hand_str.split(',')]
            second_hand = [str(card) for card in second_hand_str.split(',')]

            while True:
                first_hand_optimal_move, next_hand_bet = strategy.get_optimal_move(current_bet, dealer_hand, first_hand, no_split=True)
                if first_hand_optimal_move == "hit":
                    new_card = str(input(f"First hand {first_hand} -> [{first_hand_optimal_move}] Enter the new card: "))
                    first_hand.append(new_card)
                if (first_hand_optimal_move == "stand"
                    or first_hand_optimal_move == "double"):
                    print(f"First hand {first_hand} -> [{first_hand_optimal_move}]")
                    break
            
            while True:
                second_hand_optimal_move, next_hand_bet = strategy.get_optimal_move(current_bet, dealer_hand, second_hand, no_split=True)
                if second_hand_optimal_move == "hit":
                    new_card = str(input(f"Second hand {second_hand} -> [{second_hand_optimal_move}] Enter the new card: "))
                    second_hand.append(new_card)
                if (second_hand_optimal_move == "stand"
                    or second_hand_optimal_move == "double"):
                    print(f"Second hand {second_hand} -> [{second_hand_optimal_move}]")
                    break

            print(f"Next hand optimal bet -> [{next_hand_bet}]")
            break             
        if optimal_move == "stand" or optimal_move == "double":
            print(f"{player_hand} -> [{optimal_move}]")
            print(f"Next hand optimal bet -> [{next_hand_bet}]")
            break