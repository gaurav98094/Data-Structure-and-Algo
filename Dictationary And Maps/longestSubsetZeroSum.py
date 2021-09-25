'''
Given an array consisting of positive and negative integers, find the length of the longest subarray whose sum is zero.
Input Format:
The first line of input contains an integer, that denotes the value of the size of the array. Let us denote it with the symbol N.
The following line contains N space separated integers, that denote the value of the elements of the array.
Output Format
The first and only line of output contains length of the longest subarray whose sum is zero.
Constraints:
0 <= N <= 10^8
Time Limit: 1 sec
Sample Input 1:
10 
 95 -97 -387 -435 -5 -70 897 127 23 284
Sample Output 1:
5
Explanation:
The five elements that form the longest subarray that sum up to zero are: -387, -435, -5, -70, 897 



'''


def subsetSum(l):
    freq = {0:-1}
    maxi = 0
    
    sumi=0
    
    for i,x in enumerate(l):
        sumi+=x
        if sumi in freq and maxi<i-freq[sumi]:
            maxi=i-freq[sumi]
        
        if sumi not in freq:
        	freq[sumi]=i
        
    print(freq)
    return maxi


# Main
l=list(int(i) for i in "4 1 2 -1 -2 4 8".strip().split(' '))
print(subsetSum(l))