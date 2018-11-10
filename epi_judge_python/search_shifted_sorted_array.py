from test_framework import generic_test

import pdb
def search_smallest(A):
    # TODO - you fill in here.
#    pdb.set_trace()
    left, right = 0, len(A)-1
    smallest_i = -1
    smallest = float('inf')
    
    while left <= right:
        mid = (left + right) // 2
        if A[mid] < smallest:
            smallest = A[mid]
            smallest_i = mid
        if A[mid] > A[right]:
            left = mid + 1
        else:
            right = mid - 1

    return smallest_i 


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("search_shifted_sorted_array.py",
                                       'search_shifted_sorted_array.tsv',
                                       search_smallest))
