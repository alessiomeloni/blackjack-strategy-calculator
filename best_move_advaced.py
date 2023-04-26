
def best_move_advanced(player_hand, dealer_hand, seen_cards, betting_strategy):
    """
    Determine the best move and bet size in blackjack based on the Hi-Lo card counting system
    and an advanced playing strategy that takes into account the composition of the player's hand
    and the true count.

    Parameters:
    player_hand (list[int]): The player's current hand as a list of integers (2-11).
    dealer_hand (list[int]): The dealer's current hand as a list of integers (2-11). Only the first card (upcard) is used.
    seen_cards (list[int]): A list of integers (2-11) representing the cards that have been seen in the game.
    
    Returns:
    tuple[str, float]: A tuple containing the best move as a string ("Hit", "Stay", or "Double") and the recommended bet size as a float.

    Example:
    player_hand = [10, 4]
    dealer_hand = [10]
    seen_cards = [5, 6, 10, 9, 4, 7, 8]

    move, bet_size = best_move_advanced(player_hand, dealer_hand, seen_cards)
    print(f"Best move: {move}, Bet size: {bet_size}")
    """
    # cards
    DECK = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4
    # Calculate the running count
    running_count = 0
    for card in seen_cards:
        if 2 <= card <= 6:
            running_count += 1
        elif card >= 10 or card == 11:
            running_count -= 1

    # Determine the true count
    num_decks_remaining = (len(DECK) - len(seen_cards)) / 52
    true_count = running_count / num_decks_remaining

    # Calculate the bet size
    bet_size = betting_strategy.bet_size(true_count)
    
    # Check for a soft hand (ace that can be counted as 11 without busting)
    is_soft = 11 in player_hand and sum(player_hand) <= 21

    # Get the dealer's upcard
    dealer_upcard = dealer_hand[0]

    # Check for a pair
    is_pair = len(player_hand) == 2 and player_hand[0] == player_hand[1]

    # Strategy adjustments based on the true count
    if true_count > 0:
        if is_soft and sum(player_hand) == 18:
            if dealer_upcard == 9 and true_count >= 1:
                return ("Double", bet_size)
            if dealer_upcard == 6 and true_count >= 1:
                return ("Double", bet_size)
            if dealer_upcard == 5 and true_count >= 1:
                return ("Double", bet_size)
        if not is_soft and sum(player_hand) == 16:
            if dealer_upcard == 10 and true_count >= 4:
                return ("Stay", bet_size)
        if not is_soft and sum(player_hand) == 15:
            if dealer_upcard == 10 and true_count >= 4:
                return ("Stay", bet_size)

    # Basic strategy
    if is_soft:
        if sum(player_hand) >= 19:
            return ("Stay", bet_size)
        if sum(player_hand) == 18 and dealer_upcard in {2, 7, 8}:
            return ("Stay", bet_size)
        if sum(player_hand) == 18 and dealer_upcard in {3, 4, 5, 6}:
            return ("Double", bet_size)
        if sum(player_hand) <= 17 and dealer_upcard in {5, 6}:
            return ("Double", bet_size)
        return ("Hit", bet_size)
    elif is_pair:
        pair_card = player_hand[0]
        if pair_card == 11:
            return ("Split", bet_size)
        if pair_card == 10 and dealer_upcard != 10:
            return ("Split", bet_size)
        if pair_card == 9 and dealer_upcard not in {7, 10, 11}:
            return ("Split", bet_size)
        if pair_card == 8:
            return ("Split", bet_size)
        if pair_card == 7 and dealer_upcard <= 7:
            return ("Split", bet_size)
        if pair_card == 6 and dealer_upcard in {2, 3, 4, 5, 6}:
            return ("Split", bet_size)
        if pair_card == 4 and dealer_upcard in {5, 6}:
            return ("Split", bet_size)
        if pair_card == 2 and dealer_upcard in {4, 5, 6}:
            return ("Split", bet_size)
    else:
        player_total = sum(player_hand)
        if player_total <= 11:
            return ("Hit", bet_size)
        if 12 <= player_total <= 16 and dealer_upcard >= 7:
            return ("Hit", bet_size)
        if 17 <= player_total:
            return ("Stay", bet_size)
   
    return ("Stay", bet_size)