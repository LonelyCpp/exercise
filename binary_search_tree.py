class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

    def __str__(self):
        return str(self.data)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        newNode = Node(data)
        if self.root is None:
            self.root = newNode
            return

        currentNode = self.root
        endReached = False
        while endReached is False:
            if currentNode.data > newNode.data:
                if currentNode.left is None:
                    currentNode.left = newNode
                    endReached = True
                else:
                    currentNode = currentNode.left
            else:
                if currentNode.right is None:
                    currentNode.right = newNode
                    endReached = True
                else:
                    currentNode = currentNode.right

    @staticmethod
    def inOrder(node):
        if node is None:
            return
        BinarySearchTree.inOrder(node.left)
        print(node)
        BinarySearchTree.inOrder(node.right)


if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.insert(2)
    bst.insert(1)
    bst.insert(3)
    BinarySearchTree.inOrder(bst.root)
