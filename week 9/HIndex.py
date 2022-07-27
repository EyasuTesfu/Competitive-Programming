'''
Question link = https://leetcode.com/problems/h-index/
Don't really apprecitate this question, it was really hard to understand
Solution: Use binary search to look for the right value in a sorted array and return the 
difference b/n the length of the array and the left most index or the right plus one
The tricky point here is when the value of the h index is not in the array, which means there is a greater value of h index then 
there must be a greater value when finding the difference between length and the part
where left index of becomes greater than the right and the while loop of the
binary search ends
'''


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        left = 0
        n = len(citations)
        right = n - 1
        citations.sort()
        while(left <= right):
            mid = left + ((right - left) // 2)
            if citations[mid] == (n - mid):
                return citations[mid]
            elif citations[mid] > (n - mid):
                right = mid - 1
            else:
                left = mid + 1
        return n-left
