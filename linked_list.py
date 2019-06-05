class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        node = Node(data)
        if(self.head is None):
            self.head = node
            return

        current = self.head
        while current.next is not None:
            current = current.next
        current.next = node

    def __str__(self):
        ll_str = ''
        current = self.head
        while current is not None:
            ll_str += str(current.data) + '->'
            current = current.next
        ll_str += 'None'
        return ll_str


if __name__ == '__main__':
    ll = LinkedList()
    ll.push(1)
    ll.push(2)
    ll.push(3)
    print(ll)
