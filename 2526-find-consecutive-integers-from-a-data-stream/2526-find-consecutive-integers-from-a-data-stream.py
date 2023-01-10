class DataStream:

    def __init__(self, value: int, k: int):
        self.stream = [value, k]
        self.holder = []

    def consec(self, num: int) -> bool:
        if num == self.stream[0]:
            self.holder.append(num)
            if len(self.holder) == self.stream[1]:
                return True
            elif len(self.holder) > self.stream[1]:
                self.holder.pop(0)
                return True
            else:
                return False
        else:
            self.holder = []
            return False

# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)