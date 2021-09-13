def lastIndex(arr, x):
    # Please add your code here
    l = len(arr)
    if l==0:
        return -1

	
    out = lastIndex(arr[1:],x)
    
    if out == -1:
        if arr[0]==x:
            return 0
        else:
            return -1
    else:
        return 1 + out

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)

n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
x=int(input())
print(lastIndex(arr, x))
