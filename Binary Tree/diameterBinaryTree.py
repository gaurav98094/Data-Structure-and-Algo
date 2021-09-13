'''
The diameter of a tree can be defined as the maximum distance between any two nodes.
Here, the distance is measured in terms of the total number of nodes present along the path 
of the two leaf nodes, including both the leaves
'''



def diameterOfBinaryTreeHelper(root) :
    if root is None:
        return 0,0
    
    lh,ld = diameterOfBinaryTreeHelper(root.left)
    rh,rd = diameterOfBinaryTreeHelper(root.right)
    
    h = 1+ max(lh,rh)
    
    d = max(ld,rd,lh+rh+1)
    
    return h,d

def diameterOfBinaryTree(root):
    _,d=diameterOfBinaryTreeHelper(root)
    return d


