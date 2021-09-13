def count(head):
    if head == None:
        return 0
    return 1 + count(head.next)

def bubbleSort(head) :
	#Your code goes here
    if head is None or head.next is None:
        return head
    
    
    for i in range(count(head)-1):
        curr = head
        prev = None
        nxt = head.next
        while nxt:
            if curr.data > nxt.data:
                if prev == None:
                    prev = curr.next
                    nxt = nxt.next
                    prev.next = curr
                    curr.next = nxt
                    head = prev
                else:
                    tmp = nxt
                    nxt = nxt.next
                    prev.next = curr.next
                    prev = tmp
                    tmp.next = curr
                    curr.next = nxt
            else:
                prev = curr
                curr = nxt
                nxt = nxt.next
                
        i+=1
    return head
    
                    