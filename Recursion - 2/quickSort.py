import sys
sys.setrecursionlimit(100000)

def partition(arr,si,ei):
    piv= arr[si]
    c =0
    
    for x in range(si,ei+1):
        if piv > arr[x]:
            c+=1
    arr[si+c],arr[si] = arr[si],arr[si+c]
    piv_index = si+c
    
    i=si
    j=ei
    while i<j:
        if arr[i]<piv:
            i+=1
        elif arr[j]>=piv:
            j-=1
        else:
            arr[i],arr[j] = arr[j],arr[i]
            i+=1
            j-=1
            
            
    return piv_index
    


def quickSort(arr, si, ei):
    # Please add your code here
    if si>=ei:
        return
    
    par = partition(arr,si,ei)
    quickSort(arr,si,par-1)
    quickSort(arr,par+1,ei)
    

n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
quickSort(arr, 0,len(arr)-1)
print(*arr)
