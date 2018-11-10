from test_framework import generic_test
from list_node import ListNode


def remove_duplicates(L):
    # TODO - you fill in here.
    node = L

    while node and node.next:
        if node.data == node.next.data:
            node.next = node.next.next
        else:
            node = node.next
    return L

def remove_all_duplicates(L):

    dummy_head = ListNode(0, L)
    node = dummy_head

    while node and node.next:
        dup = False
        while node.next.next and node.next.data == node.next.next.data:
            node.next.next = node.next.next.next
            dup = True
        if dup:
            node.next = node.next.next
        else:
            node = node.next

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "remove_duplicates_from_sorted_list.py",
            'remove_duplicates_from_sorted_list.tsv', remove_duplicates))
