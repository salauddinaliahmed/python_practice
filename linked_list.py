class Linked_List:

	class _Node:
		def __init__(self, element, next):
			self._element = element
			self._next = next

	def __init__(self):
		self._head = None
		self._size = 0

	def _len(self):
		return self._size

	def is_empty(self):
		print ("Is_empty called",self._size)
		return self._size == 0

	def add(self,element):
		self._head = self._Node(element,self._head)
		self._size += 1
	

	def remove(self):
		print (self._size)
		if self.is_empty():
			print ("Linked list is empty")
		else:
			print("Removed",self._head)
			self.head = None
			

ll = Linked_List()
ll.add(12)




