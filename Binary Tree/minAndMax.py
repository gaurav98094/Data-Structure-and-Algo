'''
For a given a Binary Tree of type integer, find and return the minimum and the maximum data values.
Return the output as an object of Pair class, which is already created.

Sample Input 1:
8 3 10 1 6 -1 14 -1 -1 4 7 13 -1 -1 -1 -1 -1 -1 -1

Sample Output 1:
1 14


Sample Input 2:
10 20 60 -1 -1 3 50 -1 -1 -1 -1 

Sample Output 2:
3 60

'''


from sys import setrecursionlimit
import queue

setrecursionlimit(10 ** 6)


#Following is the structure used to represent the Binary Tree Node
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None



#Representation of the Pair Class
class Pair :

    def __init__(self, minimum, maximum) :
        self.minimum = minimum
        self.maximum = maximum



def getMinAndMax(root) :
    #Your code goes here
    if root == None:
        return Pair(99999,-9999999)
    
    if root.left ==None and root.right==None:
        d = root.data
        return Pair(d,d)
    
    first = getMinAndMax(root.left)
    minL = first.minimum
    maxL = first.maximum
    
    second = getMinAndMax(root.right)
    minR = second.minimum
    maxR = second.maximum
    
    mini = min(minL,minR,root.data)
    maxi = max(maxL,maxR,root.data)
    
    return Pair(mini,maxi)
