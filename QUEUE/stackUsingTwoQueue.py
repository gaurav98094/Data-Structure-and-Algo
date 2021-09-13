from queue import Queue
import sys
sys.setrecursionlimit(10**6)


class Stack :
    def __init__(self):
        self.q1=Queue()
        self.q2=Queue()
        
    def getSize(self) :
        return self.q1.qsize()
    
    def isEmpty(self) :
		#Implement the isEmpty() function
        return self.q1.qsize()==0
    
    def push(self, data) :
		#Implement the push(element) function
        while self.isEmpty()==False:
            self.q2.put(self.q1.get())

        self.q1.put(data)

        while self.q2.empty()==False:
            self.q1.put(self.q2.get())
    
    def pop(self) :
		#Implement the pop() function
        if self.isEmpty():
            return -1

        return self.q1.get()
    
    def top(self) :
		#Implement the top() function
        if self.isEmpty():
            return -1
        
        z = self.q1.queue[0]
        return z
        
        


q = Stack()
print(q.getSize())
q.push(1)
print(q.getSize())