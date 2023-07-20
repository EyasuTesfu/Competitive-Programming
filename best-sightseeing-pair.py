class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        # look for the sub problem and find a relationship that works
        cur = 0
        max_val = 1
        for i in range(1, len(values)):
            cur = max(cur, values[i-1]+i-1)
            max_val = max(max_val, cur + values[i] - i)
        return max_val