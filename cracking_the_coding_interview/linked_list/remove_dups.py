"""
Write code to remove duplicates from an unsorted linked list.
"""
from linked_list import LinkedList


def remove_dup(l_list):
    seen = set()
    if isinstance(l_list, LinkedList):
        prev = None
        cur = l_list.head
        while cur is not None:
            if cur.data in seen:
                prev.next = cur.next
            else:
                prev = cur
            seen.add(cur.data)
            cur = cur.next
    else:
        raise Exception("param not of type 'LinkedList'")


if __name__ == '__main__':
    ll = LinkedList()
    ll.push(1)
    ll.push(1)
    ll.push(2)
    ll.push(2)
    ll.push(3)
    ll.push(1)
    print(ll)
    remove_dup(ll)
    print(ll)
