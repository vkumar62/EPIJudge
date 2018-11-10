from test_framework import generic_test, test_utils
from collections import deque


MAPPING = ('0', '1', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ')

# Without recursion
def phone_mnemonic(phone_number):
    # TODO - you fill in here.

    stack = deque()
    stack.append('')

    for d in phone_number:
        d = int(d)
        for i in range(len(stack)):
            s = stack.popleft()
            for c in MAPPING[d]:
                stack.append(s + c)
    return list(stack)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "phone_number_mnemonic.py",
            'phone_number_mnemonic.tsv',
            phone_mnemonic,
            comparator=test_utils.unordered_compare))
