class RandomizedSet:

    def __init__(self):
        self.my_dict = {}
        self.my_list = []

    def insert(self, val: int) -> bool:
        if val in self.my_dict:
            return False
        self.my_dict[val] = len(self.my_list)
        self.my_list.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.my_dict:
            return False
        ind = self.my_dict[val]
        n = len(self.my_list)-1
        new_num = self.my_list[n]
        self.my_list[ind], self.my_list[n] = self.my_list[n], self.my_list[ind]
        self.my_dict[new_num] = ind
        self.my_list.pop()
        del self.my_dict[val]
        return True
        

    def getRandom(self) -> int:
        return random.choices(self.my_list)[0]



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()