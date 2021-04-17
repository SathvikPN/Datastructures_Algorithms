class LinkedQueue():
    """ FIFO using singly_linked_list (queue front = linked_list head) """

    class _Node():
        """ Lightweight, nonpublic class for storing a singly linked node"""

        __slots__ = '_element', '_next'     
        # avoids the use of an auxiliary dictionary which requires 
        # additional memory usage beyond the raw data that it stores.

        def __init__(self,element,next):
            """ node object storing references for element and pointer to next node """
            self._element = element
            self._next = next
    

    # Queue Methods -------
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def is_empty(self):
        return self._size == 0

    def enqueue(self,e):
        newest = self._Node(e,None)
        if self.is_empty():
            self._head = newest # If single node in list, pointed by both head and tail pointers.
        else:
            self._tail._next = newest
            
        self._tail = newest
        self._size += 1
        return 'Enqueue success'

    def dequeue(self):
        if self.is_empty():
            raise EmptyQueue('Queue is empty')

        ans = self._head._element
        self._head = self._head._next
        self._size -= 1

        # if single node in list, it's pointed by both head and tail pointers.
        # if list empty after a dequeue, update tail pointer too
        if self.is_empty(): 
            self._tail = None
        return ans

        # Note:
        #     when dequeue is invoked on a queue with one element, 
        #     we are simultaneously removing the tail of the list.
        
    def __len__(self):
        return self._size

    def front(self):
        if self.is_empty():
            raise EmptyQueue('Empty Queue')
        return self._head._element

class EmptyQueue(Exception):
    pass

if __name__=='__main__':
    pass 
    # Q = LinkedQueue()
    # for i in range(3,10,2):
    #     print(Q.enqueue(i), i)
    # print(f'size {len(Q)}    Front {Q.front()} ')

    # print('Dequeue: ', end=' ')
    # for i in range(3,10,2):
    #     print(Q.dequeue(),end=' ')
    
    # Q.dequeue() # Error occurs

