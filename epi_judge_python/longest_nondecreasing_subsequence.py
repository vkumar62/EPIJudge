from test_framework import generic_test


# Time - O(N**2)
# Space - O(N)
def longest_nondecreasing_subsequence_length(A):
    # TODO - you fill in here.
    lis = [1] * len(A)

    for i in range(1, len(A)):
        n = 0
        for j in range(i):
            if A[j] <= A[i]:
                n = max(n, lis[j])
        lis[i] += n

    return max(lis)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "longest_nondecreasing_subsequence.py",
            'longest_nondecreasing_subsequence.tsv',
            longest_nondecreasing_subsequence_length))
