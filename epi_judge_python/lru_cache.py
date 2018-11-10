from test_framework import generic_test
from test_framework.test_failure import TestFailure

class QueueNode:
    def __init__(self, data):
        self.prev = self.next = None
        self.data = data

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, node):
        if self.tail is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

    def remove(self, node):
        if not self.head:
            assert 0

        if node is self.head and node is self.tail:
            self.head = self.tail = None
        elif node is self.head:
            self.head = self.head.next
            self.head.prev = None
        elif node is self.tail:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            node.next.prev = node.prev
            node.prev.next = node.next

class LruCache:
    def __init__(self, capacity):
        # TODO - you fill in here.
        self.lru_queue = Queue()
        self.lru_table = dict()
        self.capacity = capacity
        return

    def lookup(self, isbn):
        # TODO - you fill in here.

        if isbn not in self.lru_table:
            return -1
        price, queue_node = self.lru_table[isbn]
        self.lru_queue.remove(queue_node)
        new_queue_node = QueueNode(isbn)
        self.lru_table[isbn] = (price, new_queue_node)
        self.lru_queue.append(new_queue_node)
        return price

    def insert(self, isbn, price):
        # TODO - you fill in here.
        if isbn not in self.lru_table:
            if len(self.lru_table) == self.capacity:
                # Pop the least recently used
                queue_node_to_pop = self.lru_queue.head
                self.lru_queue.remove(queue_node_to_pop)
                popped_isbn = queue_node_to_pop.data
                del self.lru_table[popped_isbn]
        else:
            price, queue_node = self.lru_table[isbn]
            self.lru_queue.remove(queue_node)

        # Add to the isbn table
        new_queue_node = QueueNode(isbn)
        self.lru_table[isbn] = (price, new_queue_node)
        self.lru_queue.append(new_queue_node)

    def erase(self, isbn):
        # TODO - you fill in here.
        if isbn not in self.lru_table:
            return False

        price, queue_node = self.lru_table[isbn]
        self.lru_queue.remove(queue_node)
        del self.lru_table[isbn]
        return True


def run_test(commands):
    if len(commands) < 1 or commands[0][0] != 'LruCache':
        raise RuntimeError('Expected LruCache as first command')

    cache = LruCache(commands[0][1])

    for cmd in commands[1:]:
        if cmd[0] == 'lookup':
            result = cache.lookup(cmd[1])
            if result != cmd[2]:
                raise TestFailure(
                    'Lookup: expected ' + str(cmd[2]) + ', got ' + str(result))
        elif cmd[0] == 'insert':
            cache.insert(cmd[1], cmd[2])
        elif cmd[0] == 'erase':
            result = 1 if cache.erase(cmd[1]) else 0
            if result != cmd[2]:
                raise TestFailure(
                    'Erase: expected ' + str(cmd[2]) + ', got ' + str(result))
        else:
            raise RuntimeError('Unexpected command ' + cmd[0])


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("lru_cache.py", 'lru_cache.tsv',
                                       run_test))
