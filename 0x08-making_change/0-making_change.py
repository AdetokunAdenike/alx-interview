def makeChange(coins, total):
    """
    Returns the fewest number of coins needed to make up a given total.

    Parameters:
    coins (list of int): The available coin denominations.
    total (int): The target amount.

    Returns:
    int: The fewest number of coins needed, or -1 if the total cannot be made.

    Example:
    makeChange([1, 2, 25], 37)  # Returns 7
    makeChange([1256, 54, 48, 16, 102], 1453)  # Returns -1
    """

    if total <= 0:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
