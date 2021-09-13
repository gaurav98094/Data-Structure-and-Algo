from sys import stdin, setrecursionlimit
import queue

setrecursionlimit(10 ** 6)


#Following is the structure used to represent the Binary Tree Node
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None



def printNodesWithoutSibling(root) :
	# Your code goes here
    if root is None:
        return None
    
    if root.left is None and root.right is None:
        pass
    elif root.left is not None and root.right is not None:
        printNodesWithoutSibling(root.left)
        printNodesWithoutSibling(root.right)
    elif root.left is None:
        print(root.right.data,end=" ")
        printNodesWithoutSibling(root.right)
    elif root.right is None:
        print(root.left.data,end=" ")
        printNodesWithoutSibling(root.left)

