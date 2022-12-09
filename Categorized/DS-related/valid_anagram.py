# problem link: https://leetcode.com/problems/valid-anagram/description/?envType=study-plan&id=data-structure-i
# time complexity: O(n)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
# -------------------using count & any---------------


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
                    return False
                return not(any(s.count(let) != t.count(let) for let in set(s)))