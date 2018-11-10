class DListNode:
    def __init__(self, val=None):
        self.val = val
        self.next = None
        self.prev = None


class DList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, val):
        newnode = DListNode(val)

        if not self.tail:
            self.tail = self.head = newnode
            return

        self.tail.next = newnode
        newnode.prev = self.tail
        self.tail = newnode

    def prepend(self, val):
        newnode = DListNode(val)

        if not self.head:
            self.tail = self.head = newnode
            return

        newnode.next = self.head
        self.head.prev = newnode
        self.head = newnode

    def pop(self, index = 0):
        cur = self.head
        i = 0

        while i < index and cur:
            cur = cur.next

        if i != index or cur is None:
            raise IndexError

        if cur.prev:
            cur.prev.next = cur.next

        if cur.next:
            cur.next.prev = cur.prev

        if cur == self.head:
            self.head = cur.next
        if cur == self.tail:
            self.tail = cur.prev

    def __repr__(self):
        cur = self.head
        s = []
        while cur:
            s.append(cur.val)
            cur = cur.next
        return ' '.join(map(str,s))

class SListNode:
    def __init__(self, val=None):
        self.val = val
        self.next = None


class SList:
    def __init__(self):
        self.head = None

    def append(self, val):
        newnode = SListNode(val)

        if not self.head:
            self.head = newnode
            return
        
        tail = self.head
        while tail.next != None:
            tail = tail.next
        tail.next = newnode

    def prepend(self, val):
        newnode = SListNode(val)
        newnode.next = self.head
        self.head = newnode

    def pop(self, index = 0):
        dummy = SListNode()
        dummy.next = self.head
        cur = dummy
        i = 0

        while i < index and cur.next:
            cur = cur.next
            i += 1

        if i != index:
            raise IndexError

        cur.next = cur.next.next
        self.head = dummy.next

    def __repr__(self):
        cur = self.head
        s = []
        while cur:
            s.append(cur.val)
            cur = cur.next
        return ' '.join(map(str,s))

l = SList()

for x in range(10):
    l.append(x)

print(l)

for x in range(10):
    l.prepend(x)

print(l)

l.pop()

print(l)
l.pop(2)
print(l)
