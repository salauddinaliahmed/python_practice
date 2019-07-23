
# Imported the local implementation of the Binary Tree ADT
import Tree_T

class BinaryTree(Tree_T.Tree):
    def left(self,p):
        raise NotImplementedError("must be implemented by a sub class")
    
    def right(self, p):
        raise NotImplementedError("must be implemented by a sub class")
    
    def sibling(self, p):
        # To find sibling, find the parent first.
        parent = self.parent(p)
        if parent is None:
            return Nonec
        else:
            # Check if p is left child of p's parent
            if p == self.left(parent):
                return self.right(parent)
            else:
                return self.left(parent)
    
    # Returning the children on P in a proper order.
    def children(self,p):
        if self.left(p) != None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)

    class _Node:
        __slots__ = '_element', '_left', '_parent', '_right'
        
        #Creating a single node on init
        def __init__(self,_element, _left=None, _parent=None, _right=None):
            self._element = _element
            self._left = _left
            self._right = _right
            self._parent = _parent
        
    # We are using position class to find the position of nodes (as object references)
    # We are overriding the position class while inheriting it?

    # Doubt
    class Position(BinaryTree.Position):


