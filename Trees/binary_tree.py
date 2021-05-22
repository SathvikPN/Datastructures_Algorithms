from general_tree import Tree

class BinaryTree(Tree):
    """ Abstract base class representing binary tree structure. 
    
    Inherits general tree structure
    """

    # Additional Abstract Methods ------------------------------
    def left(self,p):
        """ Return a Position representing p's left child.

        Return None if p does not have left child.
        """
        raise NotImplementedError('must be implemented by subclass')

    def right(self,p):
        """ Return a Position representing p's right child.

        Return None if p does not have right child.
        """
        raise NotImplementedError('must be implemented by subclass')



    # Concrete Methods ---------------------------------------------
    def sibling(self,p):
        """ Return Position representing p's sibling (None if no sibling) """
        parent = self.parent(p)
        if parent is None: # if p is root
            return None    # root has no siblings

        else:
            if p == self.left(parent):
                return self.right(parent)   # Possibly None
            else:
                return self.left(parent)    # Possibly None

    def children(self, p):
        """ Generate an iteration of Positions representing p's children """
        if self.left(p) is not None:
            yield self.left(p)
        
        if self.right(p) is not None:
            yield self.right(p)

    
# IN-ORDER Tree traversal --------------------------------------------------------------

    # Algorithm inorder(p):
    #     if p has a left child lc then
    #         inorder(lc) {recursively traverse the left subtree of p}
    # 
    #     perform the “visit” action for position p
    # 
    #     if p has a right child rc then
    #         inorder(rc) {recursively traverse the right subtree of p}

    def inorder(self):
        """ Generate an inorder iteration of positions in the tree """
        if not self.is_empty():
            for p in self._subtree_inorder(self.root()):
                yield p

    def _subtree_inorder(self, p):
        """ Generate an inorder iteration of positions in subtree rooted at p """

        # if left child exists, traverse its subtree
        if self.left(p) is not None: 
            for other in self. subtree inorder(self.left(p)):
                yield other
        
        yield p

        # if right child exists, traverse its subtree
        if self.right(p) is not None:
            for other in self. subtree inorder(self.right(p)):
                yield other

    
    # override inherited version to make inorder the default
    def positions(self):
        """ Generate an iteration of the tree s positions """
        return self.inorder()    # make inorder the default