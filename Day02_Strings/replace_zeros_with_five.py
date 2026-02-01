"""
Problem:
Given an integer n, replace all occurrences of digit 0 with 5.

Example:
Input:  n = 1004
Output: 1554

Approach:
- Convert the number to string
- Replace '0' with '5'
- Convert back to integer

Time Complexity: O(d), where d is number of digits
Space Complexity: O(d)
"""

def replace_zeros_with_five(n):
    result = ""

    for char in str(n):
        if char == '0':
            result += '5'
        else:
            result += char

    return int(result)


if __name__ == "__main__":
    n = 1004
    print(replace_zeros_with_five(n))
