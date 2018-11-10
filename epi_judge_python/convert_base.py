from test_framework import generic_test
import string
import functools


def convert_base(num_as_string, b1, b2):
    # TODO - you fill in here.

    is_neg = num_as_string[0] == '-'

    x = functools.reduce(lambda result, c: result*b1 + string.hexdigits.index(c.lower()),
                                num_as_string[is_neg:], 0)

    if False:
        x = string.hexdigits.index(num_as_string[0].lower()) if not is_neg else 0
        for i in range(1, len(num_as_string)):
            x *= b1
            x += string.hexdigits.index(num_as_string[i].lower())

    # Convert to base b2

    s = []

    while True:
        s.append(string.hexdigits[x%b2].upper())
        x //= b2
        if x == 0:
            break

    if is_neg:
        s.append('-')
    return ''.join(reversed(s))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("convert_base.py", "convert_base.tsv",
                                       convert_base))
