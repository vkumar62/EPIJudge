from test_framework import generic_test


class Queue:
    def __init__(self):
        self.enq_stack = []
        self.deq_stack = []

    def enqueue(self, x):
        # TODO - you fill in here.
        self.enq_stack.append(x)
        return

    def dequeue(self):
        # TODO - you fill in here.
        if not self.deq_stack:
            while self.enq_stack:
                self.deq_stack.append(self.enq_stack.pop())
        if not self.deq_stack:
            raise IndexError
        return self.deq_stack.pop()


def queue_tester(ops):
    from test_framework.test_failure import TestFailure

    try:
        q = Queue()

        for (op, arg) in ops:
            if op == 'Queue':
                q = Queue()
            elif op == 'enqueue':
                q.enqueue(arg)
            elif op == 'dequeue':
                result = q.dequeue()
                if result != arg:
                    raise TestFailure("Dequeue: expected " + str(arg) +
                                      ", got " + str(result))
            else:
                raise RuntimeError("Unsupported queue operation: " + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("queue_from_stacks.py",
                                       'queue_from_stacks.tsv', queue_tester))
