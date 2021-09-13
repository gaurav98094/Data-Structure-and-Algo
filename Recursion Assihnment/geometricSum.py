## Read input as specified in the question.
## Print output as specified in the question.
'''
Given k, find the geometric sum i.e.
1 + 1/2 + 1/4 + 1/8 + ... + 1/(2^k) 
using recursion.

'''

def geometric_sum(k):
    if k==0:
        return 1
    else:
        return 1/(2**k) + geometric_sum(k-1)


k = int(input())
print("%.5f" % geometric_sum(k))