class TrieNode:
    def __init__(self):
        self.count = 1
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            else:
                curr.children[char].count += 1
            curr = curr.children[char]
    
    def search_count(self, word):
        curr = self.root
        count = 0
        for char in word:
            count += curr.children[char].count
            curr = curr.children[char]
        return count
        
class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:

        trie = Trie()
        for word in words:
            trie.insert(word)
        res = []
        for word in words:
            res.append(trie.search_count(word))
        return res