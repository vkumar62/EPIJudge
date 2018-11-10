from test_framework import generic_test
from test_framework.test_failure import TestFailure


import pdb
class Stack:
    def __init__(self):
        self.stack = []
        self.max_element_stack = []
        self.debug = False

    def empty(self):
        # TODO - you fill in here.
        return len(self.stack) == 0

    def max(self):
        if self.debug:
            pdb.set_trace()
        # TODO - you fill in here.
        if self.max_element_stack:
            return self.max_element_stack[-1][0]
        return float('-inf')

    def pop(self):
        # TODO - you fill in here.
        if self.debug:
            pdb.set_trace()
        item = self.stack.pop()
        if item == self.max():
            m, c = self.max_element_stack[-1]
            c -= 1
            if c == 0:
                self.max_element_stack.pop()
            else:
                self.max_element_stack[-1] = (m, c)
        return item

    def push(self, x):
        if self.debug:
            pdb.set_trace()
        # TODO - you fill in here.
        self.stack.append(x)
        if x > self.max():
            self.max_element_stack.append((x, 1))
        elif x == self.max():
            m, c = self.max_element_stack[-1]
            c += 1
            self.max_element_stack[-1] = (m, c)
        return


def stack_tester(ops):
    try:
        s = Stack()

        for (op, arg) in ops:
            if op == 'Stack':
                s = Stack()
            elif op == 'push':
                s.push(arg)
            elif op == 'pop':
                result = s.pop()
                if result != arg:
                    raise TestFailure(
                        "Pop: expected " + str(arg) + ", got " + str(result))
            elif op == 'max':
                result = s.max()
                if result != arg:
                    raise TestFailure(
                        "Max: expected " + str(arg) + ", got " + str(result))
            elif op == 'empty':
                result = int(s.empty())
                if result != arg:
                    raise TestFailure(
                        "Empty: expected " + str(arg) + ", got " + str(result))
            else:
                raise RuntimeError("Unsupported stack operation: " + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("stack_with_max.py",
                                       'stack_with_max.tsv', stack_tester))
