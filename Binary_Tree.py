
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

class LinkedBinaryTree(BinaryTree):
    class _Node:
        __slots__ = '_element', '_left', '_parent', '_right'
        
        #Creating a single node on init
        def __init__(self,_element, _parent=None, _left=None,_right=None):
            self._element = _element
            self._parent = _parent
            self._left = _left
            self._right = _right
            
        
    # We are using position class to find the position of nodes (as object references)
    # We are overriding the position class while inheriting it?

    # Redefining position.
    class Position(BinaryTree.Position):

        def __init__(self, container, node):
            self._container = container
            self._node = node

        def element(self):
            return self._node._element

        def __eq__(self, other):
            return type(other) is type(self) and other._node is self
        
    #Validating the node in the tree.
    def _validate(self, p):
        if not isinstance(p, self.Position):
            print (type(p))
            print("Correct", type(self.Position))
            raise TypeError("p is not proper type Position")
        if p._container is not self:
            raise TypeError("P does not belong to this container")
        if p._node._parent is p._node:
            raise ValueError("p is no longer valid")
        return p._node

    def _make_position(self, p):
        return self.Position(self, p) if p is not None else None
        """
        This basically is a way of telling if is not none, make the position object, else
        do nothing (None)
        """

    # Tree constructor.
    # Initializing the tree with only one root as none and 0 size
    def __init__(self):
        self._root = None
        self._size = 0

    ## Public methods.
    def __len__(self):
        return self._size

    def root(self):
        # Here we need to make the position if it exists. 
        return self._make_position(self._root)
        # This calls the make method and returns the p._node. That is the node at root. given that self._root exists

    #This is a returning method. No checks done here. 
    def parent(self, p):
        #Check if p has a parent, then return the parent.
        node = self._validate(p)
        return self._make_position(node._parent)

    def left(self,p):
        #Validate if the node exists.
        node = self._validate(p)
        return self._make_position(node._left)
    
    def right(self, p):
        node = self._validate(p)
        return self._make_position(node._right)
    
    # Create an algorithm to figure out number of children of node p and not the entire length of subreee
    def num_children(self,p):
        count = 0
        node = self._validate(p)
        if self._make_position(node._right) is not None:
            count += 1
        if self._make_position(node._left) is not None:
            count += 1
        return count
        
        """
        you can also go ahead with 
        node._left and node._right
        Need to run this for a better understanding.
        """

    def _add_root(self, p):
        if self._root is not None:
            raise ValueError("Root already exists.")
        else:
            # Increment the size of the root.
            self._size = 1
            # Create a node of the root.
            self._root = self._Node(p)
            # Make a position object refering to the root, return the position object.
            return self._make_position(self._root)

    def _add_left(self,p,parent):
        #Check if p is a valid node.
        node = self._validate(parent)
        if node._left is not None:
            raise ValueError("Left child already exisits")
        #Create a node. Assinging it to the Node class's left child
        self._size += 1
        node._left = self._Node(p,node)
        #Increment size
        
        #Add to positional list.
        return self._make_position(node._left)

    def _add_right(self, p, parent):
        node = self._validate(parent)
        if node._right is not None:
            raise ValueError("Right child already present")
        #Create node., then map that new node with the parent node.
        self._size += 1
        node._right = self._Node(p, node)
        return self._make_position(node._right)

    def _replace(self, p, replacement):
        #Check if node exists.
        node = self._validate(p)
        """
        When you call makeposition it creates an instance of position with first element as its own instance and node
        as the instance of the node (which contains the parent, element, left and right.
        """
        old = node._element
        node._element = p
        return old

    # This is the difficult part: to delete the node. 
    def delete(self, p):
        print ("In delete method", type(p))
        #First we check if the node exists.
        node = self._validate(p) # Returns the node if the node exists as the instance of the position class and has the node(its own instance variable) pointing to the parent class.
        if node is None:
            raise ValueError("No such node present")
        # check if the number of children are two
        if self.num_children(p) == 2: raise ValueError("Has 2 children, cannot delete")
        # Need to save the child node.
        child_node = node._left if node._left else node._right
        
        #Check if child is not none.
        if child_node is not None:
            #Grand parent becomes parent
            child_node._parent = node._parent
        
        if node is self._root:
            # Removing root, then child becomes the root.
            self._root = child_node
        # meaning that the node is not the root.
       
        #When its not the root, then we need to connect the grandparent to the child
        else:

            parent = node._parent
            if node is parent._left:
                parent._left = child_node
            elif node is parent._right:
                parent._right = child_node
        #Decrement the size
        self._size -= 1
        # Pointing the parent of the node which is deleted to itself. Says in the book, that its by convention.
        node._parent = node
        return node._element


    def _attach(self, p, t1, t2):
    # Attaching t1 and t2 as left and right subtrees.

    # 1. Validate if p exists.
        node = self._validate(p)

    # 2. Check if that node is a leaf node.
        if not self.is_leaf(p): raise ValueError("Not a leaf node")
    
    # 3. Check if the types of trees match.
        if not type(self) is type(t1) and type(t2): raise TypeError("t1 and t2 are not proper tree types")

        # This method belong to tree package.(Which is imported)
        if not t1.is_empty():
            # Set the parent t1 as node.left.
            # IMPORTANT> MAKE CONNECTION BOTH WAYS.Parent is connected to child, child is connected to parent too.
            t1._root._parent = node._left
            # Attach node to root of the first tree
            node._left = t1._root
            
            #Make tree empty
            t1._root = None
            t1._size = 0

        if not t2.is_empty():
            # If statement the two statements at 225 and 226 are flipped, the t2 will point to itself.
            t2._root._parent = node._right
            node._right = t2._root
            #Make tree empty
            t2._root = None
            t2._size = 0

    # Inorder traversal
    def inorder(self):
        if not self.is_empty():
            for p in self._subtree_inorder(self.root()):
                yield p
    
    def _subtree_inorder(self, p):
        if self.left(p) is not None:
            for each in self._subtree_inorder(self.left(p)):
                yield each
        # No more left.
        yield p
        if self.right(p) is not None:
            for each in  self._subtree_inorder(self.right(p)):
                yield each

    # Overwriting positions. 
    def positions(self):
        return self.inorder()

# Running the class.
x = LinkedBinaryTree()
p1 = x._add_root(10)
l = x._add_left(15, p1)
r1 = x._add_right(20, p1)
j = x._add_left(25, r1) 
print (type(j))
print ("J actually->",j)

# Tree 1
t1 = LinkedBinaryTree()
p = t1._add_root(2)
l = t1._add_left(4, p)
r = t1._add_right(6, p)
t1._add_left(8, r) 

# Tree 2
t2 = LinkedBinaryTree()
p = t2._add_root(3)
l = t2._add_left(6, p)
r = t2._add_right(9, p)
t2._add_left(12, r) 

print (x.num_children(p1))
print (x._size)

#x._attach(j, t1, t2)
#print (x._size)

"""
for a in x.postorder():
    print (a.element())
"""
#When i did x.num_children(p->which pointed to instance of T2)
#It gave me the error P does not belong to this container. Since p was the instance of position method for sure, 
# But was of the instance of T2. hence we needed that check

a = x.positions()
for b in a:
    print (b.element())
