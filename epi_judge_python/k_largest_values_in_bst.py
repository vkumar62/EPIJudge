from test_framework import generic_test, test_utils


def find_k_largest_in_bst(tree, k):
    # TODO - you fill in here.
    def find_helper(node):
        if not node:
            return

        find_helper(node.right)

        if len(largest_k) == k:
            return
        largest_k.append(node.data)

        find_helper(node.left)

    largest_k = []
    find_helper(tree)
    return largest_k




if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "k_largest_values_in_bst.py", 'k_largest_values_in_bst.tsv',
            find_k_largest_in_bst, test_utils.unordered_compare))
