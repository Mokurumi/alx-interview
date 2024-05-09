#!/usr/bin/python3
'''
Minimum Operations
'''


def minOperations(n):
    """
    Calculate the fewest number of operations needed to result
    in exactly n H characters in the file
    """
    if n < 2:
        return 0
    operations = 0
    for i in range(2, n + 1):
        while n % i == 0:
            operations += i
            n /= i
    return operations
