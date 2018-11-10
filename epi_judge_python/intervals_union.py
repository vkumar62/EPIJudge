import collections
import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Endpoint = collections.namedtuple('Endpoint', ('is_closed', 'val'))

Interval = collections.namedtuple('Interval', ('left', 'right'))


# is_closed means interval includes the endpoint value. So closed_left < open_left and open_right < closed_right
def union_of_intervals(intervals):
    # TODO - you fill in here.
    intervals.sort(key = lambda k: (k.left.val, not k.left.is_closed))

    result = [intervals[0]]

    for interval in intervals[1:]:
        if interval.left.val < result[-1].right.val or \
           (interval.left.val == result[-1].right.val and \
                   (interval.left.is_closed or result[-1].right.is_closed)):
            '''
            result[-1] = Interval(Endpoint(interval.left.is_closed or result[-1].left.is_closed,
                                           min(interval.left.val, result[-1].left.val)),
                                  Endpoint(interval.right.is_closed or result[-1].right.is_closed,
                                           max(interval.right.val, result[-1].right.val)))
            '''
            if (interval.right.val > result[-1].right.val or \
                    (interval.right.val == result[-1].right.val and interval.right.is_closed)):
                result[-1] = Interval(result[-1].left, interval.right)

        else:
            result.append(interval)

    return result


@enable_executor_hook
def union_of_intervals_wrapper(executor, intervals):
    intervals = [
        Interval(Endpoint(x[1], x[0]), Endpoint(x[3], x[2])) for x in intervals
    ]

    result = executor.run(functools.partial(union_of_intervals, intervals))

    return [(i.left.val, i.left.is_closed, i.right.val, i.right.is_closed)
            for i in result]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("intervals_union.py",
                                       "intervals_union.tsv",
                                       union_of_intervals_wrapper))
