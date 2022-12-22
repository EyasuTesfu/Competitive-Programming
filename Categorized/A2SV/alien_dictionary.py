# problem link: https://leetcode.com/problems/verifying-an-alien-dictionary/description/
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        for i in range(1, len(words)):
            j = 0
            while(j < len(words[i]) and j < len(words[i-1]) and words[i][j] == words[i-1][j]):
                j += 1
            if j < len(words[i]) and j < len(words[i-1]):
                if order.index(words[i][j]) < order.index(words[i-1][j]):
                    return False
            else:
                if len(words[i]) < len(words[i-1]):
                    return False

        return True
