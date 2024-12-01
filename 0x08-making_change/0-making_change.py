#!/usr/bin/python3
"""
Module for solving the coin change problem.
Determines the minimum number of coins needed to make a total amount.
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given total.

    Args:
        coins (list): Available coin denominations.
        total (int): Target amount to make change for.

    Returns:
        int: Fewest number of coins needed, or -1 if total cannot be met.
    """
    if total <= 0:
        return 0

    # Initialize dp array with large value
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Iterate through all coin denominations
    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # Return result or -1 if impossible
    return dp[total] if dp[total] != float('inf') else -1
