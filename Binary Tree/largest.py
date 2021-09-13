

class BinaryTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


# Largest of all in Tree
def findLargest(head):
    if head is None:
        return -1

    leftL = findLargest(head.left)
    rightL = findLargest(head.right)
    return max(leftL,rightL,head.data)



bt1 = BinaryTreeNode(1)
bt2 = BinaryTreeNode(2) 
bt3 = BinaryTreeNode(3)

bt1.left = bt2
bt1.right = bt3

bt4 = BinaryTreeNode(4)
bt5 = BinaryTreeNode(5)

bt2.left = bt4
bt2.right = bt5


print(findLargest(bt1))

