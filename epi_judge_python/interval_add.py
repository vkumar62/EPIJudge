import collections
import functools

from test_framework import generic_test
from test_framework.test_failure import PropertyName
from test_framework.test_utils import enable_executor_hook

Interval = collections.namedtuple('Interval', ('left', 'right'))


def add_interval(disjoint_intervals, new_interval):
    # TODO - you fill in here.

    i = 0
    result_intervals = []

    while i < len(disjoint_intervals):
        interval = disjoint_intervals[i]
        if interval.right >= new_interval.left:
            break
        result_intervals.append(interval)
        i += 1

    # Discard all the intervals in disjoint_intervals which fall in this new interval
    while i < len(disjoint_intervals):
        interval = disjoint_intervals[i]
        if new_interval.right < interval.left:
            break
        new_interval = Interval(min(new_interval.left, interval.left),
                                max(new_interval.right, interval.right))
        i += 1

    result_intervals.append(new_interval)
    result_intervals.extend(disjoint_intervals[i:])
    return result_intervals


@enable_executor_hook
def add_interval_wrapper(executor, disjoint_intervals, new_interval):
    disjoint_intervals = [Interval(*x) for x in disjoint_intervals]
    return executor.run(
        functools.partial(add_interval, disjoint_intervals,
                          Interval(*new_interval)))


def res_printer(prop, value):
    def fmt(x):
        return [[e[0], e[1]] for e in x] if x else None

    if prop in (PropertyName.EXPECTED, PropertyName.RESULT):
        return fmt(value)
    else:
        return value


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "interval_add.py",
            'interval_add.tsv',
            add_interval_wrapper,
            res_printer=res_printer))
