from test_framework import generic_test
from list_node import ListNode

import pdb
def reverse_sublist(L, start, finish):
#    pdb.set_trace()
    # TODO - you fill in here.
    if not L:
        return L

    dummy_head = ListNode(0, L)
    tail = dummy_head
    nodeid = 1 

    while nodeid < start and tail:
        tail = tail.next
        nodeid += 1

    if not tail:
        return L

    reverse_tail = tail.next
    while nodeid < finish:
        nodeid += 1

        if False:
            next_next = reverse_tail.next
            reverse_tail.next = next_next.next
            next_next.next = tail.next
            tail.next = next_next

        if True:
            next_next = reverse_tail.next
            reverse_tail.next = next_next.next
            next_next.next = tail.next
            tail.next = next_next

    return dummy_head.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("reverse_sublist.py",
                                       "reverse_sublist.tsv", reverse_sublist))
