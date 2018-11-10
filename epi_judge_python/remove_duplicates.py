import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

import pdb

class Name:
    def __init__(self, first_name, last_name):
        self.first_name, self.last_name = first_name, last_name

'''
    def __lt__(self, other):
        return (self.first_name < other.first_name
                if self.first_name != other.first_name else
                self.last_name < other.last_name)

    def __eq__(self, other):
        return self.first_name == other.first_name
'''


def eliminate_duplicate(A):
#    pdb.set_trace()
    A.sort(key=lambda k: (k.first_name, k.last_name))

    write_idx = 1
    for cand in A[1:]:
        if cand.first_name != A[write_idx - 1].first_name:
            A[write_idx] = cand
            write_idx += 1
    del A[write_idx:]
    return

@enable_executor_hook
def eliminate_duplicate_wrapper(executor, names):
    names = [Name(*x) for x in names]

    executor.run(functools.partial(eliminate_duplicate, names))

    return names


def comp(expected, result):
    return all([
        e == r.first_name for (e, r) in zip(sorted(expected), sorted(result, key=lambda k: (k.first_name, k.last_name)))
    ])


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("remove_duplicates.py",
                                       'remove_duplicates.tsv',
                                       eliminate_duplicate_wrapper, comp))
'''
eliminate_duplicate([Name("Foo", "1"), Name("ABC", "1"), Name("Foo", "1")])
'''
