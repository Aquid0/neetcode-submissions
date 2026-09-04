from math import inf

class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []
        self.minValue = inf

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.minValue = min(val, self.minStack[-1]) if self.minStack else val
        self.minStack.append(self.minValue)

    def pop(self) -> None:
        self.minStack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.minStack[-1]
        
