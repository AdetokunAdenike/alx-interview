#!/usr/bin/python3
"""
Module for solving the coin change problem.

This module provides an efficient function to determine the minimum
number of coins required to make up a specific total amount.
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
    # Handle edge cases
    if total <= 0:
        return 0
    if not coins:
        return -1

    # Sort coins in descending order for more efficient processing
    coins.sort(reverse=True)

    # Initialize minimum coins needed to max possible value
    min_coins = float('inf')

    def backtrack(remaining, coins_used, coin_index):
        """
        Recursive backtracking to find minimum coins.

        Args:
            remaining (int): Remaining amount to make change for.
            coins_used (int): Number of coins used so far.
            coin_index (int): Current index in coins list.

        Returns:
            int: Minimum coins needed or float('inf') if impossible.
        """
        nonlocal min_coins

        # Base cases
        if remaining == 0:
            min_coins = min(min_coins, coins_used)
            return coins_used
        if remaining < 0 or coin_index >= len(coins):
            return float('inf')

        # Optimization: early stopping if current coins used exceeds known minimum
        if coins_used >= min_coins:
            return float('inf')

        # Try using current coin as many times as possible
        coin = coins[coin_index]
        max_coin_count = remaining // coin

        best_result = float('inf')
        for count in range(max_coin_count + 1):
            result = backtrack(
                remaining - count * coin,
                coins_used + count,
                coin_index + 1
            )
            best_result = min(best_result, result)

        return best_result

    # Find minimum coins needed
    result = backtrack(total, 0, 0)

    # Return result or -1 if impossible
    return result if result != float('inf') else -1
