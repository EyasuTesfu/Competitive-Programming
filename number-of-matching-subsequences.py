class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        self.count = 0

class Solution:
    def __init__(self):
        self.root = TrieNode()
        self.count = 0


    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        for word in words:
            self.insert(word)
        def dfs(node, index):
            for char in node.children:
                child = node.children[char]
                ind = -1
                for i in range(index, len(s)):
                    if s[i] == char:
                        ind = i
                        break
                if ind != -1:
                    self.count += child.count
                    dfs(child, ind+1)

        dfs(self.root, 0)
        return self.count
        
    def insert(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.is_end_of_word = True
        curr.count += 1