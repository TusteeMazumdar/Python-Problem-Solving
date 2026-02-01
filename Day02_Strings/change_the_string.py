"""
Problem:
Given a string s, change the entire string to lowercase or uppercase
depending on the case of the first character.

Example:
Input:  s = "abCD"
Output: "abcd"

Approach:
- Check the case of the first character
- Convert the full string accordingly

Time Complexity: O(n)
Space Complexity: O(n)
"""

def change_the_string(s):
    if 'a' <= s[0] <= 'z':
        return s.lower()
    else:
        return s.upper()


if __name__ == "__main__":
    s = "abCD"
    print(change_the_string(s))
