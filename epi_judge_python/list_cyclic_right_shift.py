from test_framework import generic_test


def cyclically_right_shift_list(L, k):
    # TODO - you fill in here.
    n = 0
    node = L
    while node:
        n += 1
        node = node.next

    if n == 0:
        return None
    k = k%n
    if k == 0:
        return L

    node = tail = L
    for _ in range(k):
        tail = tail.next

    while tail.next:
        node, tail = node.next, tail.next

    new_head = node.next
    node.next = None
    tail.next = L
    return new_head


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("list_cyclic_right_shift.py",
                                       'list_cyclic_right_shift.tsv',
                                       cyclically_right_shift_list))
