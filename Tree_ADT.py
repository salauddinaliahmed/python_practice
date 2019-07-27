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

    #Defining iterations.
    """
    The reason behind doing this is: to reach all the elements , we need to have all positions. 
    """
    def __iter__(self):
        for each in self.positions():
            yield each.element()

    # Defining traversal methods using the positions of the node. 

    def preorder(self):
        #Check if the object is empty.
        if not self.is_empty():
            #Now call the non-public method with the root as the parameter
            for p in self._subtree_preorder(self.root()):
                yield p
    
    def _subtree_preorder(self, p):
        yield p                                         # Visits p
        for c in self.children(p):                      # Loops through p's children
            # For each child call itself.                       
            for other in self._subtree_preorder(c):     # Pre-orders child's subtree. 
                yield other                             # This prints immediate children of each of the node. ( we are looping though children because we need to print children of left and then right.)

    #Using preorder as default.
    def positions(self):
        return self.preorder()


    # Defining recursive depth.
    def depth(self, p):
        if self.is_root(p): # Base case. Returning 0 for reaching root.
            return 0
        else:
            # Here we are adding one each time we find something other than root.
            # Recursively checking if the parent of the node p exists and peforming addition of the parent too (incase it exists)
            return 1 + self.depth(self.parent(p))

    # Computing height.
    def height1(self):
        return max(self.depth(p) for p in self.Position() if self.is_leaf(p))
        """
         This means, for each "p" we check if that is the leaf. If it is, then we add it to p. 
         Now, p becomes a generator object. It is holding a set of numbers which are sort of a list but
         not an actual list. 
         You can still perform operations like max(), abs(), min() etc.
         But it is of type generator. 
         Here, it just returns the highest number of children as height.
        """
    # Better height.

    """ 
    Rationale behind recursion, you need to call a function while manipulating its next call, such that it finally leads
    to a base case and building up from the reverse order of the base case gives us the final output.
    """
    def _height2(self,p):
        if self.is_leaf(p):
            return 0
        else:
            return 1 + max(self._height2(c) for c in self.children(p))
            # The max() value is a generator of the values from left child and right child, which return the height.
            # Unless leaf is found, we keep iterating over a function and keep adding one to the parent with that leaf node.

    def height(self, p = None):
        if p is None:
            p = self.root()
        return self._height2(p)

    def postorder(self):
        if not self.is_empty():
            for p in self._subtree_postorder(self.root()): # This is a continously growing list of elements.
                yield p # This yeild is given to the user. 


    # This function does not return anything to the user directly, it gives it to postorder() who gives it to the user.
    def _subtree_postorder(self, p):
        #Loop through children
        for p in self.children(p):
            #Loop though each element of the child.
            for other in self._subtree_postorder(p):
                # This returns all the children of the node p. 
                yield other
        #This then returns the node of the parent to the generator loop in post_order.
        yield p

    
