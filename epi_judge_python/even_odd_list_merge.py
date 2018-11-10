from test_framework import generic_test
from list_node import ListNode


def even_odd_merge(L):
    # TODO - you fill in here.
    even_head, odd_head = ListNode(0), ListNode(0)
    even_tail, odd_tail = even_head, odd_head

    while L and L.next:
        even_tail.next = L
        odd_tail.next = L.next
        even_tail, odd_tail = even_tail.next, odd_tail.next
        L = L.next.next

    odd_tail.next = None
    if L:
        even_tail.next = L
        even_tail = even_tail.next

    even_tail.next = odd_head.next
    
    return even_head.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("even_odd_list_merge.py",
                                       'even_odd_list_merge.tsv',
                                       even_odd_merge))
