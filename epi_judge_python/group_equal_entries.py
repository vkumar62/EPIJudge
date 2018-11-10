import collections
import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

Person = collections.namedtuple('Person', ('age', 'name'))

import pdb
def group_by_age(people):
    # TODO - you fill in here.
#    pdb.set_trace()
    MAX_AGE = 10000
    order = []
    age_count = [0] * MAX_AGE
    offsets = [-1] * MAX_AGE
    result = [None] * len(people)

    for person in people:
        if age_count[person.age] == 0:
            order.append(person.age)
        age_count[person.age] += 1

    offset = 0
    for age in order:
        offsets[age] = offset
        offset += age_count[age]

    for person in people:
        age = person.age
        result[offsets[age]] = person
        offsets[age] += 1

    people.clear()
    people.extend(result)
    return

# Using only one array extra space
def group_by_age(people):
    # TODO - you fill in here.
#    pdb.set_trace()
    MAX_AGE = 10000
    order = []
    age_count = [0] * MAX_AGE
    result = [None] * len(people)

    for person in people:
        if age_count[person.age] == 0:
            order.append(person.age)
        age_count[person.age] += 1

    for i in range(1, len(age_count)):
        age_count[i] += age_count[i-1] 

    for person in people:
        age = person.age
        result[age_count[age] - 1] = person
        age_count[age] -= 1

    people.clear()
    people.extend(result)
    return


@enable_executor_hook
def group_by_age_wrapper(executor, people):
    if not people:
        return
    people = [Person(*x) for x in people]
    values = collections.Counter()
    values.update(people)

    executor.run(functools.partial(group_by_age, people))

    if not people:
        raise TestFailure('Empty result')

    new_values = collections.Counter()
    new_values.update(people)
    if new_values != values:
        raise TestFailure('Entry set changed')

    ages = set()
    last_age = people[0]

    for x in people:
        if x.age in ages:
            pdb.set_trace()
            raise TestFailure('Entries are not grouped by age')
        if last_age != x.age:
            ages.add(last_age)
            last_age = x.age


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("group_equal_entries.py",
                                       'group_equal_entries.tsv',
                                       group_by_age_wrapper))
