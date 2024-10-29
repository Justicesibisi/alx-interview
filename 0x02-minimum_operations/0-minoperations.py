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

    num_of_operations = 0
    divisor = 2

    # Loop until we reduce n to 1
    while n > 1:
        # While n is divisible by the current divisor
        while n % divisor == 0:
            num_of_operations += divisor  # Add divisor to the operation count
            n /= divisor  # Reduce n by dividing it by divisor

        divisor += 1  # Move to the next potential divisor

    return num_of_operations

# Test cases
print(minOperations(9))   # Expected output: 6
print(minOperations(12))  # Expected output: 7
print(minOperations(3))   # Expected output: 3
print(minOperations(5))   # Expected output: 5
print(minOperations(10))  # Expected output: 7
