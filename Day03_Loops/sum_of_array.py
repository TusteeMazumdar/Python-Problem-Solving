"""
Problem:
Given an integer array, find the sum of all its elements.

Example:
Input:  [1, 2, 3, 4]
Output: 10

Approach:
- Initialize a variable to store the sum
- Traverse the array and add each element

Time Complexity: O(n)
Space Complexity: O(1)
"""

def sum_of_array(arr):
    total = 0

    for num in arr:
        total += num

    return total


if __name__ == "__main__":
    arr = [1, 2, 3, 4]
    print(sum_of_array(arr))
