


'''
Sample Input 1:
8 5 10 2 6 -1 -1 -1 -1 -1 7 -1 -1
6 10

Sample Output 1:
6 7 8 10
'''

def elementsInRangeK1K2(root, k1, k2):
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    if root is None:
        return
    
    if root.data<k1:
        elementsInRangeK1K2(root.right,k1,k2)
    elif root.data>k2:
        elementsInRangeK1K2(root.left,k1,k2)
    else:
        elementsInRangeK1K2(root.left,k1,k2)
        print(root.data,end=" ")
        elementsInRangeK1K2(root.right,k1,k2)