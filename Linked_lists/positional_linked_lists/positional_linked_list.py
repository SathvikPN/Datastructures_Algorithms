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

class PositionalList(_DoublyLinkedBase):
    """ A sequential container of elements allowing positional access """

    # Nested Positional class ---------------------------------------------------------
    class Position:
        """ An abstraction representing the location of single element """

        def __init__(self,container,node):
            """ constructor should not be invoked by user """
            self._container = container
            self._node = node

        def element(self):
            """ Return element stored at this Position """
            return self._node._element

        def __eq__(self,other):
            """ Return True if 'other' is a position representing the same location """
            return (type(other) is type(self)) and (other._node is self._node)

        def __ne__(self,other):
            """ Return true if 'other' does not represent the same location """
            return not(self==other) # opposite of __eq__
 


    # Utility Method ---------
    def _validate(self,p):
        """ Return position's node or Raise appropriate error if invalid """
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type')

        if p._container is not self:
            raise ValueError('p does not belong to this container')

        if p._node._next is None: # deprecated node convention
            raise ValueError('p is no longer valid')

        return p._node

    # Utility Method ------------
    def _make_position(self, node):
        """ Return Position instance for given node (None if Sentinel node) """
        if node is self._header or node is self._trailer:   # boundary condition
            return None                             
        else:
            return self.Position(self, node)    # Legitimate position

    

    # Accessors ----------------
    def first(self):
        """ Return first Position in the list (None if list is empty) """
        return self._make_position(self._header._next)

    def last(self):
        """ Return last Position in list (None if list is empty) """
        return self._make_position(self._trailer._prev)

    def before(self, p):
        """ Return the Position just before Position p (or None if p is first) """
        node = self._validate(p)
        return self._make_position(node._prev)

    def after(self, p):
        """ Return the Position just after Position p (or None if p is last) """
        node = self._validate(p)
        return self._make_position(node._next)

    def __iter__(self):
        """ Generate a forward iteration of the elements of the list """
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)


    
    # Mutators -------------------------------------------------------------
    # override inherited version to return Position, rather than Node
    def _insert_between(self, e, predecessor, successor):
        """ Add element between existing nodes and return new Position """
        node = super()._insert_between(e, predecessor, successor)
        return self._make_position(node)

    def add_first(self, e):
        """ Insert element e at the front of the list and return new Position """
        return self._insert_between(e, self._header, self._header._next)

    def add_last(self, e):
        """ Insert element e at the back of the list and return new Position """
        return self._insert_between(e, self._trailer._prev, self._trailer)

    def add_before(self, p, e):
        """ Insert element e into list before Position p and return new Position """
        original = self._validate(p)
        return self._insert_between(e, original._prev, original)

    def add_after(self, p, e):
        """ Insert element e into list after Position p and return new Position """
        original = self._validate(p)
        return self._insert_between(e, original, original._next)

    def delete(self, p):
        """ Remove and return the element at Position p """
        original = self._validate(p)
        element = self._delete_node(original) # inherited method returns element
        return element

    def replace(self, p, e):
        """ Replace element at position p with new element e. 
        Returns old element """
        original = self._validate(p)
        old_value = original._element
        original._element = e  # Replace with new element
        return old_value