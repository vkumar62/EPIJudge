from test_framework import generic_test
from list_node import ListNode
from sorted_lists_merge import merge_two_sorted_lists

import pdb

# Merge sort
def stable_sort_list(L):
    # TODO - you fill in here.

    #pdb.set_trace()
    
    if not L or not L.next:
        return L

    slow = fast = L

    while fast and fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    slow_next = slow.next
    slow.next = None
    return merge_two_sorted_lists(stable_sort_list(L), stable_sort_list(slow_next))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sort_list.py", 'sort_list.tsv',
                                       stable_sort_list))
