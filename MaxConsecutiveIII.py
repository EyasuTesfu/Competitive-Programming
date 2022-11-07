class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = -1
        right = 0
        length = 0
        flipped = k
        while(right < len(nums)):
            if nums[right] == 0: flipped -= 1
            if flipped < 0:
                while(flipped < 0):
                    left += 1
                    if nums[left] == 0:
                        flipped += 1
            length = max(length, right - left)
            right += 1
        return length