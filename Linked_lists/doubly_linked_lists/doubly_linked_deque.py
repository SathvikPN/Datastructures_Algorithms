# using Sentinel nodes: header, trailer instead of just variable instances head,tail.
# Eliminates the special case of checking empty linked list.
# All insertions, deletions in a unified manner.
# new node placed between a pair of existing sentinel nodes.
# every node that is to be deleted is guaranteed to have neighbors on each side.

class _DoublyLinkedBase:
    """ a base class for doubly linked list representation """

    # Nested node class -------------
    class _Node:
        __slots__ = '_element','_prev','_next'

        def __init__(self,element,prev,next):
            self._element = element
            self._prev = prev
            self._next = next


    def __init__(self):
        self._header = self._Node(None,None,None)
        self._trailer = self._Node(None,None,None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0

    def __len__(self):
        return self._size 

    def is_empty(self):
        return self._size == 0

    def _insert_between(self,e,predecessor,successor):
        """ Add element e between two nodes """
        newest = self._Node(e,predecessor,successor) # linked to neighbours
        predecessor._next = newest
        successor._prev = newest
        self._size += 1
        return newest

    def _delete_node(self,node):
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        element = node._element  # record the to-be-deleted element
        node._prev = node._next = node._element = None # deprecate node
        return element


class LinkedDeque(_DoublyLinkedBase): # Note Inheritance
    """ Double-ended Queue (deque) implementation using doubly linked lists """

    # No explicit __init__ since inherited version is suffice for new instance

    def first(self):
        if self.is_empty(): # inherited method
            raise Exception('deque is empty')
        return self._header._next._element

    def last(self):
        if self.is_empty():
            raise Exception('deque is empty')
        return self._trailer._prev._element

    def insert_first(self,e):
        self._insert_between(e,self._header, self._header._next) # after header sentinel

    def insert_last(self,e):
        self._insert_between(e,self._trailer._prev, self._trailer) # before trailer sentinel

    def delete_first(self):
        if self.is_empty():
            raise Exception('Empty Deque')
        return self._delete_node(self._header._next) # inherited delete method

    def delete_last(self):
        if self.is_empty():
            raise Exception('Empty deque')
        return self._delete_node(self._trailer._prev) # inherited method


if __name__=='__main__':
    pass

    # a = LinkedDeque()
    # for i in range(3):
    #     a.insert_first(i)

    # for i in range(3,6):
    #     a.insert_last(i)

    # print(f'deque size: {len(a)}')

    # for i in range(6):
    #     print(a.delete_first(),end=' ')

    # # for i in range(6):
    # #     print(a.delete_last(),end=' ')




    