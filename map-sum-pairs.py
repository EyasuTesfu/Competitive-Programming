class TrieNode:
    def __init__(self):
        self.children = {}
        self.val = 0

class MapSum:
    def __init__(self):
        self.root = TrieNode()
        self.keys = {}

    def insert(self, key: str, val: int) -> None:
        if key not in self.keys:
            curr = self.root
            self.keys[key] = val
            for char in key:
                if char not in curr.children:
                    curr.children[char] = TrieNode()
                curr = curr.children[char]
                curr.val += val
        else:
            curr = self.root
            for char in key:
                if char not in curr.children:
                    curr.children[char] = TrieNode()
                curr = curr.children[char]
                curr.val += val - self.keys[key]
            self.keys[key] = val
        
    def sum(self, prefix: str) -> int:
        print(self.keys)
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return 0
            curr = curr.children[char]
        return curr.val

        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)