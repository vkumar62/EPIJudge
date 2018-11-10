from test_framework import generic_test


def search_first_of_k(A, k):
    # TODO - you fill in here.
    left, right = 0, len(A) - 1
    first_k = -1

    while left <= right:
        mid = (left + right) // 2
        if A[mid] == k:
            first_k = mid
            right = mid - 1
        elif A[mid] > k:
            right = mid - 1
        else:
            left = mid + 1

    return first_k


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "search_first_key.py", 'search_first_key.tsv', search_first_of_k))
