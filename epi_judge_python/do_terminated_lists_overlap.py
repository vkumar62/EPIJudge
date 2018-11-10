import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

import pdb
def overlapping_no_cycle_lists(l0, l1):
    # TODO - you fill in here.
    def listlen(L):
        c = 0
        while L:
            c += 1
            L = L.next
        return c

    len0, len1 = listlen(l0), listlen(l1)

    if len0 > len1:
        len1, len0 = len0, len1
        l1, l0 = l0, l1

    t0, t1 = l0, l1

    for _ in range(len1-len0):
        t1 = t1.next

    while t0 and t1 and t0 is not t1:
        t0, t1 = t0.next, t1.next

    return t0


@enable_executor_hook
def overlapping_no_cycle_lists_wrapper(executor, l0, l1, common):
    if common:
        if l0:
            i = l0
            while i.next:
                i = i.next
            i.next = common
        else:
            l0 = common

        if l1:
            i = l1
            while i.next:
                i = i.next
            i.next = common
        else:
            l1 = common

    result = executor.run(
        functools.partial(overlapping_no_cycle_lists, l0, l1))

    if result != common:
        raise TestFailure('Invalid result')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("do_terminated_lists_overlap.py",
                                       'do_terminated_lists_overlap.tsv',
                                       overlapping_no_cycle_lists_wrapper))
