class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        n = len(satisfaction)
        sat = sorted(satisfaction, reverse = True)
        def dp(i, _sum, max_sum):
            if _sum < 0 or i == n:
                return max_sum
            _sum += sat[i]
            if _sum < 0:
                return max_sum
            max_sum += _sum
            return dp(i+1, _sum, max_sum)
        return dp(0, 0, 0)