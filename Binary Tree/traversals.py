

#Pre Order Traversals
def preOrder(root):
	# Your code goes here
    if root is None:
        return
    
    print(root.data,end=" ")
    preOrder(root.left)
    preOrder(root.right)


#PostOrder Traversals
def postOrder(root):
    if root is None:
        return
    
    postOrder(root.left)
    postOrder(root.right)
    print(root.data,end=" ")