class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = [] # Represents the smallest value up to that point in the stack
                           # To be kept in sync with stack

    def push(self, val: int) -> None:
        self.stack.append(val)      
        current_min = min(val, self.minStack[-1]) if self.minStack else val
        self.minStack.append(current_min)

    def pop(self) -> None:
        self.stack.pop(-1)
        self.minStack.pop(-1)

    def top(self) -> int:
        return self.stack[-1]        

    def getMin(self) -> int:
        return self.minStack[-1]
        
