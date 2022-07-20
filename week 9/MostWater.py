'''
Question link = https://leetcode.com/problems/container-with-most-water/
area = distance(index_difference) * minimum height
move right and left pointer based on which one is greater
because the greater one will give a greater or equal area to the previous one
but if we move one it will get even lower and we might not 
get our potential area'''


from typing import List


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
