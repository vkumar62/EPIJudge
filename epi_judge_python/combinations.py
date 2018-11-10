from test_framework import generic_test, test_utils


def combinations(n, k):
    # TODO - you fill in here.
    def helper(offset, partial):
        if len(partial) == k:
            result.append(partial)
            return

        num_remaining = k-len(partial)
        for i in range(offset, n-num_remaining+2):
            helper(i+1, partial + [i])

    result = []
    helper(1, [])
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "combinations.py",
            'combinations.tsv',
            combinations,
            comparator=test_utils.unordered_compare))
