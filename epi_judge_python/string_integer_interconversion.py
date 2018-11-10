from test_framework import generic_test
from test_framework.test_failure import TestFailure

import pdb
def int_to_string(x):
    # TODO - you fill in here.
#    pdb.set_trace()
    s = []
    y = abs(x)

    while True:
        s.append(chr(ord('0') + y%10))
        y //= 10
        if y == 0:
            break
    if x < 0:
        s.append('-')
    s = ''.join(reversed(s))
    return s



def string_to_int(s):
    # TODO - you fill in here.
    x = ord(s[0]) - ord('0') if s[0] != '-' else 0

    for i in range(1, len(s)):
        x *= 10
        x += ord(s[i]) - ord('0')

    return x if s[0] != '-' else -x


def wrapper(x, s):
    if int_to_string(x) != s:
        raise TestFailure("Int to string conversion failed")
    if string_to_int(s) != x:
        raise TestFailure("String to int conversion failed")


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("string_integer_interconversion.py",
                                       'string_integer_interconversion.tsv',
                                       wrapper))
