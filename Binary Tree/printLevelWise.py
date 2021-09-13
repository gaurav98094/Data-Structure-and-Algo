from sys import setrecursionlimit
import queue

setrecursionlimit(10 ** 6)


#Following is the structure used to represent the Binary Tree Node
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def printLevelWise(root):
    if root is None:
        return root
    
    q = queue.Queue()
    q.put(root)
    
    q1 = queue.Queue()
    q1.put(root)
    
    while q1.qsize()!=0:
        q=q1
        q1 = queue.Queue()
        
        while q.qsize()!=0:
            tmp = q.get()
            print(tmp.data,end=" ")

            if tmp.left==None:
                #print("-1",end="")
                pass
            else:
                q1.put(tmp.left)

                #print(tmp.left.data,end="")

            #print(",R:",end="")
            if tmp.right==None:
                #print("-1",end="")
                pass
            else:
                q1.put(tmp.right)
        print()
    

        