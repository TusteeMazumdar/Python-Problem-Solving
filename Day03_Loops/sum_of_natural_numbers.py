"""
Problem:
Given an integer n, calculate the sum of all natural numbers
from 1 to n (inclusive).

If n is 0, the sum should be 0.

Example:
Input:  n = 5
Output: 15

Approach:
- Initialize a variable to store the sum
- Use a loop from 1 to n and accumulate the sum

Time Complexity: O(n)
Space Complexity: O(1)
"""

def sum_of_natural_numbers(n):
    total = 0

    for i in range(1, n + 1):
        total += i

    return total


if __name__ == "__main__":
    n = 5
    print(sum_of_natural_numbers(n))
