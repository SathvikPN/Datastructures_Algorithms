class ArrayStack:
    """stack implementation using list"""
    
    def __init__(self,capacity=0):
        """create stack with custom capacity"""
        self._data = [None]*capacity # non-public list instance
        self._capacity = capacity
        self._n = 0  # number of elements currently in stack
        
    def capacity(self):
        """Return MAX_SIZE of stack"""
        if self._capacity:
            return self._capacity
        else:
            return 'Capacity_NOT_SET'
    
    def __len__(self):
        """Return number of elements in stack"""
        return self._n
    
    def is_empty(self):
        return self._n==0
    
    def top(self):
        if self.is_empty():
            raise EmptyStack('No elements in stack to look for TOP') # custom error exception
        return self._data[-1]
    
    def push(self,value):
        if len(self)<self._capacity:
            self._data[self._n] = value # DO NOT Append!!
            self._n += 1
            return value,'PUSH success'
        elif self._capacity==0:
            self._data.append(value)
            self._n += 1
            return value,'PUSH success'
        else:
            raise StackFull(f'Initialised stack capacity was [{self._capacity}]') # custom error exception class
            
    def pop(self):
        if self.is_empty():
            raise EmptyStack('No elements to POP')
        value = self._data[self._n - 1]  # self._n pointing to next positiion to welcome new value
        self._data[self._n - 1] = None  # restoring space with None
        self._n = self._n - 1  # adjust for reduced data list
        return value
    
class EmptyStack(Exception):  # E must be capital in parameter i.e. Exception
    pass
class StackFull(Exception):
    pass







#----- Driver code ------------------------------------------------
if __name__ == '__main__': # condition
    """
    Below code (This code block)
    Executes: only if invoked this file directly
    DOES-NOT-Execute: if this file is being imported in another module
    """
    
    s = ArrayStack(1)
    a = ArrayStack()
    print(f'capacity:  s = {s.capacity()}    a = {a.capacity()}')
    
    for i in range(1,9,3):
        print("Push to a",a.push(i))
    print('stackSize',len(a))
    
    print('top',a.top())

    for i in range(3):
        print(f"Pop from a {a.pop()}     stack empty? {a.is_empty()}")

    #s.push(1)
    #s.push(2) # Error
    # ArrayStack.StackFull: Initialised stack capacity [1]
    
    #print(s.pop()) # pops value 1
    #print(s.pop()) # Error
    # ArrayStack.EmptyStack: No elements to POP