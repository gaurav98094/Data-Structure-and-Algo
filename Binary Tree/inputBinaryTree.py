
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


head = treeInput()
printT(head) 



