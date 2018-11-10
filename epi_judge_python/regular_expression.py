from test_framework import generic_test


def is_match(regex, s):
    # TODO - you fill in here.
    def regex_helper(regex, s):
        if not regex:
            return True

        if regex == '$':
            return s == ''

        if len(regex) >= 2 and regex[1] == '*':
            i = 1
            while i <= len(s) and (regex[0] == s[i-1] or regex[0] == '.'):
                if regex_helper(regex[2:], s[i:]):
                    return True
                i += 1
            return regex_helper(regex[2:], s)

        if s and (s[0] == regex[0] or regex[0] == '.'):
            return regex_helper(regex[1:], s[1:])
        return False

    if regex[0] == '^':
        return regex_helper(regex[1:], s)
    for i in range(len(s) + 1):
        if regex_helper(regex, s[i:]):
            return True
    return False


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("regular_expression.py",
                                       'regular_expression.tsv', is_match))
