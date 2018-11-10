from test_framework import generic_test
from test_framework.test_failure import TestFailure

from collections import deque

class QueueWithMax:
    class MaxElement:
        def __init__(self, val, count=1):
            self.val = val
            self.count = count

    def __init__(self):
        self.q = deque()
        self.max_q = deque()

    def enqueue(self, x):
        # TODO - you fill in here.
        self.q.append(x)

        if not self.max_q:
            self.max_q.append(self.MaxElement(x))
        else:
            if self.max_q[-1].val == x:
                self.max_q[-1].count += 1
            elif self.max_q[-1].val > x:
                self.max_q.append(self.MaxElement(x))
            else:
                while self.max_q and self.max_q[-1].val < x:
                    self.max_q.pop()
                self.max_q.append(self.MaxElement(x))
        return

    def dequeue(self):
        # TODO - you fill in here.
        if not self.q:
            raise IndexError
        x = self.q.popleft()

        if x == self.max_q[0].val:
            self.max_q[0].count -= 1
            if self.max_q[0].count == 0:
                self.max_q.popleft()
        return x

    def max(self):
        # TODO - you fill in here.
        if not self.max_q:
            raise IndexError
        return self.max_q[0].val


def queue_tester(ops):

    try:
        q = QueueWithMax()

        for (op, arg) in ops:
            if op == 'QueueWithMax':
                q = QueueWithMax()
            elif op == 'enqueue':
                q.enqueue(arg)
            elif op == 'dequeue':
                result = q.dequeue()
                if result != arg:
                    raise TestFailure("Dequeue: expected " + str(arg) +
                                      ", got " + str(result))
            elif op == 'max':
                result = q.max()
                if result != arg:
                    raise TestFailure(
                        "Max: expected " + str(arg) + ", got " + str(result))
            else:
                raise RuntimeError("Unsupported queue operation: " + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("queue_with_max.py",
                                       'queue_with_max.tsv', queue_tester))
