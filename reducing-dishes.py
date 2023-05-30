class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        sat = sorted(satisfaction)
        satisfy = 0
        max_satisfy = 0
        i = len(sat)-1
        while i > -1 and satisfy + sat[i] > 0:
            satisfy += sat[i]
            max_satisfy += satisfy
            i -= 1
        return max_satisfy