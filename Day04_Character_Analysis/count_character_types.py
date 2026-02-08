def count_character_types(s):
    upper_case = 0
    lower_case = 0
    numeric = 0
    special = 0

    for char in s:
        if 65 <= ord(char) <= 90:
            upper_case += 1
        elif 97 <= ord(char) <= 122:
            lower_case += 1
        elif 48 <= ord(char) <= 57:
            numeric += 1
        else:
            special += 1

    return upper_case, lower_case, numeric, special


if __name__ == "__main__":
    s = "#GeeKs01fOr@gEEks07"
    print(count_character_types(s))
