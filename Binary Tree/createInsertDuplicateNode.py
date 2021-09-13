'''
For a given a Binary Tree of type integer, duplicate every node of the tree and attach it
 to the left of itself.
The root will remain the same. So you just need to insert nodes in the given Binary Tree.


Sample Input 1:
10 20 30 40 50 -1 60 -1 -1 -1 -1 -1 -1

Sample Output 1: (Level Wise Traversal)
10 
10 30 
20 30 60 
20 50 60 
40 50 
40 


'''

#Following is the structure used to represent the Binary Tree Node
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Method to insert duplicate Node
def insertDuplicateNode(root):
    if root==None:
        return None
    
    rd = root.data
    newNode = BinaryTreeNode(rd)
    newNode.left = root.left
    root.left = newNode
    
    insertDuplicateNode(root.left.left)
    insertDuplicateNode(root.right)
    return root

