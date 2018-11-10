from test_framework import generic_test

import pdb
def square_root(k):
    # TODO - you fill in here.
#    pdb.set_trace()
    left , right = 0, k
    root = 0

    while left <= right:
        mid = (left + right) // 2
        if mid**2 > k:
            right = mid - 1
        else:
            root = mid
            left = mid + 1

    return root 


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("int_square_root.py",
                                       "int_square_root.tsv", square_root))
