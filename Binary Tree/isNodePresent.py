'''
For a given Binary Tree of type integer and a number X, find whether a node exists in the tree with data X or not.
'''


class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def isNodePresent(root, x):
    # Write your code here.
    if root is None:
        return False
    
    if root.data==x:
        return True
    
    lc = isNodePresent(root.left,x)
    rc = isNodePresent(root.right,x)
    return lc or rc




