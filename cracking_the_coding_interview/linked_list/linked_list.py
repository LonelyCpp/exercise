class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        ll_str = ''
        current = self.head
        while current is not None:
            ll_str += str(current.data) + '->'
            current = current.next
        ll_str += 'None'
        return ll_str

    def push(self, data):
        cur = self.head
        node = Node(data)
        if cur is None:
            self.head = node
            return
        while cur.next != None:
            cur = cur.next
        cur.next = node
