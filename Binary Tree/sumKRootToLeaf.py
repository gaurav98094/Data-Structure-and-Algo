'''
For a given Binary Tree of type integer and a number K, print out all root-to-leaf paths where the sum of all 
the node data along the path is equal to K.

Sample Input 1:
2 3 9 4 8 -1 2 4 -1 -1 -1 6 -1 -1 -1 -1 -1
13

Sample Output 1:
2 3 4 4 
2 3 8


Sample Input 2:
5 6 7 2 3 -1 1 -1 -1 -1 9 -1 -1 -1 -1
13

Sample Output 2:
5 6 2
5 7 1
'''



#Following is the structure used to represent the Binary Tree Node
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None



def rootToLeafPathsSumToK(root, k , string=""):
	#Your code goes here
    if root == None:
        return
    
    string= string+str(root.data)+" "
    rootToLeafPathsSumToK(root.left,k-root.data,string)
    rootToLeafPathsSumToK(root.right,k-root.data,string)
    
    if k==root.data and root.left==None and root.right==None:
        print(string)




