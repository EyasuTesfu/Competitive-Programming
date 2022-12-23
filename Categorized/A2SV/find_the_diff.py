# problem link: https://leetcode.com/problems/find-the-difference/description/
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        if s == "":
            return t
        s_counter = Counter(s)
        for i in t:
            if s_counter.get(i, 0) == 0:
                return i
            else:
                s_counter[i] -= 1
