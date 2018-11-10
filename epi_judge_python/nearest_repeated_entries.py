from test_framework import generic_test


def find_nearest_repetition(paragraph):
    # TODO - you fill in here.
    last_occurence_table = dict()
    min_dist = float('inf')

    for i, word in enumerate(paragraph):
        if word in last_occurence_table:
            min_dist = min(i-last_occurence_table[word], min_dist)
        last_occurence_table[word] = i

    return min_dist if min_dist != float('inf') else -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("nearest_repeated_entries.py",
                                       'nearest_repeated_entries.tsv',
                                       find_nearest_repetition))
