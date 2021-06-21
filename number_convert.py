def from_ten(num, base):
    res = []

    while num > 0:
        n = num % base
        res.insert(0, only_digit_from_ten(n, base))
        num = num // base

    return ''.join(res)


def to_ten(num, base):
    res = 0
    for i in str(num):
        res = res * base + int(only_digit_to_ten(i, base))

    return res


def only_digit_from_ten(n, base):
    if base > 9:
        num_dict = {i: chr(ord('A') + i) for i in range(base - 10)}

    return str(n) if n < 10 else num_dict.get(n - 10)


def only_digit_to_ten(n_str, base):
    if base > 9:
        num_dict = {chr(ord('A') + i): str(i + 10) for i in range(base - 10)}

    return n_str if ord(n_str) <= ord('9') else num_dict.get(n_str)


if __name__ == "__main__":
    num1 = 2
    base1 = 2
    num2 = 7
    base2 = 2
    num3 = 16
    base3 = 8
    num4 = 16
    base4 = 16
    num5 = 31
    base5 = 16

    print(f"10 base {num1} => {base1} base {from_ten(num1, base1)}")
    print(f"10 base {num2} => {base2} base {from_ten(num2, base2)}")
    print(f"10 base {num3} => {base3} base {from_ten(num3, base3)}")
    print(f"10 base {num4} => {base4} base {from_ten(num4, base4)}")
    print(f"10 base {num5} => {base5} base {from_ten(num5, base5)}")

    print("=========================================================")

    num_str1 = '111'
    base1 = 2
    num_str2 = '1000'
    base2 = 2
    num_str3 = '7107'
    base3 = 8
    num_str4 = '10'
    base4 = 8
    num_str5 = '1F'
    base5 = 16
    print(f"{base1} base {num_str1} => 10 base {to_ten(num_str1, base1)}")
    print(f"{base2} base {num_str2} => 10 base {to_ten(num_str2, base2)}")
    print(f"{base3} base {num_str3} => 10 base {to_ten(num_str3, base3)}")
    print(f"{base4} base {num_str4} => 10 base {to_ten(num_str4, base4)}")
    print(f"{base5} base {num_str5} => 10 base {to_ten(num_str5, base5)}")

    print("=========================================================")
    from IPython import embed
    embed()
