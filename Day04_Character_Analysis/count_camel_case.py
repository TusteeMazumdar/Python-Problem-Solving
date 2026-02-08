def count_camel_case(s):
    camel_case = 0

    for char in s:
        if 65 <= ord(char) <= 90:
            camel_case += 1

    return camel_case


if __name__ == "__main__":
    s = "ckjkUUYII"
    print(count_camel_case(s))
