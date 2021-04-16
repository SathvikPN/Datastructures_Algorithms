class ArrayStack():
    """ LIFO implementation using Python Lists as underlying storage for stack """

    def __init__(self):
        """ Initialize stack """
        self._stack = []

    def is_empty(self):
        return self._stack == []

    def top(self):
        if self.is_empty():
            raise Exception('Empty stack')
        return self._stack[-1]

    def __len__(self):
        return len(self._stack)

    def push(self,e):
        self._stack.append(e)
    
    def pop(self):
        if self.is_empty():
            raise Exception('Empty stack error')
        else:
            return self._stack.pop()

if __name__=='__main__':
    # pass
    a = ArrayStack()
    a.push(1)
    a.push(2)
    print(a.is_empty(), len(a))

