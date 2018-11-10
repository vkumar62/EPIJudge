
from collections import namedtuple

BalanceData = namedtuple('BalanceData', 'is_balanced, height')
class TreeNode:
    def __init__(self):
        self.right = None
        self.left = None
        self.data = None


# Space - O(h)
# Time - O(n)
def is_tree_balanced(root):
    def is_tree_balanced_helper(node):
        if not node:
            return BalanceData(True, 0)

        right = is_tree_balanced_helper(node.right)
        left = is_tree_balanced_helper(node.right)

        if not right.is_balanced or not left.is_balanced:
            return BalanceData(False, -1)

        if abs(right.height - left.height) > 1:
            return BalanceData(False, -1)

        return BalanceData(True, 1 + max(right.height, left.height))

