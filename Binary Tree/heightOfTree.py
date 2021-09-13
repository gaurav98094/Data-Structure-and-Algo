#Following is the structure used to represent the Binary Tree Node
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

#Find the Height of tree
def height(root) :
	#Your code goes here
    if root is None:
        return 0
    
    lh = 1 + height(root.left)
    rh = 1 + height(root.right)
    
    return max(lh,rh)


bt1 = BinaryTreeNode(1)
bt2 = BinaryTreeNode(2) 
bt3 = BinaryTreeNode(3)

bt1.left = bt2
bt1.right = bt3

bt4 = BinaryTreeNode(4)
bt5 = BinaryTreeNode(5)

bt2.left = bt4
bt2.right = bt5


print(height(bt1))
