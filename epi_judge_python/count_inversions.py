from sortedcontainers import SortedList
from test_framework import generic_test


def count_inversions(A):
    # TODO - you fill in here.
    s = SortedList()

    inversions = 0

    for num in A:
        inversions += len(s) - s.bisect(num)
        s.add(num)
    return inversions


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "count_inversions.py", 'count_inversions.tsv', count_inversions))
