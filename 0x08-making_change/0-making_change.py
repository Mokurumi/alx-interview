#!/usr/bin/python3
"""
Module that determines the fewest number of coins needed
to meet a given amount total.
"""


def makeChange(coins, total):
    """
    Given a pile of coins of different values,
    determine the fewest number of coins needed to meet a given amount total.
    """
    if total <= 0:
        return 0
    coins.sort(reverse=True)
    i = 0
    num_coins = 0
    while total > 0 and i < len(coins):
        if coins[i] <= total:
            total -= coins[i]
            num_coins += 1
        else:
            i += 1
    if total == 0:
        return num_coins
    return -1
