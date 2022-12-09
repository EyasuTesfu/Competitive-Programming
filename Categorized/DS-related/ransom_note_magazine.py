# problem link: https://leetcode.com/problems/ransom-note/?envType=study-plan&id=data-structure-i
# time complexity: O(n), nice code at the last
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rans_counter = Counter(ransomNote)
        mag_counter = Counter(magazine)
        for i in rans_counter.keys():
            if i not in mag_counter.keys() or rans_counter[i] > mag_counter[i]:
                return False
        return True
# -------------2nd solution--------------


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        return not(any(ransomNote.count(let) > magazine.count(let) for let in set(ransomNote)))
