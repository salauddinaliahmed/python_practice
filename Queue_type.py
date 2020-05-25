# Creating a queue adt

class QueueType:
    # Default size of the queue.
    DEFAULT_SIZE = 10
    def __init__(self):
        self._data = [None] * QueueType.DEFAULT_SIZE
        self._size = 0
        self._front = 0

    def is_empty(self):
        return self._size == 0
        
    #defining dequeue and enqueue.
    def dequeue(self):
        if not self.is_empty():
            answer = self._data[self._front]
            self._data[self._front] = None
            self._front = (self._front + 1) % len(self._data)  #Need to understand how this is derieved. 
            self._size -= 1
            return answer
        
    # Enqueue
    def enqueue(self, e):
        avail = (self._size + self._front) % len(self._data)
        self._data[avail] = e
        self._size += 1
        

