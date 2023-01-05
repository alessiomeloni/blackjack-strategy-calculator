class BlackjackStrategy:
    def __init__(self):
        self.HI_LO_COUNT = 0

    def count_cards(self, hand):
        """Updates the HI_LO_COUNT based on the given hand."""
        for card in hand:
            if card in ["T", "J", "Q", "K", "A"]:
                self.HI_LO_COUNT -= 1
            elif card in ["2", "3", "4", "5", "6"]:
                self.HI_LO_COUNT += 1

    def calculate_bet(self, current_bet):
        """Calculates the optimal bet for the next hand based on the HI_LO_COUNT."""
        if self.HI_LO_COUNT > 5:
            return current_bet * 2
        elif self.HI_LO_COUNT < -5:
            return current_bet / 2
        return current_bet

    def should_split(self, dealer_hand, player_hand):
        """Determines if the player should split their hand based on the cards in the dealer's hand and the player's hand."""
        if (len(player_hand) != 2) or (player_hand[0] != player_hand[1]):
            return False
        if player_hand[0] in ["A"]:
            return True
        elif player_hand[0] in ["8"]:
            return True
        elif player_hand[0] in ["9"]:
            if dealer_hand[0] in ["7", "T", "J", "Q", "K", "A"]:
                return False
            else:
                return True
        elif player_hand[0] in ["2", "3", "4", "5", "6"]:
            return True
        return False

    def calculate_points(self, hand):
        """Calculates the total points in the given hand."""
        points = 0
        num_aces = 0
        for card in hand:
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
        return points
    
    def get_optimal_move(self, current_bet, dealer_hand, player_hand, no_split=False):
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
        self.count_cards(dealer_hand)
        self.count_cards(player_hand)
        next_hand_bet = self.calculate_bet(current_bet)
        if (no_split is False) and self.should_split(dealer_hand, player_hand):
            return "split", next_hand_bet
        points = self.calculate_points(player_hand)
        if points < 17:
            return "hit", next_hand_bet
        elif points > 21:
            return "stand", next_hand_bet
        elif (points == 17) and (len(player_hand) == 2) and ("A" in player_hand):
            return "double", next_hand_bet
        return "stand", next_hand_bet