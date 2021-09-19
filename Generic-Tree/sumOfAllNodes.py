sum = 0

# Function
def sumOfAllNodes(root) :
    if root is None:
        return 0
    
    global sum
    sum+= root.data
    
    for child in root.children:
        sumOfAllNodes(child)
	
    return sum