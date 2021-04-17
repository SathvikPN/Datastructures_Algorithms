class Empty(Exception):
    pass

class ArrayQueue:
    """FIFO queue implementation with list"""
    
    def __init__(self, capacity=10): # default capacity 10
        """create empty queue"""
        self._data = [None]*capacity
        self._size = 0
        self._front = 0
        
    def __len__(self):
        """Return no. elements in queue"""
        return self._size
    
    def is_empty(self):
        return self._size==0
    
    def first(self):
        """Return (but donot remove) element at front of queue"""
        if self.is_empty():
            raise Empty('Empty Queue.')
        return self._data[self._front]
    
    def dequeue(self):
        """Remove and Return front element FIFO"""
        if self.is_empty():
            raise Empty('Empty queue')
        
        answer = self._data[self._front]
        
        self._data[self._front] = None  # help garbage collection 
        
        self._front = (self._front+1) % len(self._data)  # initialised queue length = capacity
        # NOT len(self) which is actual no. elements
        
        self._size = self._size - 1  # decrease queue size
        
        if 0 < self._size < len(self._data)//4 :
            self._resize(len(self._data)//2)
            """reduce the array to half of its current size, whenever the number of elements
                stored in it falls below one fourth of its capacity. a desirable property to 
                have queue space usage worst case Big-Theta(n)"""
            
        return answer
    
    def enqueue(self,value):
        """Add element to back of queue"""
        if self._size == len(self._data):
            self._resize(2*len(self._data)) # double array size if full
            
        available = (self._front + self._size) % len(self._data) # Modular operation for circular array
        self._data[available] = value
        self._size = self._size + 1
        return value, 'enqueue success'

    def _resize(self,capacity):
        """Resize to new list capacity which is greater than current size i.e.len(self)"""
        
        old = self._data  # keep track of existing list
        
        self._data = [None]*capacity  # allocate same list but with new capacity full of None
        
        walk = self._front # start walking from first element to all elements of queue
        
        for k in range(self._size): # consider all existing old elements
            self._data[k] = old[walk] # start newlist[0]<--first     newlist[1]<--- (first+1)%oldsize
            # no matter which index (first) in old list, it is copied to starting index[0] of new list
            walk = (walk+1)%len(old) # traverse old list circularly as it was designed 
            
        self._front = 0  # front in new list 
    
    def capacity(self):  # for debugging _resize
        return len(self._data)