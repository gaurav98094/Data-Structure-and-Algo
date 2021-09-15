'''
Check if the given tree is BST or not.
'''



# MEthod 1 :    o(n log(n)) ---> Balanced Tree    or   O(n^2) ---> Skewed Tree
def minTree(root):
    if root is None:
        return 10000000
    
    leftMin = minTree(root.left)
    rightMin = minTree(root.right)
    return min(root.data,leftMin,rightMin)

def maxTree(root):
    if root is None:
        return -1000000

    leftMax = maxTree(root.left)
    rightMax = maxTree(root.right)
    return max(root.data,leftMax,rightMax)

def isBST(root):
    if root is None:
        return True

    maxi = maxTree(root.left)
    mini = minTree(root.right)

    if root.data > mini or root.data <= maxi:
        return False
    
    isLeftBST = isBST(root.left)
    isRightBST = isBST(root.right)

    return isLeftBST and isRightBST

# Method 2 : Setting the constraints
def isBSTimproved(root,min_Range=-1111111,max_Range = 111111111):
    if root is None:
        return


    if root.data <min_Range or root.data>max_Range:
        return False

    isLeftWithinCons = isBSTimproved(root.left,min_Range,root.data-1)
    isRightWithinCons = isBSTimproved(root.roght,root.data,max_Range)

    return isLeftWithinCons and isLeftWithinCons
    


    