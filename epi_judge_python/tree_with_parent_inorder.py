from test_framework import generic_test

# inorder with O(1) space
def inorder_traversal(tree):
    def visit(node):
        visits.append(node.data)

    prev = None
    cur = tree
    visits = []

    while cur:
        if cur.parent == prev:
            if cur.left:
                next = cur.left
            else:
                visit(cur)
                next = cur.right if cur.right else cur.parent
        elif cur.left == prev:
            visit(cur)
            next = cur.right if cur.right else cur.parent
        else:
            next = cur.parent
        prev = cur
        cur = next

    return visits

def preorder_traversal(tree):
    def visit(node):
        visits.append(node.data)

    cur = tree
    visits = []

    while cur:
        visit(cur)
        if cur.left:
            next = cur.left
        elif cur.right:
            next = cur.right
        else:
            next = None
            while node.parent:
                if node == node.parent.left and node.parent.right:
                    next = node.parent.right
                    break
                else:
                    node = node.parent
        cur = next
    return visits

def postorder_traversal(tree):
    def visit(node):
        visits.append(node.data)

    cur = tree
    visits = []

    while cur:
        if cur.left:
            next = cur.left
        elif cur.right:
            next = cur.right
        else:
            visit(cur)
            next = None
            while cur.parent and cur == cur.parent.right:
                cur = cur.parent
            if cur.parent:
                next = cur.parent.right if cur.parent.right else cur.parent
        cur = next

    return visits

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_with_parent_inorder.py",
                                       'tree_with_parent_inorder.tsv',
                                       inorder_traversal))
