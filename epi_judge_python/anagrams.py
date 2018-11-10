from test_framework import generic_test, test_utils
from collections import defaultdict

def find_anagrams(dictionary):
    # TODO - you fill in here.
    anagrams_table = defaultdict(list)

    for s in dictionary:
        anagrams_table[''.join(sorted(s))].append(s)

    return [s for s in anagrams_table.values() if len(s) > 1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "anagrams.py",
            "anagrams.tsv",
            find_anagrams,
            comparator=test_utils.unordered_compare))
