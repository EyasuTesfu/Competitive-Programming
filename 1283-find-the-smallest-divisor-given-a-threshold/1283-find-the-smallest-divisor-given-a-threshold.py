class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        if threshold == len(nums):
            return max(nums)
        
        # check the validity of the divisor
        def divisor_check(divisor, arr):
            _sum = 0
            for num in arr:
                _sum += math.ceil(num/divisor)
                if _sum > threshold:
                    return False
            return True
            
        # binary search on the valid values
        l = 1
        r = max(nums)
        while l <= r:
            mid = (r+l)//2
            if divisor_check(mid, nums):
                r = mid -1
            else:
                l = mid + 1
        return l