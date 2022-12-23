# prolem link: https://leetcode.com/problems/merge-strings-alternately/description/
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        output = []
        n = min(len(word1), len(word2))
        for i in range(n):
            output.append(word1[i])
            output.append(word2[i])
        if n < len(word1):
            output.append("".join(word1[n:]))
        if n < len(word2):
            output.append("".join(word2[n:]))
        return "".join(output)
