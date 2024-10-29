#!/usr/bin/python3
"""
In a text file, there is a single character H. Your text editor can execute
only two operations in this file: Copy All and Paste. Given a number n, write
a method that calculates the fewest number of operations needed to result in
exactly n H characters in the file.

    Prototype: def minOperations(n)
    Returns an integer
    If n is impossible to achieve, return 0

Example:

n = 9

H => Copy All => Paste => HH => Paste =>HHH => Copy All => Paste => HHHHHH =>
Paste => HHHHHHHHH

Number of operations: 6
"""


def minOperations(n):
    if n <= 1:
        return 0

    divisor = 2
    num_of_operations = 0

    while n > 1:
        if n % divisor == 0:
            n = n / divisor
            num_of_operations += divisor
        else:
            divisor += 1

    return num_of_operations

# Test cases
n = 12
print(minOperations(n))  # Expected output: 7

n = 9
print(minOperations(n))  # Expected output: 6
