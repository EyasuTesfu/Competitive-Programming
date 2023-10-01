class WordFilter:

    def __init__(self, words: List[str]):
        self.words = words
        self.trie = [{}, 0, False]
        for i in range(len(words)):
            for j in range(len(words[i])):
                curr = self.trie
                temp_word = words[i][j:] + '{' + words[i]
                for char in temp_word:
                    if char not in curr[0]:
                        curr[0][char] = [{}, i, False]
                    else:
                        curr[0][char][1] = max(curr[0][char][1], i)
                    curr = curr[0][char]
                curr[2] = True
        
    def f(self, pref: str, suff: str) -> int:
        searched_word = suff + "{" + pref
        curr = self.trie
        for char in searched_word:
            if char not in curr[0]:
                return -1
            curr = curr[0][char]
        return curr[1]
        

        return res



            


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)