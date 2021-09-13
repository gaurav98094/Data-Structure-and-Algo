#Following the structure used for Binary Tree
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None




def getSum(root):
	#Your code goes here
    if root is None:
        return 0
    
    return getSum(root.left)+getSum(root.right)+root.data




