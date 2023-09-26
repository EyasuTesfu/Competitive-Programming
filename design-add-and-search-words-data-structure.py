class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.is_end_of_word = True
        

    def search(self, word: str) -> bool:
        def dfs(node, ind):
            if ind == len(word):
                return node.is_end_of_word
            if word[ind] == ".":
                for child in node.children:
                    if dfs(node.children[child], ind+1):
                        return True
                return False
            
            if word[ind] not in node.children:
                return False

            return dfs(node.children[word[ind]], ind + 1)
        return dfs(self.root, 0)
    
        
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)