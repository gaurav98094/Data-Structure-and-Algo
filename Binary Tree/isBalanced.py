'''
Check if the BT is balanced or not

The root is said to be balanced if the left and right subtree donot have the height difference greater than 1
'''

from heightOfTree import height

class BinaryTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


#Print The Tree
def printT(head):
    if head is None:
        return 
    
    if head.left is None and head.right is None:
        print(head.data," : None")
    elif head.left is None:
        print(head.data," : None , ",head.right.data)
    elif head.right is None:
        print(head.data," : ",head.left.data," , None")
    else:
        print(head.data," : ",head.left.data," , ",head.right.data)    
    printT(head.left)
    printT(head.right)


def treeInput():
    rootD = int(input())
    if rootD==-1:
        return None

    root = BinaryTreeNode(rootD)
    leftT = treeInput()
    rightT = treeInput()
    root.left = leftT
    root.right = rightT

    return root



# Function to ckeck if the root is balanced or not
def isBalanced(root):
    if root is None:
        return True

    lh = height(root.left)
    rh = height(root.right)

    if abs(rh-lh)>1:
        return False

    isLeftBalanced = isBalanced(root.left)
    isRightBalanced = isBalanced(root.right)

    if isLeftBalanced and isRightBalanced:
        return True
    else:
        return False


def isBalancedOpti(root):
    if root is None:
        return 0,True

    lh,isLeftBalanced = isBalancedOpti(root.left)
    rh,RightBalanced = isBalancedOpti(root.right)

    h = 1 + max(lh,rh)

    if abs(lh-rh)>1:
        return h,False
    
    if isLeftBalanced and RightBalanced:
        return h,True
    else:
        return h,False


head = treeInput()
printT(head) 
print("\n\nHEIGHT OF TREE : ",height(head))
print("\n iS BALANCED : ",isBalanced(head))





