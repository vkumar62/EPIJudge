from test_framework import generic_test


def palindrome_decompositions(input):
    # TODO - you fill in here.
    def helper(offset, partial):
        if offset == len(input):
            result.append(partial)
            return

        for j in range(offset+1, len(input)+1):
            prefix = input[offset:j]
            if prefix == prefix[::-1]:
                helper(j, partial + [input[offset:j]])

    result = []
    helper(0, [])
    return result


def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "enumerate_palindromic_decompositions.py",
            'enumerate_palindromic_decompositions.tsv',
            palindrome_decompositions, comp))
