from test_framework import generic_test
import string
import functools


def ss_decode_col_id(col):
    # TODO - you fill in here.

    x = functools.reduce(lambda result, c: result*26 + string.ascii_uppercase.index(c.upper()) + 1,
            col, 0)
    return x



# This does the reverse operation
def ss_encode_col_id(col):
    s = []
    while True:
        col -= 1
        s.append(string.ascii_uppercase[col%26])
        col //=26
        if col == 0:
            break
    return ''.join(s)



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("spreadsheet_encoding.py",
                                       'spreadsheet_encoding.tsv',
                                       ss_decode_col_id))
