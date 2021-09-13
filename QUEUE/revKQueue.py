'''
For a given queue containing all integer data, reverse the first K elements.
You have been required to make the desired change in the input queue itself.
Input Format :
The first line of input would contain two integers N and K, separated by a single space. 
They denote the total number of elements in the queue and the count with which the elements need to be reversed respectively.

The second line of input contains N integers separated by a single space, representing the order in which 
the elements are enqueued into the queue.


Output Format:
The only line of output prints the updated order in which the queue elements are dequeued,
 all of them separated by a single space. 


Note:
You are not required to print the expected output explicitly, it has already been taken care of.
 Just make the changes in the input queue itself.


Contraints :
1 <= N <= 10^6
1 <= K <= N
-2^31 <= data <= 2^31 - 1

 Time Limit: 1sec



Sample Input 1:
5 3
1 2 3 4 5

Sample Output 1:
3 2 1 4 5

Sample Input 2:
7 7
3 4 2 5 6 7 8

Sample Output 2:
8 7 6 5 2 4 3


'''




#SOLUTION 1

import queue

def reverseQueue(inputQueue) :
    # Your code goes here
    if inputQueue.qsize()<=1:
        return inputQueue
    
    val = inputQueue.get()
    small = reverseQueue(inputQueue)
    small.put(val)
    
    return small

def segregate(inp,k):
    helper = queue.Queue()
    
    while k!=0:
        helper.put(inp.get())
        k-=1
    
    rev = reverseQueue(helper)
    
    while inp.qsize()!=0:
        rev.put(inp.get())
        
    return rev
    



def reverseKElements(inputQueue, k) :
    #Your code goes here
    ans = segregate(inputQueue,k)
    return ans



# Solution 2

'''
import queue

def reverseQueueKtimes(inputQueue,k) :
    # Your code goes here
    if k<=0 or inputQueue.qsize()<=1:
        return inputQueue
    
    val = inputQueue.get()
    small = reverseQueueKtimes(inputQueue,k-1)
    small.put(val)
    
    return small






def reverseKElements(inputQueue, k) :
    #Your code goes here
	
    rev = reverseQueueKtimes(inputQueue,k)
    
    z = rev.qsize()-k
    
    while z>0:
        rev.put(rev.get())
        z-=1
    
    return rev
'''