"""
Problem:
Given an array arr[], return a list of elements in alternate order
(starting from index 0).
...
"""

def get_alternate_elements(arr):
    result = []

    for i in range(len(arr)):
        if i % 2 == 0:
            result.append(arr[i])

    return result


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    print(get_alternate_elements(arr))
