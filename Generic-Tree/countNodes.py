'''Count the number of Node'''


def numNodes(root):
    if root==None:
        return 0
        
    count=1
    for child in root.children:
        count = count + numNodes(child)
    return count