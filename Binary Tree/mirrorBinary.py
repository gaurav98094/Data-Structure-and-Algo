'''
For a given Binary Tree of type integer, update it with its corresponding mirror image.

Sample Input 1:
1 2 3 4 5 6 7 -1 -1 -1 -1 -1 -1 -1 -1

Sample Output 1:
1 
3 2 
7 6 5 4


Sample Input 2:
5 10 6 2 3 -1 -1 -1 -1 -1 9 -1 -1

Sample Output 2:
5 
6 10 
3 2 
9



'''


def mirrorBinaryTree(root) :
    # Your code goes here
    if root is None:
        return root
    
    tmp = root.left
    root.left = root.right
    root.right = tmp
    
    mirrorBinaryTree(root.left)
    mirrorBinaryTree(root.right)
    return root
