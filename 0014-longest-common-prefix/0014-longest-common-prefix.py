class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        word = strs[0]
        for i in range(1, len(strs)):
            j = 0
            while(j < len(strs[i]) and j < len(word) and strs[i][j] == word[j]):
                j += 1
            word = strs[i][:j]
        return word
                