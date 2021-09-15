'''
You are given a Binary Tree of type integer, a target node, and an integer value K.
Print the data of all nodes that have a distance K from the target node. The order in which they would be
 printed will not matter.



Sample Input 1:
5 6 10 2 3 -1 -1 -1 -1 -1 9 -1 -1
3 1
Sample Output 1:
9
6


Sample Input 2:
1 2 3 4 5 6 7 -1 -1 -1 -1 -1 -1 -1 -1
3 3
Sample Output 2:
4
5
'''




def kDistanceDown(root,k):
    if root==None:
        return
    
    if k==0:
        print(root.data)
        return
    
    kDistanceDown(root.left,k-1)
    kDistanceDown(root.right,k-1)
    
    
    
    
    
    

def nodesAtDistanceK(root, node, k) :
    if root==None:
        return -1
    
    
    if root.data==node:
        kDistanceDown(root,k)
        return 0
    
    dl = nodesAtDistanceK(root.left,node,k)
  
    if dl!=-1:
        if dl+1==k:
            print(root.data)
        else:
            kDistanceDown(root.right,k-dl-2)
        return 1+dl
            
    dr = nodesAtDistanceK(root.right,node,k)
    
    if dr!=-1:
        if dr+1==k:
            print(root.data)
        else:
            kDistanceDown(root.left,k-dr-2)
        return 1+dr
    
    return -1
    