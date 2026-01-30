"""
Problem:
Given an array of positive integers, return the count of
odd and even numbers.

Output format:
[odd_count, even_count]

Example:
Input:  [1, 2, 3, 4, 5]
Output: [3, 2]

Approach:
- Traverse the array
- Use modulo (%) operator to classify odd and even numbers

Time Complexity: O(n)
Space Complexity: O(1)
"""

def count_odd_even(arr):
    odd_count = 0
    even_count = 0

    for num in arr:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    return [odd_count, even_count]


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    print(count_odd_even(arr))
