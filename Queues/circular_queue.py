class CircularQueue:
    """ Queue implementation using circularly linked list (Round_Robin_Scheduling)
    
    When using _tail instance variable, explicit _head is redundant in circular queue
    since _tail._next points to _head.
    rotate(): dequeue element and enqueue same at end of list
    """

    # Nested Node class ----------------------
    class _Node:
        def __init__(self,element, next):
            __slots__ = '_element','_next'  # streamline memory usage
            self._element = element
            self._next = next

    # Queue Methods --------------------
    def __init__(self):
        """ iniitalise empty queue """
        self._tail = None
        self._size = 0

    def is_empty(self):
        return self._size == 0

    def __len__(self):
        return self._size

    def enqueue(self,e):
        newest = self._Node(e,None)
        if self.is_empty():
            newest._next = newest # circular representation of single node in circular list
        else:
            newest._next = self._tail._next
            self._tail._next = newest
        self._tail = newest
        self._size += 1
        return f'enqueue success {e}'

    def dequeue(self):
        if self.is_empty():
            raise EmptyQueue('Queue is empty')
        
        oldhead = self._tail._next
        if self._size == 1:     # single node edge case
            self._tail = None
        else:
            self._tail._next = oldhead._next # bypass oldhead

        self._size -= 1
        return oldhead._element

    def front(self):
        if self.is_empty():
            raise EmptyQueue('Queue is empty')
        head = self._tail._next 
        return head._element

    def rotate(self,k=1):
        if self.is_empty():
            raise EmptyQueue('Empty queue. No elements to rotate')
        
        for i in range(k):
            self._tail = self._tail._next  # traverse
        
        return f'SUCCESS: Rotate by {k} elements '


class EmptyQueue(Exception):
    pass

if __name__=='__main__':
    pass
    # Q = CircularQueue()
    # for i in range(1,9,2):
    #     print(Q.enqueue(i))

    # print('Traverse Queue_linked_list: ',end=' ')
    # for i in range(len(Q)):
    #     print(Q.front(), end=' ')
    #     Q.rotate()
    
    # print()


    # print(Q.rotate(2), end=' ')
    # for i in range(1,9,2):
    #     print(Q.dequeue(), end=' ')