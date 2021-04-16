class ArrayStackSized():
    """ Array Stack with fixed capacity """

    def __init__(self, CAPACITY=2):
        self._CAPACITY = CAPACITY
        self._data = [None]*self._CAPACITY
        self._top = -1  # top element index if any value inserted

    def is_empty(self):
        return self._top>=0

    def is_full(self):
        return self._top == self._CAPACITY - 1

    def __len__(self):
        return self._top + 1

    def top(self):
        if self.is_empty():
            raise Exception('Stack Empty')
        return self._data[self._top]

    def push(self, e):
        if self.is_full():
            raise Exception('FAILED to push: STACK FULL')
        self._top += 1
        self._data[self._top] = e
        return f'PUSH SUCCESS {e}'

    def pop(self):
        if len(self)==0:
            raise Exception('Empty stack')
        e = self._data[self._top]
        self._data[self._top] = None
        self._top -= 1
        return e



if __name__=='__main__':
    pass

    # a = ArrayStackSized(5)
    # e = 4
    # while True:
    #     try:
    #         print(f'{a.push(e)} Stack_size {len(a)} ')
    #         e += 2
    #     except:
    #         break


    # while True:
    #     try:
    #         print(a.pop())
    #     except:
    #         break
