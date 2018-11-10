import collections
import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

# Event is a tuple (start_time, end_time)
Event = collections.namedtuple('Event', ('start', 'finish'))

import pdb
def find_max_simultaneous_events(A):
    # TODO - you fill in here.

#    E = [p for event in A for p in ((event.start, True), (event.finish, False))]
    E = [p for event in A for p in ((event.start, True), (event.finish, False))]

    E.sort(key = lambda k: (k[0], not k[1]))

    cur_events = 0
    max_events = 0

    for p in E:
        if p[1] == True:
            cur_events += 1
        else:
            max_events = max(cur_events, max_events)
            cur_events -= 1
    max_events = max(cur_events, max_events)
    return max_events
    '''
    A.sort(key=lambda k: k.finish)

    max_events = 0
    cur_events = 0
    cur_finish_idx = 0
    cur_idx = 0

    while cur_idx < len(A) and cur_finish_idx < len(A):
        if A[cur_idx].start < A[cur_finish_idx].finish:
            cur_events += 1
            max_events = max(cur_events, max_events)
            cur_idx += 1
        else:
            cur_finish_idx += 1
            cur_events = 0

    if cur_idx < len(A):
        cur_events += len(A) - cur_idx - 1
        max_events = max(cur_events, max_events)

    return max_events 
    '''

def find_max_simultaneous_events(A):
    starts = sorted(A, key=lambda k: k.start)
    finishes = sorted(A, key=lambda k: k.finish)

    max_events = 0
    cur_events = 0

    start_idx, finish_idx = 0, 0

    while start_idx < len(A) and finish_idx < len(A):
        if starts[start_idx].start <= finishes[finish_idx].finish:
            cur_events += 1
            start_idx += 1
        else:
            max_events = max(max_events, cur_events)
            cur_events -= 1
            finish_idx += 1

    
    max_events = max(max_events, cur_events)
    return max_events





@enable_executor_hook
def find_max_simultaneous_events_wrapper(executor, events):
    events = [Event(*x) for x in events]
    return executor.run(
        functools.partial(find_max_simultaneous_events, events))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("calendar_rendering.py",
                                       'calendar_rendering.tsv',
                                       find_max_simultaneous_events_wrapper))
