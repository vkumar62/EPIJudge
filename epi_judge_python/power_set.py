from test_framework import generic_test, test_utils


def generate_power_set(S):
    # TODO - you fill in here.
    def power_set(offset, partial):
        if offset == len(S):
            results.append(partial)
            return
        power_set(offset+1, partial)
        power_set(offset+1, partial + [S[offset]])

    results = []
    power_set(0, [])
    return results


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("power_set.py", 'power_set.tsv',
                                       generate_power_set,
                                       test_utils.unordered_compare))
