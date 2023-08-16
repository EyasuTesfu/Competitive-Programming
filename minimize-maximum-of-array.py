class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        left = 0
        right = 10**9
        nums.reverse()
        def locate(target):
            count = 0
            for i in nums:
                i += count
                count = 0
                if i >= target:
                    count = i - target
            return count == 0
        while(right > left):
            mid = (right+left)//2
            if locate(mid):
                right = mid
            else:
                left = mid + 1
        return left