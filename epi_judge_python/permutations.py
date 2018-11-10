from test_framework import generic_test, test_utils


def permutations(A):
    def perm_helper(i):
        if i == len(A)-1:
            result.append(A[:])
            return

        for j in range(i, len(A)):
            A[j], A[i] = A[i], A[j]
            perm_helper(i+1)
            A[j], A[i] = A[i], A[j]

    result = []
    perm_helper(0)
    return result

#Leetcode 47 https://leetcode.com/problems/permutations-ii/description/
# DOES NOT WORK
def permutations_duplicates(A):
    def perm_helper(i):
        if i == len(A)-1:
            result.append(A[:])
            return

        for j in range(i, len(A)):
            if A[j] != A[i]:
                A[j], A[i] = A[i], A[j]
                perm_helper(i+1)
                A[j], A[i] = A[i], A[j]

    result = []
    perm_helper(0)
    return result

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("permutations.py", 'permutations.tsv',
                                       permutations,
                                       test_utils.unordered_compare))
