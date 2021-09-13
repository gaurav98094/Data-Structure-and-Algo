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
    elif head.left is None:
        print(head.data," : ",head.left.data," , None")
    else:
        print(head.data," : ",head.left.data," , ",head.right.data)

    
    printT(head.left)
    printT(head.right)


bt1 = BinaryTreeNode(1)
bt2 = BinaryTreeNode(2) 
bt3 = BinaryTreeNode(3)

bt1.left = bt2
bt1.right = bt3

bt4 = BinaryTreeNode(4)
bt5 = BinaryTreeNode(5)

bt2.left = bt4
bt2.right = bt5

printT(bt1)