""" Implement an algorithm to find the kth to last element of a singly linked list."""
from linked_list import LinkedList


def get_kth_last(l_list, k):
    if isinstance(l_list, LinkedList):
        fast_ptr = slow_ptr = l_list.head
        for _ in range(k):
            if fast_ptr is None:
                return "list size smaller than %d" % k
            fast_ptr = fast_ptr.next

        while fast_ptr is not None:
            fast_ptr = fast_ptr.next
            slow_ptr = slow_ptr.next

        return slow_ptr.data
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
    print(ll)
    print(get_kth_last(ll, 3))
