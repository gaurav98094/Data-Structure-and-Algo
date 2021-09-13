
from sys import stdin
from typing_extensions import TypeVarTuple


#Following is the structure of the node class for a Singly Linked List
class Node :

    def __init__(self, data) :
        self.data = data
        self.next = None


class Queue :

    #Define data members and __init__()
    def __init__(self):
        self.__head = None
        self.__count = 0


    '''----------------- Public Functions of Stack -----------------'''

    def getSize(self) :
        #Implement the getSize() function
        return self.__count



    def isEmpty(self) :
        #Implement the isEmpty() function
        if self.__count<=0:
            return False
        else:
            return True



    def enqueue(self, data) :
        #Implement the enqueue(element) function
        newNode = Node(data)
        if self.__head is None:
            self.__head = newNode
        else:
            newNode.next = self.__head.next
            self.__head = newNode
        self.__count+=1




    def dequeue(self) :
        #Implement the dequeue() function
        if self.isEmpty():
            return -1
        else:
            if self.__count==1:
                ele = self.__head.data
                self.__head= None
                self.__count = 0
                return ele
            else:
                tmp = self.__head
                while tmp.next is not None:
                    tmp = tmp.next
                ele = tmp.next.data
                tmp.next = tmp.next.next
                return ele


    def front(self) :
        #Implement the front() function
        if self.__count==0:
            return -1
        else:
            return self.__head.data
        

		