from test_framework import generic_test


def is_palindrome(s):
    # TODO - you fill in here.
    l, r = 0, len(s)-1

    while l < r:
        if s[l].isalnum() and s[r].isalnum():
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        elif s[l].isalnum():
            r -= 1
        else:
            l += 1
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_string_palindromic_punctuation.py",
                                       "is_string_palindromic_punctuation.tsv",
                                       is_palindrome))
