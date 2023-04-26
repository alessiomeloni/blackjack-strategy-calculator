def bet_size_advanced(betting_system, true_count, base_bet=10, bet_spread=8, **kwargs):
    if  betting_system == "martingale":
        loss_streak = kwargs.get("loss_streak", 0)
        return base_bet * (2 ** loss_streak)
    elif betting_system == "fibonacci":
        fib_index = kwargs.get("fib_index", 0)
        fib_seq = [1, 1]
        for _ in range(fib_index):
            fib_seq.append(fib_seq[-1] + fib_seq[-2])
        
        return base_bet * fib_seq[fib_index]
    else:  # Default: Hi-Lo betting
        bet_size = max(min(base_bet * (true_count + 1), base_bet * bet_spread), base_bet)
        return bet_size