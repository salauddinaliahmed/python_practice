#Creating a double linked list data structure.

class _DoubleLinkedList:
    
    class _Node:
        # Initializing the node. The node will now have a head and a tail pointer along with the element. 
        def __init__(self,head, e,tail):
            self._prev = head
            self._element = e
            self._next = tail
    
    #Intitializing the "Sentinal" nodes when we create a constructor of the Double linkedlist class.
    def __init__(self):
        self._header = self._Node(None, None, None)
        self._tailer = self._Node(None, None, None)
        
        #Once the empty nodes are created, we move towards making the connection. 
        #Mapping header.
        self._header._next = self._tailer
        #Mapping tailer.
        self._tailer._prev = self._header

        #Important! Initializing the size of the linked list as 0.
        self._size = 0

    #Basic insert function operation. We will be abstracting the details here. 
    def _insert_between(self, predecessor, element, sucessor):
        #First thing we do is we create the Node. The node points to the precursor and successor already. 
        new_node = self._Node(predecessor,element,sucessor)
        
        #Once the new node is created and points to the appropriate nodes. We need to update the links of precursor and sucessor to map 
        # the new node.
        predecessor._next = new_node
        sucessor._prev = new_node

        #increment the size of the linked list.
        self._size += 1
        return new_node
    
    #Basic delete function. Will abstract the complete functionality.
    def _delete_between(self,node):
        #The node to be deleted is passed. 
        # To delete a node, we need to dereference its previous and its next and point the other elements together. 

        # We gather what the node was pointing to originally. 
        node_prev = node._prev
        node_next = node._next

        # We have now re-assigned the other connecting links of the linkedlist. WE HAVE NOT YET TAKEN OFF THE POINTERS OFF OFF THE NODE.
        node_prev._next = node_next
        node_next._prev = node_prev

        #Decrease the size.
        self._size -= 1

        element = node._element

        #Re-claiming the new node. Also called as deprecating node.
        node._prev = node._next = node._element = None

        return element

    #Defining current length function.
    def __len__(self):
        return self._size

    #Defining method to check if linkedlist is empty. 

    def _isempty(self):
        return self._size == 0

#Calling class and functions. 
#---------------------------------------------------------------------------------#

#Creating positional list. 

class PositionalList(_DoubleLinkedList):
    class Position:
        # Initializing the container.
        def __init__(self,container, node):
            self._container = container
            self._node = node

        # Returning the element stored at the element.
        def element(self):
            return self._node._element

        # Checking if the positions of 2 nodes is the same.
        def __eq__(self,other):
            return type(other) is type(self) and other._node is self._node

        # Checking if they are not equal.
        def __ne__(self,other):
            return not (self == other)

    #Checking if the node belongs to the list / is deleted from the list. 
    def _validate(self, p):
        # Checking if p is an object of type position.
        if not isinstance(p, self.Position):
            raise TypeError('p does not belong to position')
        
        #Checking if its in the same instance. 
        if p._container is not self:
            raise ValueError("Does not belong to this instance of the p class")
        
        #Checking if p has any reference to the next of it. 
        if p._node._next is None:
            raise ValueError("p is no longer a valid entry of the list.")
        
        return p._node


    #Creating make position class. ! Need to figure out that this means.
    def _make_position(self, node):
        # Checking if the node is header or tailer. If it is then we cant really create a positional object of it. 
        if node is self._header or node is self._tailer:
            return None
        else:
            # This creates a position object. The first argument is the position object itself and the next is the actual node.
            # This goes into the init method, the container becomes the position object and the node becomes the node. 
            return self.Position(self, node)

    # Inserting the first position, the entire position object(contains Component and Node).
    def first(self):
        return self._make_position(self._header._next)

    # Inserting the last position.
    def last(self):
        return self._make_position(self._tailer._prev)

    # Inserting the element before the passed position.
    def before(self,p):
        node = self._validate(p)
        return self._make_position(node._prev)

    # Inserting after
    def after(self, p):
        node = self._validate(p)
        return self._make_position(node._next)
    
    # Iterating through all the positions and returning the output.
    def __iter__(self):
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)

    #---------- Adding elements -----------#

    # Overwriting the superclass method to insert between. 
    def _insert_between(self, predecessor, e, successor):
        """ Calling the super class method. We did this to encapsulate the workings of the super class _insert_between method.
            When referencing the super class method you dont need to provided self instance. Since you are using the superclass function as an outside function.
            Just like adding and substracting function.
        """
        node = super()._insert_between(predecessor, e, successor)
        return self._make_position(node)

    # Adding at the first position of the linked list. 
    def add_first(self, e):
        return self._insert_between(self._header, e, self._header._next)

    # Adding at the last position of the linked list. 
    def add_last(self, e):
        """ Adding stuff near the tail. So, the new element's previous element should be pointed to the tails previous element.
            The next element to the new element should be the tail.
            This is because the tailer node is a sentinal. 
        """
        return self._insert_between(self._tailer._prev, e, self._tailer)

    # Adding before a specified element.
    def add_before(self, e, p):
        original = self._validate(p)
        return self._insert_between(original._prev, e, original)

    # Adding after a specified element
    def add_after(self, e, p):
        original = self._validate(p)
        return self._insert_between(original, e, original._next)

    # Deleting an element
    def delete(self, p):
        original = self._validate(p)
        return self._delete_between(original)
    
    #Replacing an element with another.
    def replace(self, e, p):
        original = self._validate(p)
        old_value = original._element
        original._element = e
        return old_value


x = PositionalList()
a = x.add_first(10)
x.replace(25, a)
x.add_last(20)
x.add_after(15, a)

# Favorite List.
class FavoriteList:

    #Creating a composition pattern
    class _item:
        # This is used for efficient memory management.
        __slots__ = '_value', '_count'
        def __init__(self, e):
            self._value = e
            self._count = 0
    
    def _find_position(self, e):
        walk = self._data.first()
        # Check if the item is present in the list by walking though the list.
        while walk is not None and walk.element()._value != e:
            walk = self._data.after(walk)
        # Returns object.
        return walk
    
    # This is called when we need to sort the list after an element has been accessed.
    def _move_up(self, p):
        # We are moving from the end of the list to the beginning.
        """
            This is because, the new item might have greater count value. And the sorting is done in the ascending 
            order.
        """
        if p != self._data.first():
            count = p.element()._count
            walk = self._data.before(p)
            if count > walk.element()._count:
                while walk != self._data.first() and count > self._data.before(walk).element()._count:
                    walk = self._data.before(walk)
                # self._data.add_before(count, walk) =-> This is right too, but we need to delete the node too. since we
                # are recreating them using "add_before" method. 
                self._data.add_before(self._data.delete(p),walk)
        
    # Public methods.
    def __init__(self):
        #Creating an empty positional list.
        self._data = PositionalList()

    def _len(self):
        return len(self._data)
    
    def _isempty(self):
        return len(self._data)==0
    
    # Creating an access method.
    def access(self, e):
        p = self._find_position(e)
        if p is None:
            # self._data is the instance of Positional List.
            p = self._data.add_last(self._item(e)) # Initializing the item class as an object. THus the linked list now contains 
                                                   # object references.
        p.element()._count += 1
        # After the access, we need to run the sort.
        return self._move_up(p)
    
    def remove(self, e):
        p = self._find_position(e)
        if p != None:
            self._data.delete(p)

    def top(self, k):
        walk = self._data.first()
        for i in range(k):
            yield walk.element()._value
            walk = self._data.after(walk)
        
fav_x = FavoriteList()
fav_x.access(10)
fav_x.access(14)
fav_x.access(10)
fav_x.access(13)
fav_x.access(14)
fav_x.access(12)
fav_x.access(11)
land = fav_x.top(3)
for each in land:
    print (each)
