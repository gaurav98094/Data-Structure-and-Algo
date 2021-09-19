class GenericTreeNode:
    def __init__(self,data):
        self.data = data
        self.children = list()


def takeTreeInput():
    rootData = int(input("Enter Root Data : "))

    if rootData==-1:
        return
    
    root = GenericTreeNode(rootData)
    
    childCount = int(input("Enter no of child for "+str(root.data)+" : "))
    for i in range(childCount):
        child = takeTreeInput()
        root.children.append(child)
    return root

def printTreeBetter(root):
    if root is None:
        return

    print(root.data,end=" : ")
    for child in root.children:
        print(child.data,end=',')
    print()
    for child in root.children:
        printTreeBetter(child)



root = takeTreeInput()
printTreeBetter(root)
