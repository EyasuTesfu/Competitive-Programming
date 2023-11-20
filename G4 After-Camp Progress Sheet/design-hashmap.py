class MyHashMap:

    def __init__(self):
        self.array = [0]*(10**7)
        self.my_set = set()

    def put(self, key: int, value: int) -> None:
        self.array[key] = value
        self.my_set.add(key)

    def get(self, key: int) -> int:
        if key in self.my_set:
            return self.array[key]
        
        return -1

    def remove(self, key: int) -> None:
        if key in self.my_set:
            self.my_set.remove(key)
        
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)