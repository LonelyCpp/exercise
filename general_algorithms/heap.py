class PriorityQueue:
    def __init__(self):
        self.__heap = [None, ]

    def insert(self, val):
        self.__heap.append(val)
        self.__heapify_up(len(self.__heap) - 1)

    @staticmethod
    def __get_parent_index(child_index):
        if child_index <= 1:
            return -1
        return child_index // 2

    @staticmethod
    def __get_first_child_index(parent_index):
        return parent_index * 2

    def __heapify_up(self, current_index):
        parent_index = self.__get_parent_index(current_index)

        if parent_index is -1:
            return

        if self.__heap[parent_index] > self.__heap[current_index]:
            self.__heap[parent_index], self.__heap[current_index] = \
                self.__heap[current_index], self.__heap[parent_index]
            self.__heapify_up(parent_index)

    def __heapify_down(self, current_index):
        min_index = current_index

        first_child_index = self.__get_first_child_index(current_index)
        second_child_index = first_child_index + 1

        for child_index in [first_child_index, second_child_index]:
            if child_index < len(self.__heap):
                if self.__heap[child_index] < self.__heap[min_index]:
                    min_index = child_index

        if min_index != current_index:
            self.__heap[current_index], self.__heap[min_index] = \
                self.__heap[min_index], self.__heap[current_index]
            self.__heapify_down(min_index)

    def peak(self):
        """returns the first element in the queue"""
        if len(self.__heap) <= 1:
            return None
        return self.__heap[1]

    def dequeue(self):
        if len(self.__heap) <= 1:
            return None
        if len(self.__heap) == 2:
            return self.__heap.pop()

        first_element = self.__heap[1]
        self.__heap[1] = self.__heap.pop()
        self.__heapify_down(1)
        return first_element

    def __str__(self):
        return str(self.__heap)


if __name__ == "__main__":
    pq = PriorityQueue()
    pq.insert(4)
    pq.insert(3)
    pq.insert(1)
    pq.insert(2)
    pq.insert(-1)
    print(pq.dequeue())
    print(pq.dequeue())
    print(pq.dequeue())
    print(pq.dequeue())
