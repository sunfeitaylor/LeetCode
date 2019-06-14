class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_idx = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if self.min_idx:
            min_num = self.getMin()
            if x <= min_num:
                self.min_idx.append(len(self.stack) - 1)
        else:
            self.min_idx.append(0)

    def pop(self) -> None:
        try:
            num = self.stack[-1]
            if num == self.stack[self.min_idx[-1]]:
                self.min_idx.pop()
            return self.stack.pop()
        except IndexError:
            raise IndexError('The stack is empty now.')

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        try:
            min_idx = self.min_idx[-1]
            return self.stack[min_idx]
        except IndexError:
            raise IndexError('The stack is empty now.')

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
