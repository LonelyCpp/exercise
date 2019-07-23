"""
Implement an algorithm to delete a node in the middle
(i.e., any node but the first and last node, not
necessarily the exact middle)
"""
from linked_list import LinkedList


def delete_mid(l_list):
    if isinstance(l_list, LinkedList):
        fast_ptr = l_list.head
        slow_ptr = l_list.head

        while fast_ptr is not None:
            try:
                fast_ptr = fast_ptr.next
                fast_ptr = fast_ptr.next
            except AttributeError:
                break
            slow_ptr = slow_ptr.next

        print(slow_ptr.data)
    else:
        raise Exception("param not of type 'LinkedList'")


if __name__ == '__main__':
    ll = LinkedList()
    ll.push(1)
    ll.push(2)
    ll.push(3)
    ll.push(4)
    ll.push(5)
    ll.push(6)
    ll.push(7)
    print(ll)
    delete_mid(ll)
    print(ll)
