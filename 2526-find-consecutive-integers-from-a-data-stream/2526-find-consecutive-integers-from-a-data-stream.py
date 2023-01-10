class DataStream:

    def __init__(self, value: int, k: int):
        self.stream = [value, k]
        self.count = 0

    def consec(self, num: int) -> bool:
        if num == self.stream[0]:
            self.count += 1
            if self.count == self.stream[1]:
                self.count -= 1
                return True
            else:
                return False
        else:
            self.count = 0
            return False

# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)