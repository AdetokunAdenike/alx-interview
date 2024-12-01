#!/usr/bin/python3
def makeChange(coins, total):
    """
    Returns the fewest number of coins needed to make up a given total.
    Parameters:
    coins (list of int): The available coin denominations.
    total (int): The target amount.
    Returns:
    int: The fewest number of coins needed, or -1 if the total cannot be made.
    """
    # Handle edge cases first
    if total <= 0:
        return 0
    
    # Handle case of no coins
    if not coins:
        return -1
    
    # Initialize DP table with a large value (total + 1)
    dp = [float('inf')] * (total + 1)
    
    # Base case: 0 coins needed to make 0
    dp[0] = 0
    
    # Iterate through all possible totals from 1 to target total
    for i in range(1, total + 1):
        # Try each coin
        for coin in coins:
            # If coin is less than or equal to current total
            if coin <= i:
                # Update minimum coins needed
                dp[i] = min(dp[i], dp[i - coin] + 1)
    
    # If no solution found, return -1
    # Otherwise return the minimum number of coins
    return dp[total] if dp[total] != float('inf') else -1
