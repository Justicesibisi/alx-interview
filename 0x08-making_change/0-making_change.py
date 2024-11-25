#!/usr/bin/python3
"""
Coin Change Problem
"""


def makeChange(coins, total):
    """
    Determine the minimum number of coins needed to make up a given amount.

    :param coins: List of coin denominations
    :param total: Total amount to make change for
    :return: Minimum number of coins needed or -1 if it's not possible
    """
    if total <= 0:
        return 0

    # Initialize a list to store the minimum coins needed for each amount
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins needed to make 0

    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1


