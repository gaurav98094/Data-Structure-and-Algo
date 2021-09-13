class qUsingTwoStack:
    def __init__(self):
        self.__a1 = []
        self.__a2 = []

    def enqueue(self,data):
        if len(self.__a1)==0:
            self.__a1.append(data)
        
        while len(self.__a1)!=0:
            self.__a2.append(self.__a1.pop())

        self.__a1.append(data)

        while len(self.__a2)!=0:
            self.__a1.append(self.__a2.pop())
        


    def dequeue(self):
        if len(self.__a1)==0:
            return -1

        return self.__a1.pop()

    def front(self):
        if len(self.__a1)==0:
            return 0
        return self.__a1[-1]

    def isEmpty(self):
        return len(self.__a1)==0

    def size(self):
        return len(self.__a1)

q = qUsingTwoStack()
q.enqueue(1)
q.enqueue(2)
q.enqueue(4)
q.enqueue(5)

print("Is Empty : ",q.isEmpty())
print("Size : ",q.size())
print("Front : ",q.front())

print("\nD Queue : ",q.dequeue())

print("\nIs Empty : ",q.isEmpty())
print("Size : ",q.size())
print("Front : ",q.front())


