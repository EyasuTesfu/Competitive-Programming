class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        word1, word2, ans = list(word1), list(word2), []
        while(word1 and word2):
            ans.append(word1.pop(0) if word1 > word2 else word2.pop(0))
        return ''.join(ans) + ''.join(word1) + ''.join(word2)