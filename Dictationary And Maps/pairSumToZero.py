'''
Given a random integer array A of size N. Find and print the count of pair of elements in the array which sum up to 0.
Note: Array A can contain duplicate elements as well.
Input format:
The first line of input contains an integer, that denotes the value of the size of the array. Let us denote it with the symbol N
The following line contains N space separated integers, that denote the value of the elements of the array.
Output format :
The first and only line of output contains the count of pair of elements in the array which sum up to 0. 
Constraints :
0 <= N <= 10^4
Time Limit: 1 sec
Sample Input 1:
5
2 1 -2 2 3
Sample Output 1:
2

'''


def pairSum0(l,n):
    freq = {}
    ans = 0
    for x in l:
        if -x in freq:
            ans = ans + freq[-x]
        
        if x not in freq:
            freq[x]=1
        else:
            freq[x]+=1
            
    return ans
                

print(pairSum0([0,0,0,0,0],5))

arr = [int(x) for x in "-2 -12 2 11 12 -2 1 -2 2 -11 12 2 6".split()]
print(pairSum0(arr,13))