# Blackjack Strategy Calculator

This is a Python function that determines the optimal move for a player in a game of Blackjack, based on three different strategies: the Hi-Lo system, Betting Deviations, and Playing Deviations. The function takes in four arguments: the current bet of the player, the cards in the dealer's hand, the cards in the player's hand, and a boolean value indicating whether the player is allowed to split their hand (default value is False). It returns a tuple containing the optimal move as a string and the optimal bet for the next hand as an integer. The possible values for the move are 'hit', 'stand', 'double', and 'split'.

### This code was written quickly in order to start a community project. Every pull request is welcome in order to make the code more precise and well-structured.

## There are a few things that could be added or improved in this code:

- Implement more advanced betting strategies, such as the Martingale or Fibonacci systems.
- Add support for more complex hand situations, such as soft hands or double downs after splits.
- Implement a strategy for insurance bets.
- Add a function to calculate the expected return for each possible move, taking into account the current bet - and the probability of winning or losing.
- Add support for multiple decks and card counting strategies.
- Implement a simulation to test the effectiveness of different betting and playing strategies, with a target win rate of 55% for the player.
- Write more detailed documentation and examples for each function.

# Usage
### To use the function, import it and call get_optimal_move() with the appropriate arguments:

```Python
from blackjack_strategy import get_optimal_move

current_bet = 100
dealer_hand = ['A', '5']
player_hand = ['T', '6']
move, next_hand_bet = get_optimal_move(current_bet, dealer_hand, player_hand)
print(f'Optimal move: {move}')
print(f'Next hand bet: {next_hand_bet}')
```

## Parameters
- current_bet (int): The current bet of the player.
- dealer_hand (list): A list of strings representing the cards in the dealer's hand. Each string is a single - character representing the rank of the card, with T representing 10, J representing Jack, Q representing Queen, K representing King, and A representing Ace.
- player_hand (list): A list of strings representing the cards in the player's hand. Each string is a single character representing the rank of the card, with T representing 10, J representing Jack, Q representing Queen, K representing King, and A representing Ace.
- no_split (bool): A boolean value indicating whether the player is allowed to split their hand. The default value is False.
- Returns
tuple: A tuple containing the optimal move as a string and the optimal bet for the next hand as an integer. The possible values for the move are 'hit', 'stand', 'double', and 'split'.