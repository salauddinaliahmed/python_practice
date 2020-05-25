#Creating a double linked list data structure.

class _DoubleLinkedList():
    
    class _Node():
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
        

# Now we create the functionality which the users can interface with. 
class LinkedDeque(_DoubleLinkedList):
    #Function to return the first element.
    def first(self):
        if self._isempty():
            raise Exception("Empty linked list")
        return self._header._next._element

    # Returning last element
    def last(self):
        if self._isempty():
            raise Exception("Empty linked list")
        return self._tailer._prev._element
    
    # inserting at the beginning.
    def insert_first(self, e):
        self._insert_between(self._header, e, self._header._next)
        return "Success, entered first"

    # inserting at the end.
    def insert_end(self, e):
        self._insert_between(self._tailer._prev, e, self._tailer)
        return "Success, entered last"
    
    # delete first.
    def delete_first(self):
        if self._isempty():
            raise Exception("Linked list is empty")
        self._delete_between(self._header._next)
        return "Success, deleted first"
    
    # delete last.
    def delete_last(self):
        if self._isempty():
            raise Exception("Linked list is empty")
        self._delete_between(self._tailer._prev)
        return "Success, deteled last"
    

#Calling class and functions. 
x = LinkedDeque()
x.insert_first(10)
x.insert_first(20)
print (x.first())
x.insert_end(30)
x.insert_end(40)
print (x.last())
