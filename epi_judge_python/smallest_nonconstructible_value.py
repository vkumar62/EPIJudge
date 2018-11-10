from test_framework import generic_test


def smallest_nonconstructible_value(A):
    # TODO - you fill in here.
    max_construct = 0
    for a in sorted(A):
        if a > max_construct + 1:
            break
        max_construct += a
    return max_construct + 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("smallest_nonconstructible_value.py",
                                       'smallest_nonconstructible_value.tsv',
                                       smallest_nonconstructible_value))
