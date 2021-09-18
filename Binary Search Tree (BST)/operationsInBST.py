'''
Implement the BST class which includes following functions -

1. search
Given an element, find if that is present in BST or not. Return true or false.

2. insert -
Given an element, insert that element in the BST at the correct position. If element is equal to the data of the node,
 insert it in the left subtree.

3. delete -
Given an element, remove that element from the BST. If the element which is to be deleted has both children,
 replace that with the minimum element from right sub-tree.

4. printTree (recursive) -

Print the BST in ithe following format -
For printing a node with data N, you need to follow the exact format -
N:L:x,R:y

where, N is data of any node present in the binary tree. x and y are the values of left and right child of node N.
 Print the children only if it is not null.
There is no space in between.
You need to print all nodes in the recursive format in different lines.

'''

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class BST:
    
    def __init__(self):
        self.root = None
        self.numNodes = 0
    
    def printTreeHelper(self,root):
        if root==None:
            return
        
        if root.left is None and root.right is None:
            print(str(root.data)+":")
        elif root.left is not None and root.right is not None:
            print(str(root.data)+":L:"+str(root.left.data)+",R:"+str(root.right.data))
        elif root.left is None:
            print(str(root.data)+":R:"+str(root.right.data))
        else:      
            print(str(root.data)+":L:"+str(root.left.data)+",")
            
        self.printTreeHelper(root.left)
        self.printTreeHelper(root.right)
            
    
    def printTree(self):
        self.printTreeHelper(self.root)
        
        
    
    def searchHelper(self,root,data):
        if root is None:
            return False
        
        if root.data == data:
            return True
        
        if root.data<data:
            return self.searchHelper(root.right,data)
        else:
            return self.searchHelper(root.left,data)
        
    
    def search(self, data):
        return self.searchHelper(self.root,data)
    
    
    def insertHelper(self,root,data):
        if root==None:
            root = BinaryTreeNode(data)
            return root
        
        if data<=root.data:
            root.left = self.insertHelper(root.left,data)
        else:
            root.right = self.insertHelper(root.right,data)
        return root
        

        
    def insert(self, data):
        if self.root is None:
            self.root = BinaryTreeNode(data)
        else:
            self.insertHelper(self.root,data)
        
        self.numNodes
            
        
    def deleteHelper(self,root,data):
        if root is None:
            return False,None
        
        if root.left is None and right.right is None and root.data==data:
            return True,None
        
        if root.data==data and root.left is None:
            root = root.right
            return True,root
        
        if root.data==data and root.right is None:
            root = root.left
            return True,root
        
        if root.left is not None and root.right is not None and root.data==data:
            z = root.left
            root = root.right
            
            zz= root
            while zz.left is not None:
                zz = zz.left
            zz.left = z
            
            return True,root
        
        if root.data<data:
            d,root.right = self.deleteHelper(root.right,data)
        else:
            d,root.left = self.deleteHelper(root.left,data)
    	
        return d,root
                
     
    def delete(self, data):
        root = self.root
        d,self.root = self.deleteHelper(root,data)
        return d
        
        
    
    def count(self):
        return self.numNodes