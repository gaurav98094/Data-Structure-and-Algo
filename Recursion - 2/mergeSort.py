import sys
sys.setrecursionlimit(1500000000)

def merge(a1,a2,arr):
    i,j,k=0,0,0
    while i<len(a1) and j<len(a2):
        if a1[i]<a2[j]:
            arr[k] = a1[i]
            i=i+1
            k=k+1
        else:
            arr[k] = a2[j]
            j=j+1
            k=k+1
    
    
    while i<len(a1):
        arr[k] = a1[i]
        i=i+1
        k=k+1
        
    while j<len(a2):
        arr[k]=a2[j]
        j=j+1
        k=k+1
        

def mergeSort(arr):
    if len(arr)==0 or len(arr)==1:
        return
    mid = len(arr)//2
    a1 = arr[:mid]
    a2 = arr[mid:]
    
    mergeSort(a1)
    mergeSort(a2)
    merge(a1,a2,arr)

# Main
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
mergeSort(arr)
print(*arr)
