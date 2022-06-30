'''
Question link = https://leetcode.com/problems/design-circular-deque/
'''


class MyCircularDeque:

    def __init__(self, k: int):
        self.size = k
        self.queue = [None for i in range(k)]
        self.front = -1
        self.rear = -1

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.isEmpty():
            self.front = 0
            self.rear = 0
            self.queue[0] = value
        elif self.front == 0:
            self.front = self.size-1
            self.queue[self.front] = value
        else:
            self.front = self.front - 1
            self.queue[self.front] = value
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.isEmpty():
            self.front = 0
            self.rear = 0
            self.queue[0] = value
        else:
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = value
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        elif (self.front == self.rear):
            self.queue[self.front] = None
            self.front = -1
            self.rear = -1

        elif self.front == self.size - 1:
            self.queue[self.front] = None
            self.front = 0
        else:
            self.queue[self.front] = None
            self.front = self.front + 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        elif self.front == self.rear:
            self.queue[self.rear] = None
            self.front = -1
            self.rear = -1
        elif self.rear == 0:
            self.queue[self.rear] = None
            self.rear = self.size - 1
        else:
            self.queue[self.rear] = None
            self.rear = self.rear - 1
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return self.front
        return self.queue[self.front]

    def getRear(self) -> int:
        if self.isEmpty():
            return self.rear
        return self.queue[self.rear]

    def isEmpty(self) -> bool:
        return (self.front == -1)

    def isFull(self) -> bool:
        return ((self.front == 0 and self.rear == self.size - 1) or (self.front == self.rear + 1))


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
