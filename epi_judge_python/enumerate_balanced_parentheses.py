from test_framework import generic_test, test_utils


def generate_balanced_parentheses(num_pairs):
    # TODO - you fill in here.
    def parens_helper(left_parens, right_parens, partial):
        if left_parens == right_parens == 0:
            result.append(partial)
            return

        if left_parens > 0:
            parens_helper(left_parens-1, right_parens, partial + '(')
        if left_parens < right_parens:
            parens_helper(left_parens, right_parens-1, partial+')')

    result = []
    parens_helper(num_pairs, num_pairs, '')
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("enumerate_balanced_parentheses.py",
                                       'enumerate_balanced_parentheses.tsv',
                                       generate_balanced_parentheses,
                                       test_utils.unordered_compare))
