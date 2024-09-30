class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.size = maxSize
        

    def push(self, x: int) -> None:
        if len(self.stack) == self.size:
            return
        self.stack.append(x)

    def pop(self) -> int:
        if len(self.stack) == 0:
            return -1
        val = self.stack.pop()
        return val
        

    def increment(self, k: int, val: int) -> None:
        i = 0
        while i < k and i < len(self.stack):
            self.stack[i] += val
            i += 1
        
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)