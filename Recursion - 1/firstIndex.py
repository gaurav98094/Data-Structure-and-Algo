def firstIndex(arr, x):
    # Please add your code here
    if len(arr)==0:
        return -1
    if arr[0]==x:
        return 0
    
    out = firstIndex(arr[1:],x)
    if out==-1:
        return -1
    else:
        return out + 1

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
x=int(input())
print(firstIndex(arr, x))
