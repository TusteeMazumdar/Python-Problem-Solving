"""
Problem:
Given two strings, concatenate them and return the result.

Example:
Input:  s1 = "Geeksfor", s2 = "Geeks"
Output: "GeeksforGeeks"

Approach:
- Convert inputs to strings if necessary
- Concatenate using '+' operator

Time Complexity: O(n + m)
Space Complexity: O(n + m)
"""

def concatenate_strings(s1, s2):
    return str(s1) + str(s2)


if __name__ == "__main__":
    s1 = "Geeksfor"
    s2 = "Geeks"
    print(concatenate_strings(s1, s2))
