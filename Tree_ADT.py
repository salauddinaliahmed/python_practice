"""
Tree implementation in python.
Taken from: DS and algorithms in python by Goodrich, Tammasia and Goldwesser.
"""
# This is a creation of abstract class.
class Tree:
    class Position:
        def element(self):
            raise NotImplementedError("must be implemented by subclass")    
        def __eq__(self, e):
            raise NotImplementedError("must be implemented by subclass")
        def __ne__(self, e):
            return not (self == e)
    
    def root(self):
        raise NotImplementedError("must be implemented by subclass")
    
    def parent(self,p):
        raise NotImplementedError("must be implemented by subclass")
    
    def num_children(self,p):
        raise NotImplementedError("must be implemented by subclass")

    def children(self):
        raise NotImplementedError("must be implemented by subclass")

    def __len__(self):
        raise NotImplementedError("must be implemented by subclass")
    
    def is_root(self,p):
        return self.root() == p
    
    def is_leaf(self, p):
        return self.num_children(p)==0
    
    def is_empty(self):
        return len(self) == 0
        
