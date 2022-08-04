class MinStack:
    # Only problem is how to return min by O(1) time
    # Using a minStack
    # stack    = [4, 8, 2, -1, 9, -4]
    # minStack = [4, 4, 2, -1, -1, -4]

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        
        if self.minStack:
            val = min(val, self.minStack[-1])
            
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()