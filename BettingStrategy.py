from bet_size_advaced import bet_size_advanced

class BettingStrategy:
    """
    The BettingStrategy class manages the state of the betting strategy for a blackjack game.

    Attributes:
        system (str): The betting system to use ("hi-lo", "martingale", or "fibonacci").
        base_bet (int): The base bet amount.
        bet_spread (int): The maximum bet spread for the Hi-Lo system.
        loss_streak (int): The current loss streak for the Martingale system.
        fib_index (int): The current index in the Fibonacci sequence for the Fibonacci system.
    """

    def __init__(self, system="hi-lo", base_bet=10, bet_spread=20):
        self.system = system
        self.base_bet = base_bet
        self.bet_spread = bet_spread
        self.loss_streak = 0
        self.fib_index = 0

    def reset(self):
        """Reset the loss streak and Fibonacci index."""
        self.loss_streak = 0
        self.fib_index = 0

    def on_result(self, result):
        """
        Update the betting strategy state based on the result of a hand.

        Args:
            result (str): The result of the hand ("win", "lose", or "push").
        """
        if self.system == "martingale":
            if result == "lose":
                self.loss_streak += 1
                print(self.loss_streak)
            else:
                self.reset()
        elif self.system == "fibonacci":
            if result == "lose":
                self.fib_index += 1
            else:
                self.reset()

    def bet_size(self, true_count):
        """
        Calculate the bet size based on the current betting strategy state and true count.

        Args:
            true_count (float): The current true count.

        Returns:
            int: The recommended bet size.
        """
        return bet_size_advanced(self.system, true_count, self.base_bet, self.bet_spread, loss_streak=self.loss_streak, fib_index=self.fib_index)
    



