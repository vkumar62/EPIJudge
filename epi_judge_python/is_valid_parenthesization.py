from test_framework import generic_test

import pdb
def is_well_formed(s):
    # TODO - you fill in here.
    MATCHING = { '}':'{', ']':'[', ')':'('}
    parens = []

#    pdb.set_trace()
    for c in s:
        if c not in MATCHING:
            parens.append(c)
        elif not parens or parens.pop() != MATCHING[c]:
            return False
    return len(parens) == 0


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_valid_parenthesization.py",
                                       'is_valid_parenthesization.tsv',
                                       is_well_formed))
