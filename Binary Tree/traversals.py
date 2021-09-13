

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


# LevelWise
def printLevelWise(root):
    # Your code goes here
    if root is None:
        return root
    
    q = queue.Queue()
    q.put(root)
    
    while q.qsize()!=0:
        tmp = q.get()
        print(tmp.data,end="")
        print(':L:',end="")
        
        if tmp.left==None:
            print("-1",end="")
        else:
            q.put(tmp.left)
            print(tmp.left.data,end="")
            
        print(",R:",end="")
        if tmp.right==None:
            print("-1",end="")
        else:
            q.put(tmp.right)
            print(tmp.right.data,end="")
        print()
        
        