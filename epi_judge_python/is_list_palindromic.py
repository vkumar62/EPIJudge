from test_framework import generic_test


def reverse(L):
    node = L
    prev = None
    while node:
        node_next = node.next
        node.next = prev
        prev = node 
        node = node_next
    return prev


def is_linked_list_a_palindrome(L):
    # TODO - you fill in here.

    if not L:
        return True
    mid = tail = L

    while tail and tail.next:
        mid, tail = mid.next, tail.next.next

#    rev_head = reverse(mid.next)
#    mid.next = None
    rev_head = reverse(mid.next)

    fwd_iter, rev_iter = L, rev_head
    while fwd_iter and rev_iter:
        if fwd_iter.data != rev_iter.data:
            return False
        fwd_iter, rev_iter = fwd_iter.next, rev_iter.next

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_list_palindromic.py",
                                       'is_list_palindromic.tsv',
                                       is_linked_list_a_palindrome))
