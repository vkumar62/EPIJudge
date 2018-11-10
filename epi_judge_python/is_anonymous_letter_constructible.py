from test_framework import generic_test
from collections import Counter
from collections import defaultdict


def is_letter_constructible_from_magazine(letter_text, magazine_text):
    # TODO - you fill in here.
    #letter_char_counts = Counter(letter_text)
    #return True
    letter_char_counts = defaultdict(int)

    for l in letter_text:
        letter_char_counts[l] += 1

    for l in magazine_text:
        if l in letter_char_counts:
            letter_char_counts[l] -= 1
            if letter_char_counts[l] == 0:
                del letter_char_counts[l]
            if not letter_char_counts:
                break
    return not letter_char_counts
    #return not Counter(letter_text)-Counter(magazine_text)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_anonymous_letter_constructible.py",
                                       'is_anonymous_letter_constructible.tsv',
                                       is_letter_constructible_from_magazine))
