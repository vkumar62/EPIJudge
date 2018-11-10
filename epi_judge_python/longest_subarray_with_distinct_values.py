from test_framework import generic_test

import pdb
def longest_subarray_with_distinct_entries(A):
    # TODO - you fill in here.
    prev_index = dict()
    max_len = 0
    start_idx = 0

    for i, a in enumerate(A):
        if a in prev_index:
            if prev_index[a] >= start_idx:
                max_len = max(max_len, i - start_idx)
                start_idx = prev_index[a] + 1
        prev_index[a] = i

    return max(max_len, len(A) - start_idx)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "longest_subarray_with_distinct_values.py",
            'longest_subarray_with_distinct_values.tsv',
            longest_subarray_with_distinct_entries))
