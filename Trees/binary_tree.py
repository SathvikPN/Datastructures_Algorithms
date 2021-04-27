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