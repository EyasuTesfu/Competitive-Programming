class MyQueue:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        temp_stack = []
        if self.empty():
            self.stack.insert(0, x)
        else:
            for item in self.stack:
                temp_stack.insert(0, item)
            while not self.empty():
                self.pop()
            self.stack.insert(0, x)
            for i in range(len(temp_stack)):
                self.stack.insert(0, temp_stack[i])

    def pop(self) -> int:
        return self.stack.pop(0)

    def peek(self) -> int:
        return self.stack[0]

    def empty(self) -> bool:
        if len(self.stack) == 0:
            return True
        return False
# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
