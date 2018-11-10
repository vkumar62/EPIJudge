from test_framework import generic_test
from test_framework.test_failure import TestFailure


import pdb
class Queue:
    def __init__(self, capacity):
        # TODO - you fill in here.
        self.items = [None] * (capacity + 1)
        self.head = self.tail = 0
        self.debug = False
        return

    def full(self):
        return (self.tail + 1) % len(self.items) == self.head

    def empty(self):
        return self.tail == self.head

    def enqueue(self, x):
        # TODO - you fill in here.
        if self.debug:
            pdb.set_trace()
        if self.full():
            # resize
            if self.tail < self.head:
                new_items = self.items[self.head:] + self.items[:self.tail] + [None] * (len(self.items)+1)
            else:
                new_items = self.items[self.head:self.tail] + [None]*(len(self.items)+1)
            assert(len(new_items) == 2*len(self.items))
            self.head = 0
            self.tail = len(self.items)-1
            self.items = new_items
        self.items[self.tail] = x
        self.tail = (self.tail + 1) % len(self.items)
        return

    def dequeue(self):
        # TODO - you fill in here.
        if self.debug:
            pdb.set_trace()
        if self.empty():
            raise IndexError
        else:
            x = self.items[self.head]
            self.head = (self.head + 1) % len(self.items)
            return x 

    def size(self):
        # TODO - you fill in here.
        if self.tail >= self.head:
            sz = self.tail - self.head
        else:
            # Wrap around
            sz = len(self.items) - self.head + self.tail
        return sz

    def __repr__(self):
        return 'head %d tail %d len %d items %s' % (self.head, self.tail, len(self.items), str(self.items))

    def __str__(self):
        return self.__repr()


def queue_tester(ops):
    q = Queue(1)

    for (op, arg) in ops:
        if op == 'Queue':
            q = Queue(arg)
        elif op == 'enqueue':
            q.enqueue(arg)
        elif op == 'dequeue':
            result = q.dequeue()
            if result != arg:
                raise TestFailure(
                    "Dequeue: expected " + str(arg) + ", got " + str(result))
        elif op == 'size':
            result = q.size()
            if result != arg:
                raise TestFailure(
                    "Size: expected " + str(arg) + ", got " + str(result))
        else:
            raise RuntimeError("Unsupported queue operation: " + op)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("circular_queue.py",
                                       'circular_queue.tsv', queue_tester))
