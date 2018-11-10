from test_framework import generic_test
from list_node import ListNode


def merge_two_sorted_lists(L1, L2):
    # TODO - you fill in here.
    dummy_head = ListNode(0)
    tail = dummy_head

    while L1 and L2:
        if L1.data < L2.data:
            tail.next = L1
            L1 = L1.next
        else:
            tail.next = L2
            L2 = L2.next
        tail = tail.next

    if L1:
        tail.next = L1
    else:
        tail.next = L2
    return dummy_head.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sorted_lists_merge.py",
                                       'sorted_lists_merge.tsv',
                                       merge_two_sorted_lists))
