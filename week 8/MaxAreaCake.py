
'''
Question link = https://leetcode.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts/
This is an easy question but sorting involves Timsort algorithm which is the combination of insertion sort and merge sort,
This made the algorithm faster and avoided the time limit exceeded test case,
But the insertion sort algorithm is at the under the code'''
from typing import List


class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        max_width = 0
        max_height = 0
        horizontalCuts.append(0)
        verticalCuts.append(0)
        horizontalCuts.sort()
        verticalCuts.sort()
        max_width = w - verticalCuts[0]
        max_height = h - horizontalCuts[0]
        for i in range(1, len(horizontalCuts)):
            max_height = max(
                max_height, horizontalCuts[i-1] - horizontalCuts[i])
        for i in range(1, len(verticalCuts)):
            max_width = max(max_width, verticalCuts[i-1] - verticalCuts[i])
        return (max_height * max_width) % (10**9 + 7)


'''
for i in range(1, len(horizontalCuts)):
    temp = horizontalCuts[i]
    j = i - 1
    while(j >= 0 and horizontalCuts[j] < temp):
        horizontalCuts[j + 1] = horizontalCuts[j]
        j -= 1
    horizontalCuts[j + 1] = temp
for i in range(1, len(verticalCuts)):
    temp = verticalCuts[i]
    j = i - 1
    while(j >= 0 and verticalCuts[j] < temp):
        verticalCuts[j + 1] = verticalCuts[j]
        j -= 1
    verticalCuts[j + 1] = temp
'''
