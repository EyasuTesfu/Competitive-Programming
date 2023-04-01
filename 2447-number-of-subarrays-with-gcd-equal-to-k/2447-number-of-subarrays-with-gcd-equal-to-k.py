class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        # check the next num if the GCD of the number is greater than k
        def GCD(a,b):
            if b == 0:
                return a
            return GCD(b, a%b)
        
        res = 0
        for i in range(len(nums)):
            j = i
            prev = GCD(nums[i], nums[j])
            while j < len(nums) and prev >= k:
                if prev == k:
                    res += 1
                j += 1
                if j < len(nums):
                    prev = GCD(nums[j], prev)
        return res