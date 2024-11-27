#!/usr/bin/python3
"""
Module to determine the fewest number of coins needed
to meet a given amount total.
"""


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given amount total.

    Args:
        coins (list of int): A list of coin denominations available.
        total (int): The target amount to make change for.

    Returns:
        int: The fewest number of coins needed to meet the total.
             Returns -1 if the total cannot be met by any number of coins.
    """
    if total <= 0:
        return 0

    coins.sort(reverse=True)

    min_coins = 0
    remaining_total = total

    for coin_value in coins:
        if remaining_total >= coin_value:
            num_coins = remaining_total // coin_value
            remaining_total -= num_coins * coin_value
            min_coins += num_coins

    if remaining_total == 0:
        return min_coins
    else:
        return -1


