from test_framework import generic_test
import sys


import pdb
def find_closest_elements_in_sorted_arrays(sorted_arrays):
    # TODO - you fill in here.
    pdb.set_trace()

    min_diff = float('inf')
    chosen_set = []

    idx = [0] * len(sorted_arrays)

    while True:
        vals = list(s[idx[x]] for x, s in enumerate(sorted_arrays))
        min_val, max_val = min(vals), max(vals)

        #min_diff = min(max_val-min_val, min_diff)
        if min_diff > max_val-min_val:
            min_diff = max_val-min_val
            chosen_set = vals

        min_idx = 0
        for val in vals:
            if min_val == val:
                break
            min_idx += 1

        idx[min_idx] += 1
        if idx[min_idx] == len(sorted_arrays[min_idx]):
            break

    print(chosen_set)
    return min_diff


# Pythonic using sortedcontainers - DOES NOT WORK because iters[] may have duplicate
# values. So idx has to be part of the key
from sortedcontainers import SortedDict
def find_closest_elements_in_sorted_arrays(sorted_arrays):
    # TODO - you fill in here.

    min_diff = float('inf')

    chosen_set = []
    iters = SortedDict()

    for idx, s in enumerate(sorted_arrays):
        it = iter(s)
        first_min = next(it, None)
        assert first_min is not None, pdb.set_trace()
        if first_min is not None:
            iters[first_min] = (idx, it)

    while True:
        max_val = iters.keys()[-1]
        min_val, (min_idx, it) = iters.peekitem(0)

        if min_diff > max_val-min_val:
            min_diff = max_val-min_val
            chosen_set = sorted(list((v, i) for v, (i, _) in iters.items()), key=lambda x: x[1])
        iters.popitem(0)
        next_min = next(it, None)
        if next_min == None:
            print(chosen_set)
            return min_diff
        iters[next_min] = (min_idx, it)
        assert len(iters) == len(sorted_arrays), pdb.set_trace()

from sortedcontainers import SortedDict
def find_closest_elements_in_sorted_arrays(sorted_arrays):
    # TODO - you fill in here.

    min_diff = float('inf')

    iters = SortedDict()
    chosen_set = None

    for idx, s in enumerate(sorted_arrays):
        it = iter(s)
        first_min = next(it, None)
        if first_min is not None:
            iters[(first_min, idx)] = it

    while True:
        max_val = iters.keys()[-1][0]
        min_val, min_idx = iters.keys()[0]
        
        if min_diff > max_val-min_val:
            min_diff = max_val-min_val
            chosen_set = sorted(list(iters.keys()), key=lambda x: x[1])
        it = iters.popitem(0)[1]

        next_min = next(it, None)
        if next_min == None:
            print(chosen_set)
            return min_diff
        iters[(next_min, min_idx)] = it
        assert len(iters) == len(sorted_arrays), pdb.set_trace()


from sortedcontainers import SortedList
def find_closest_elements_in_sorted_arrays(sorted_arrays):
    nums = sorted_arrays
    tree = SortedList()
    for i in range(len(nums)):
        tree.add((nums[i][0], i, 0))

    min_val = float('-inf')
    max_val = float('inf') 
    while True:
        min, mini, i = tree[0]
        max, _, _ = tree[-1]
        if max_val - min_val > max-min:
            min_val = min
            max_val = max
        tree.pop(0)
        if i+1 < len(nums[mini]):
            tree.add((nums[mini][i+1], mini, i+1))
        else:
            break
    return max_val - min_val
















































if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("minimum_distance_3_sorted_arrays.py",
                                       'minimum_distance_3_sorted_arrays.tsv',
                                       find_closest_elements_in_sorted_arrays))
