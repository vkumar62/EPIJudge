import functools

from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def lca(node0, node1):
    # TODO - you fill in here.
    ancestors_set = set()

    iter0 = node0
    iter1 = node1
    while iter0 or iter1:
        if iter0:
            if iter0 in ancestors_set:
                return iter0
            ancestors_set.add(iter0)
            iter0 = iter0.parent
        if iter1:
            if iter1 in ancestors_set:
                return iter1
            ancestors_set.add(iter1)
            iter1 = iter1.parent
    return None


@enable_executor_hook
def lca_wrapper(executor, tree, node0, node1):
    result = executor.run(
        functools.partial(lca, must_find_node(tree, node0),
                          must_find_node(tree, node1)))

    if result is None:
        raise TestFailure("Result can't be None")
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "lowest_common_ancestor_close_ancestor.py",
            'lowest_common_ancestor.tsv', lca_wrapper))
