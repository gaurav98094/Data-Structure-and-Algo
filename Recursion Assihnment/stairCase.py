'''
A child is running up a staircase with N steps, and can hop either 1 step, 2 steps or 3 steps at a time. 
Implement a method to count how many possible ways the child can run up to the stairs. 
You need to return number of possible ways W.


Input format :
Integer N
Output Format :
Integer W
Constraints :
1 <= N <= 30
Sample Input 1 :
4
Sample Output 1 :
7
Sample Input 2 :
5
Sample Output 2 :
13

'''

# Define Function
def stair_case(n):
    if n==0:
        return 1
    
    if n<=0:
        return 0

    
    return stair_case(n-1) + stair_case(n-2) + stair_case(n-3)






# Input
n = int(input())

#Function Call
ans = stair_case(n)

#Print Output
print(ans)