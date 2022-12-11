# problem link: https://leetcode.com/problems/implement-queue-using-stacks/description/?envType=study-plan&id=data-structure-i
class MyQueue:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        stack2 = []
        for i in self.stack[::-1]:
            stack2.append(i)
        a = stack2.pop()
        self.stack = []
        for i in stack2[::-1]:
            self.stack.append(i)
        return a

    def peek(self) -> int:
        stack2 = []
        for i in self.stack[::-1]:
            stack2.append(i)
        return stack2[-1]

    def empty(self) -> bool:
        if self.stack:
            return False
        else:
            return True


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
