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
