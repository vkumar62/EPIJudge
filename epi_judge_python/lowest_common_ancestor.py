import functools

from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node, strip_parent_link
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

from collections import namedtuple

LcaReturn = namedtuple('LcaReturn', 'common count')

def lca(tree, node0, node1):
    def lca_helper(tree, node0, node1):
        if tree is None:
            return LcaReturn(None, 0)

        if tree == node0 and tree == node1:
            return LcaReturn(tree, 2)

        count = 0
        if tree == node0:
            count = 1

        if tree == node1:
            count = 1

        left = lca_helper(tree.left, node0, node1)
        if left.count == 2:
            return left

        right = lca_helper(tree.right, node0, node1)
        if right.count == 2:
            return right

        common = tree if count + left.count + right.count == 2 else None
        return LcaReturn(common, count + left.count + right.count)

    return lca_helper(tree, node0, node1).common

@enable_executor_hook
def lca_wrapper(executor, tree, key1, key2):
    strip_parent_link(tree)
    result = executor.run(
        functools.partial(lca, tree, must_find_node(tree, key1),
                          must_find_node(tree, key2)))

    if result is None:
        raise TestFailure("Result can't be None")
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("lowest_common_ancestor.py",
                                       'lowest_common_ancestor.tsv',
                                       lca_wrapper))
