from test_framework import generic_test


def longest_contained_range(A):
    # TODO - you fill in here.
    all_entries = set(A)

    max_size = 0
    while all_entries:
        a = all_entries.pop()

        i = 1
        while True:
            if a-i in all_entries:
                all_entries.remove(a-i)
                i += 1
            else:
                break

        j = 1
        while True:
            if a+j in all_entries:
                all_entries.remove(a+j)
                j += 1
            else:
                break

        max_size = max(max_size, i + j - 1)

    return max_size


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("longest_contained_interval.py",
                                       'longest_contained_interval.tsv',
                                       longest_contained_range))
