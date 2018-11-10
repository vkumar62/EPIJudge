import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

import pdb


# Assume s is a string encoded as bytearray.
def reverse_words(s):
    # TODO - you fill in here.
    def reverse_helper(s, l, r):
        while l < r:
            s[l], s[r] = s[r], s[l]
            l, r = l+1, r-1

#    pdb.set_trace()
#    reverse_helper(s, 0, len(s)-1)
#    s.reverse()
    l = 0
    for r in range(0, len(s)):
        if s[r] == ord(' '):
#            pdb.set_trace()
            reverse_helper(s, l, r-1)
            l = r + 1

#    if s[-1] != ord(' '):
    reverse_helper(s, l, len(s)-1)

    return reverse_helper(s, 0, len(s)-1)


@enable_executor_hook
def reverse_words_wrapper(executor, s):
    s_copy = bytearray()
    s_copy.extend(map(ord, s))

    executor.run(functools.partial(reverse_words, s_copy))

    return s_copy.decode("utf-8")


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("reverse_words.py", 'reverse_words.tsv',
                                       reverse_words_wrapper))
