import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

from list_node import ListNode


def list_pivoting(l, x):
    # TODO - you fill in here.
    pre_pivot_head, pivot_head, post_pivot_head = ListNode(0), ListNode(0), ListNode(0)
    pre_pivot, pivot, post_pivot = pre_pivot_head, pivot_head, post_pivot_head

    node = l

    while node:
        if node.data == x:
            pivot.next = node
            pivot = pivot.next
        elif node.data < x:
            pre_pivot.next = node
            pre_pivot = pre_pivot.next
        else:
            post_pivot.next = node
            post_pivot = post_pivot.next
        node = node.next

    post_pivot.next = None
    pivot.next = post_pivot_head.next
    pre_pivot.next = pivot_head.next
    return pre_pivot_head.next


def linked_to_list(l):
    v = list()
    while l is not None:
        v.append(l.data)
        l = l.next
    return v


@enable_executor_hook
def list_pivoting_wrapper(executor, l, x):
    original = linked_to_list(l)

    l = executor.run(functools.partial(list_pivoting, l, x))

    pivoted = linked_to_list(l)
    mode = -1
    for i in pivoted:
        if mode == -1:
            if i == x:
                mode = 0
            elif i > x:
                mode = 1
        elif mode == 0:
            if i < x:
                raise TestFailure('List is not pivoted')
            elif i > x:
                mode = 1
        else:
            if i <= x:
                raise TestFailure('List is not pivoted')

    if sorted(original) != sorted(pivoted):
        raise TestFailure('Result list contains different values')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("pivot_list.py", 'pivot_list.tsv',
                                       list_pivoting_wrapper))
