from test_framework import generic_test


def merge_two_sorted_arrays(A, m, B, n):
    # TODO - you fill in here.
    a_idx, b_idx, write_idx = m - 1, n - 1, m + n - 1
    while a_idx >= 0 and b_idx >= 0:
        if A[a_idx] > B[b_idx]:
            A[write_idx] = A[a_idx]
            a_idx = a_idx - 1
        else:
            A[write_idx] = B[b_idx]
            b_idx = b_idx - 1
        write_idx = write_idx - 1
    while b_idx >= 0:
        A[write_idx] = B[b_idx]
        write_idx, b_idx = write_idx - 1, b_idx - 1
    return


def merge_two_sorted_arrays_wrapper(A, m, B, n):
    merge_two_sorted_arrays(A, m, B, n)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("two_sorted_arrays_merge.py",
                                       'two_sorted_arrays_merge.tsv',
                                       merge_two_sorted_arrays_wrapper))
