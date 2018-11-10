from test_framework import generic_test

import heapq
import pdb

def online_median(sequence):
    # TODO - you fill in here.
#    pdb.set_trace()
    min_heap = []
    max_heap = []
    medians = []

    for s in sequence:
        heapq.heappush(max_heap, -heapq.heappushpop(min_heap, s))
        if len(max_heap) > len(min_heap):
            heapq.heappush(min_heap, -heapq.heappop(max_heap))

        if len(max_heap) == len(min_heap):
            median = (min_heap[0] + -max_heap[0])/2
        else:
            median = min_heap[0]
        medians.append(median)
    return medians


def online_median_wrapper(sequence):
    return online_median(iter(sequence))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("online_median.py", "online_median.tsv",
                                       online_median_wrapper))
