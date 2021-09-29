
class PriorityQueueNode:
    def __init__(self,val,priority):
        self.val = val
        self.priority = priority

class PriorityQueue:
    def __init__(self):
        self.pq=[]

    def get_size(self):
        return len(self.pq)

    def isEmpty(self):
        return self.get_size()==0

    def __percolateUp(self):
        childIndex = self.get_size()-1

        while childIndex>0:
            parentIndex = (childIndex-1)//2

            parent = self.pq[parentIndex]
            child = self.pq[childIndex]

            if child.priority<parent.priority:
                self.pq[childIndex],self.pq[parentIndex] = self.pq[parentIndex],self.pq[childIndex]
            else:
                break
            

    def insert(self,val,priority):
        node = PriorityQueueNode(val,priority)
        self.pq.append(node)
        self.__percolateUp()

    def print_Queue(self):
        for child in self.pq:
            print("Val :",str(child.val),", Pri :",str(child.priority)+" --- > ",end=" ")
        print("None")


    def delete(self):
        pass


obj = PriorityQueue()

obj.insert(1,1)
obj.insert(12,0)
obj.insert(18,2)
obj.print_Queue()