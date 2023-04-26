# imports
from best_move_advaced import best_move_advanced
from BettingStrategy import BettingStrategy


# round 1
player_hand = [1, 2, 9, 9]
dealer_hand = [10, 3]
seen_cards = [5, 6, 10, 9, 4, 7, 8, 7, 8, 3, 5]

#  Keep in mind that both the Martingale and Fibonacci betting systems 
# require tracking the player's streak of losses or progress through the 
# Fibonacci sequence, so you'll need to manage and update these values 
# in your game or simulation logic accordingly.

# round 1
# Martingale betting system
martingale_strategy = BettingStrategy(system="martingale")
move, bet_size_martingale = best_move_advanced(player_hand, dealer_hand, seen_cards, betting_strategy=martingale_strategy)
print(f"Martingale - Best move: {move}, Bet size: {bet_size_martingale}")
# Example: Update the Martingale betting strategy after a loss
martingale_strategy.on_result("win")

# Fibonacci betting system
fibonacci_strategy = BettingStrategy(system="fibonacci")
move, bet_size_fibonacci = best_move_advanced(player_hand, dealer_hand, seen_cards, betting_strategy=fibonacci_strategy)
print(f"Fibonacci - Best move: {move}, Bet size: {bet_size_fibonacci}")
fibonacci_strategy.on_result("win")

#every roud move values from player and dealer to seen_cards
# round 2
player_hand = [7]
dealer_hand = [4, 2]
seen_cards = [5, 6, 10, 9, 4, 7, 8, 7, 9, 10, 3]

# Martingale betting system
martingale_strategy = BettingStrategy(system="martingale")
move, bet_size_martingale = best_move_advanced(player_hand, dealer_hand, seen_cards, betting_strategy=martingale_strategy)
print(f"Martingale - Best move: {move}, Bet size: {bet_size_martingale}")
# Example: Update the Martingale betting strategy after a loss
martingale_strategy.on_result("lose")

# Example: Update the Martingale betting strategy after a loss

# Fibonacci betting system
fibonacci_strategy = BettingStrategy(system="fibonacci")
move, bet_size_fibonacci = best_move_advanced(player_hand, dealer_hand, seen_cards, betting_strategy=fibonacci_strategy)
print(f"Fibonacci - Best move: {move}, Bet size: {bet_size_fibonacci}")
fibonacci_strategy.on_result("lose")
fibonacci_strategy = BettingStrategy(system="fibonacci")
move, bet_size_fibonacci = best_move_advanced(player_hand, dealer_hand, seen_cards, betting_strategy=fibonacci_strategy)
print(f"Fibonacci - Best move: {move}, Bet size: {bet_size_fibonacci}")
fibonacci_strategy.on_result("lose")
fibonacci_strategy = BettingStrategy(system="fibonacci")
move, bet_size_fibonacci = best_move_advanced(player_hand, dealer_hand, seen_cards, betting_strategy=fibonacci_strategy)
print(f"Fibonacci - Best move: {move}, Bet size: {bet_size_fibonacci}")
fibonacci_strategy.on_result("lose")
fibonacci_strategy = BettingStrategy(system="fibonacci")
move, bet_size_fibonacci = best_move_advanced(player_hand, dealer_hand, seen_cards, betting_strategy=fibonacci_strategy)
print(f"Fibonacci - Best move: {move}, Bet size: {bet_size_fibonacci}")
fibonacci_strategy.on_result("lose")
fibonacci_strategy = BettingStrategy(system="fibonacci")
move, bet_size_fibonacci = best_move_advanced(player_hand, dealer_hand, seen_cards, betting_strategy=fibonacci_strategy)
print(f"Fibonacci - Best move: {move}, Bet size: {bet_size_fibonacci}")
fibonacci_strategy.on_result("lose")