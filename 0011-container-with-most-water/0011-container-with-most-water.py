class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height) == 2:
            return min(height[0], height[1])
        l = 0
        r = len(height) - 1
        most_water = 0
        while(l != r):
            area = (r-l) * (min(height[r], height[l]))
            most_water = max(most_water, area)
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return most_water