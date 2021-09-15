'''
Sample Input 1 :
8 5 10 2 6 -1 -1 -1 -1 -1 7 -1 -1
2

Sample Output 1 :
true


Sample Input 2 :
8 5 10 2 6 -1 -1 -1 -1 -1 7 -1 -1
12

Sample Output 2 :
false


'''


#Solution
def searchInBST(root, k):
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    if root is None:
        return False
    
    if root.data>k:
        #print("g",root.data)
        return searchInBST(root.left,k)
    elif root.data<k:
        #print("l",root.data)
        return searchInBST(root.right,k)
    elif root.data==k:
        #print(root.data)
        return True