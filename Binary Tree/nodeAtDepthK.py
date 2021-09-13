''''
For a given a Binary Tree of integers, replace each of its data with the depth of the tree.
Root is at depth 0, hence the root data is updated with 0. Replicate the same further going down 
the in the depth of the given tree.
The modified tree will be printed in the in-order fashion.

'''

def changeToDepthTree(root,d=0) :
	#Your code goes here
    if root==None:
        return 
    root.data = d
    changeToDepthTree(root.left,d+1)
    changeToDepthTree(root.right,d+1)
    
    return root
    