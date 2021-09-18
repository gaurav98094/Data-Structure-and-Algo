'''
Given a BST and an integer k. Find and return the path from the node with data k and root 
(if a node with data k is present in given BST) in a list. Return empty list otherwise.
Note: Assume that BST contains all unique elements.
'''


def findPathBST(root,data,string=[]):
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    if root==None:
        return 
    
    if root.data== data:
        string.insert(0,data)
        return string

    string.insert(0,root.data)
    
    if root.data<data:
        return findPathBST(root.right,data,string)
    else:
        return findPathBST(root.left,data,string)
    