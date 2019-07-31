"""
The lowest common ancestor (LCA) for 2 nodes, 
N1 and N2, is defined as the the lowest node 
in the tree, where N1 and N2 are both its 
decendants.

Write a function that returns the LCA of 2 
given nodes in a tree.

The nodes' values are guaranteed to be 
non-duplicates.
https://codebasil.com/problems/5bbe51ef99be167d5e6756b3
"""


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)


def findLowestCommonAncestor(root, first, second):
    if root is None:
        return root
    if root.val in [first, second]:
        return root

    left = findLowestCommonAncestor(root.left, first, second)
    right = findLowestCommonAncestor(root.right, first, second)

    if left is None:
        return right
    elif right is None:
        return left

    return root


root = Node(1,
            Node(2,
                 Node(4),
                 Node(5,
                      None,
                      Node(9)
                      )
                 ),
            Node(3,
                 None,
                 Node(6))
            )
print(findLowestCommonAncestor(root, 4, 9))

root = Node(1)
print(findLowestCommonAncestor(root, 1, 1))
