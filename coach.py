HI_LO_COUNT = 0

def get_optimal_move(current_bet, dealer_hand, player_hand, no_split=False):
    """
    Returns the optimal mathematical perfect move and bet for the current hand, based on the Hi-Lo system, Betting Deviations, and Playing Deviations strategies.

    Parameters:
        current_bet (int): The current bet of the player.
        dealer_hand (list): A list of strings representing the cards in the 
            dealer's hand. Each string is a single character representing the rank of the card, with T representing 10, J representing Jack, Q representing Queen, K representing King, and A representing Ace.
        player_hand (list): A list of strings representing the cards in the 
            player's hand. Each string is a single character representing the rank of the card, with T representing 10, J representing Jack, Q representing Queen, K representing King, and A representing Ace.

    Returns:
        tuple: A tuple containing the optimal move as a string and the optimal
        bet for the next hand as an integer. The possible values for the move are 'hit', 'stand', 'double', and 'split'.
    """
    global HI_LO_COUNT
    
    dealer_hand = [string.strip().upper() for string in dealer_hand]
    player_hand = [string.strip().upper() for string in player_hand]


    # Hi-Lo system
    for card in dealer_hand:
        if card in ["T", "J", "Q", "K", "A"]:
            HI_LO_COUNT -= 1
        elif card in ["2", "3", "4", "5", "6"]:
            HI_LO_COUNT += 1
    for card in player_hand:
        if card in ["T", "J", "Q", "K", "A"]:
            HI_LO_COUNT -= 1
        elif card in ["2", "3", "4", "5", "6"]:
            HI_LO_COUNT += 1

    # Betting Deviations
    next_hand_bet = current_bet
    if HI_LO_COUNT > 5:
        next_hand_bet *= 2
    elif HI_LO_COUNT < -5:
        next_hand_bet /= 2

    # Playing Deviations
    if (no_split is False) and (len(player_hand) == 2) and (player_hand[0] == player_hand[1]):
        # Player has a pair, check if it's a good idea to split
        if player_hand[0] in ["A"]:
            return "split", next_hand_bet
        elif player_hand[0] in ["8"]:
            return "split", next_hand_bet
        elif player_hand[0] in ["9"]:
            if dealer_hand[0] in ["7", "T", "J", "Q", "K", "A"]:
                return "stand", next_hand_bet
            else:
                return "split", next_hand_bet
        elif player_hand[0] in ["2", "3", "4", "5", "6"]:
            return "split", next_hand_bet
        else:
            return "stand", next_hand_bet
    else:
        # Calculate total points
        points = 0
        num_aces = 0
        for card in player_hand:
            if card in ["T", "J", "Q", "K"]:
                points += 10
            elif card == "A":
                points += 11
                num_aces += 1
            else:
                points += int(card)
        while (points > 21) and (num_aces > 0):
            points -= 10
            num_aces -= 1

        if points < 17:
            return "hit", next_hand_bet
        elif points > 21:
            return "stand", next_hand_bet
        elif ((points == 17) and (len(player_hand) == 2)
                and ("A" in player_hand)):
            return "double", next_hand_bet
        else:
            return "stand", next_hand_bet

while True:
    # Get the player's hand, dealer hand and current bet
    player_hand_str = str(input(f"Hi-Lo[{HI_LO_COUNT}] [New Hand] Enter your hand (comma-separated): "))
    dealer_hand_str = str(input(f"Hi-Lo [{HI_LO_COUNT}] [New Hand] Enter the dealer's hand (comma-separated): "))
    current_bet = float(input(f"Hi-Lo [{HI_LO_COUNT}] [New Hand] Enter the current bet: "))

    # Convert the input strings to lists of strings
    player_hand = [str(card) for card in player_hand_str.split(',')]
    dealer_hand = [str(card) for card in dealer_hand_str.split(',')]
    
    while True:
        # Get the optimal move and next bet size
        optimal_move, next_hand_bet = get_optimal_move(current_bet, dealer_hand, player_hand)

        if optimal_move == "hit":
            new_card = str(input(f"{player_hand} -> [{optimal_move}] Enter the new card: "))
            player_hand.append(new_card)
        if optimal_move == "split":
            first_hand_str = str(input(f"[{optimal_move}] Enter the first hand: "))
            second_hand_str = str(input(f"[{optimal_move}] Enter the second hand: "))
            first_hand = [str(card) for card in first_hand_str.split(',')]
            second_hand = [str(card) for card in second_hand_str.split(',')]

            while True:
                first_hand_optimal_move, next_hand_bet = get_optimal_move(current_bet, dealer_hand, first_hand, no_split=True)
                if first_hand_optimal_move == "hit":
                    new_card = str(input(f"First hand {first_hand} -> [{first_hand_optimal_move}] Enter the new card: "))
                    first_hand.append(new_card)
                if (first_hand_optimal_move == "stand"
                    or first_hand_optimal_move == "double"):
                    print(f"First hand {first_hand} -> [{first_hand_optimal_move}]")
                    break
            
            while True:
                second_hand_optimal_move, next_hand_bet = get_optimal_move(current_bet, dealer_hand, second_hand, no_split=True)
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