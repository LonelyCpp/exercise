def check_unique_wds(string):
    """
    Checks if a string has all unique characters using an extra data structure.
    A loop is used here instead of set(string) since the loop can be stopped at
    the first non unique character found
    """
    seen = set()
    for ch in string:
        if ch in seen:
            return (string, False)
        seen.add(ch)

    return (string, True)


def get_bit(num, pos):
    return (num >> pos) & 1


def check_unique_nds(string):
    """
    Checks if a string has all unique characters using WITHOUT an extra data structure.
    uses bit manipulation to keep track of characters
    """
    check_bits = 0
    for ch in string:
        ch_ascii = ord(ch)

        if get_bit(check_bits, ch_ascii):
            return (string, False)

        mask = 1 << ch_ascii
        check_bits = check_bits | mask

    return (string, True)


if __name__ == '__main__':
    print(check_unique_wds('hello'))
    print(check_unique_wds('helo'))
    print(check_unique_wds('abcd'))
    print(check_unique_wds('abccdddaarr'))

    print(check_unique_nds('hello'))
    print(check_unique_nds('helo'))
    print(check_unique_nds('abcd'))
    print(check_unique_nds('abccdddaarr'))
