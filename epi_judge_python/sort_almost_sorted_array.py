from test_framework import generic_test

import heapq


def sort_approximately_sorted_array(sequence, k):
    # TODO - you fill in here.
    min_heap = []
    result = []

    for n in sequence:
        heapq.heappush(min_heap, n)
        if len(min_heap) == k+1:
            result.append(heapq.heappop(min_heap))

    while min_heap:
        result.append(heapq.heappop(min_heap))
    return result


def sort_approximately_sorted_array_wrapper(sequence, k):
    return sort_approximately_sorted_array(iter(sequence), k)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "sort_almost_sorted_array.py", 'sort_almost_sorted_array.tsv',
            sort_approximately_sorted_array_wrapper))
