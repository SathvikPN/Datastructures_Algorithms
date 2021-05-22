from typing import AwaitableGenerator


class Tree():
    """ Abstract base class representing a tree structure """

    # Nested Position Class ---------------------------------
    class Position():
        """ Abstraction representing location of a single element """

        def element(self):
            """ Return element stored at this position """
            raise NotImplementedError('must be implemented by subclass')

        def __eq__(self,other):
            """ Return True if 'other' Position represents the same location """
            raise NotImplementedError('must be implemented by base class')

        def __ne__(self,other):
            """ Return True if 'other' Position does not represents the same location """
            return not(self==other)     # opposite of __eq__

    


    # Abstract methods that concrete subclass must support -------------------------------
    def root(self):
        """ Return Position representing the tree's root (or None if empty) """
        raise NotImplementedError('must be implemented by subclass')

    def parent(self,p):
        """ Return Position representing parent of p (or None if p is root) """
        raise NotImplementedError('must be implemented by subclass')

    def num_children(self,p):
        """ Return the number of children that position p has """
        raise NotImplementedError('must be implemented by subclass')

    def children(self,p):
        """ Genereate an iteration of Positions representing p's children """
        raise NotImplementedError('must be implemented by subclass')

    def __len__(self):
        """ Return total number of elements in the tree """
        raise NotImplementedError('must be implemented by subclass')


    # Some concrete methods (connected to abstract methods) ----------------
    def is_root(self,p):
        """ Return True if Position p represents the root of the tree """
        return self.root() == p

    def is_leaf(self,p):
        """ Return True if Position p does not have any children """
        return self.num_children(p) == 0

    def is_empty(self):
        """ Return True if the Tree is empty """
        return len(self) == 0

    # Depth and Height Computation of Tree -----------------------------
    def depth(self,p):
        """ Return number of levels separating position P from the root. """
        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p))

    def _height1(self):
        """ Return height of tree """
        # works BUT O(n^2) worst-case time 
        return max(self.depth(p) for p in self.positions if self.is_leaf(p))

    def _height2(self,p):
        """ Return height of subtree rooted at Position p """
        if self.is_leaf(p):
            return 0
        else:
            return 1 + max(self._height2(x) for x in self.children(p))

    def height(self, p=None):
        """ Return height of subtree rooted at Position p.

        If p is None, return height of the entire tree
        """
        if p is None:
            p = self.root()
        
        return self._height2(p)     # start _height2 recursion



    
    def __iter__(self):
        """ Generate an iteration of the tree s elements """
        for p in self.positions():
            yield p.element()

        # To implement the positions method, we have a choice of tree traversal algorithms

    def positions(self):
        """ Generate an iteration of the tree s positions """
        return self.preorder()      # return entire preorder iteration





# PRE-ORDER Tree Traversal --------------------------------------------------------------------------

    # Algorithm preorder(T, p):
    #     perform the “visit” action for position p
    #     for each child c in T.children(p) do
    #         preorder(T, c) {recursively traverse the subtree rooted at c}

    def preorder(self):
        """ Generate a preorder iteration of positions in the tree """
        if not self.is_empty():
            for p in self._subtree_preorder(self.root()): # start recursion
                yield p
    
    def _subtree_preorder(self, p):
        """ Generate a preorder iteration of positions in subtree rooted at p """
        
        yield p     # visit p before its subtrees

        for c in self.children(p):
            for other in self._subtree_preorder(c):
                yield other



# POST-ORDER Tree Traversal ---------------------------------------------------------------------------

    # Algorithm postorder(T, p):
    #     for each child c in T.children(p) do
    #         postorder(T, c) {recursively traverse the subtree rooted at c}
    #     perform the “visit” action for position p

    def postorder(self):
        """ Generate a postorder iteration of positions in the tree. """
        if not self.is_empty():
            for p in self._subtree_postorder(self.root()):
                yield p
    
    def _subtree_postorder(self, p):
        """ Generate a postorder iteration of positions in subtree rooted at p. """
        for c in self.children(p):
            for other in self._subtree_postorder(c):
                yield other
        yield p     # visit p after its subtrees



# BREADTH FIRST Iteration -----------------------------------------------------------------------

    # Algorithm breadthfirst(T):
    #     Initialize queue Q to contain T.root( )
    #     while Q not empty do
    #         p = Q.dequeue( ) {p is the oldest entry in the queue}
    #         perform the “visit” action for position p
    #         for each child c in T.children(p) do
    #             Q.enqueue(c) {add p’s children to the end of the queue for later visits}

    def breadthfirst(self):
        """ Generate a breadth-first iteration of the positions of the tree """
        if not self.is_empty():
            fringe = LinkedQueue()      # known positions not yet yielded
            fringe.enqueue(self.root()) # starting with the root

            while not fringe.is empty():
                p = fringe.dequeue( )   # remove from front of the queue
                yield p                 # report 

                for c in self.children(p):
                    fringe.enqueue(c) # add children to back of queue




