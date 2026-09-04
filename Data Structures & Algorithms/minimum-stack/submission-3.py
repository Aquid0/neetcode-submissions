from math import inf

class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []
        self.minValue = inf

    def push(self, val: int) -> None:
        self.stack.append(val)

        self.minValue = min(self.minValue, val)
        self.minStack.append(self.minValue)

    def pop(self) -> None:
        self.minStack.pop()
        self.stack.pop()
        if len(self.minStack) > 0:
            self.minValue = self.minStack[-1]
        else:
            self.minValue = inf

    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.minStack[-1]
        
