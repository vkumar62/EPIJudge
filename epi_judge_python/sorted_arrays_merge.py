from test_framework import generic_test
import heapq


import pdb
#Time = O(nlogk) n is total elements, k is number of arrays
def merge_sorted_arrays(sorted_arrays):
    # TODO - you fill in here.
    #pdb.set_trace()
    sorted_iterators = [iter(a) for a in sorted_arrays]
    heap = []
    for i, it in enumerate(sorted_iterators):
        first = next(it, None)
        if first is not None:
            heapq.heappush(heap, (first, i))

    result = []
    while heap:
        x, i = heapq.heappop(heap)
        result.append(x)
        it = sorted_iterators[i]
        x = next(it, None)
        if x is not None:
            heapq.heappush(heap, (x, i))
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sorted_arrays_merge.py",
                                       "sorted_arrays_merge.tsv",
                                       merge_sorted_arrays))
