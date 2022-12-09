# problem link: https://leetcode.com/problems/first-unique-character-in-a-string/description/?envType=study-plan&id=data-structure-i
# time complexity: O(n)
class Solution:
    def firstUniqChar(self, s: str) -> int:
        s_dict = Counter(s)
        for i in range(len(s)):
            if s_dict[s[i]] == 1:
                return i
        return -1
