from test_framework import generic_test
from collections import namedtuple

BalanceData = namedtuple('BalanceData', 'is_balanced, height')

def is_balanced_binary_tree(tree):
    def is_tree_balanced_helper(node):
        if not node:
            return BalanceData(True, 0)

        right = is_tree_balanced_helper(node.right)
        if not right.is_balanced:
            return BalanceData(False, -1)

        left = is_tree_balanced_helper(node.left)

        if not left.is_balanced:
            return BalanceData(False, -1)

        return BalanceData(abs(right.height - left.height) <=1, 
                            1 + max(right.height, left.height))

    return is_tree_balanced_helper(tree).is_balanced

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_tree_balanced.py",
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
