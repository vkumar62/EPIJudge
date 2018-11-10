from test_framework import generic_test
from collections import defaultdict

def can_form_palindrome(s):
    # TODO - you fill in here.
    counter = defaultdict(int)

    for c in s:
        counter[c] += 1

    odd_count = 0
    for count in counter.values():
        if count%2:
            odd_count += 1
            if odd_count > 1:
                return False
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "is_string_permutable_to_palindrome.py",
            'is_string_permutable_to_palindrome.tsv', can_form_palindrome))
