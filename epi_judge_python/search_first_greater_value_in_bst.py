from test_framework import generic_test


def find_first_greater_than_k(tree, k):
    # TODO - you fill in here.
    greater_node = None
    search_node = tree

    while search_node:
        if search_node.data > k:
            greater_node = search_node
            search_node = search_node.left
        else:
            search_node = search_node.right
    return greater_node


def find_first_greater_than_k_wrapper(tree, k):
    result = find_first_greater_than_k(tree, k)
    return result.data if result else -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("search_first_greater_value_in_bst.py",
                                       'search_first_greater_value_in_bst.tsv',
                                       find_first_greater_than_k_wrapper))
