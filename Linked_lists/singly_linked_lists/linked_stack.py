class LinkedStack():
    """ LIFO implementation using Singly_linked_lists 

    (stack_top = Linked_list_head) 
    since insert and delete elements in constant time only at the head 
    """

    # Nested Node class ----------------------------------------------------
    class _Node():
        """ Lightweight, nonpublic class for storing a singly linked node"""

        __slots__ = '_element', '_next'     
        # avoids the use of an auxiliary dictionary which requires 
        # additional memory usage beyond the raw data that it stores.

        def __init__(self,element,next):
            """ node object storing references for element and pointer to next node """
            self._element = element
            self._next = next


    # Stack Methods ------------------------------------------------------
    def __init__(self):
        """ Initialise empty stack with stack top as linked_list head """
        self._head = None
        self._size = 0

    def is_empty(self):
        return self._size == 0

    def top(self):
        """ Return (but do not remove) the element at the top of the stack """
        if self.is_empty():
            raise EmptyStack('Stack Empty')
        return self._head._element

    def __len__(self):
        return self._size

    def push(self,e):
        """ add element e to beginning of linked_list """
        # newest = self._Node(e,self._head)
        # self._head = newest
        self._head = self._Node(e,self._head)
        self._size += 1
        return 'Push Success'

    def pop(self):
        """ Return head element and update head pointer """
        if self.is_empty():
            raise EmptyStack('Empty stack')
        ans = self._head._element
        self._head = self._head._next
        self._size -= 1
        return ans

class EmptyStack(Exception):
    pass


if __name__=='__main__':
    pass
    # L = LinkedStack()
    # for i in range(2,7,2):
    #     print(L.push(i),i)
    # print(f'stack size {len(L)}')
    # print(f'stack top {L.top()}')

    # for i in range(3):
    #     print(L.pop())
    
    # # L.pop() # Error occurs
    # print(L.top())