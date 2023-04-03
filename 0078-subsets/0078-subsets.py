class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # let me do it using bit manipulation
        # an array of bits
        n = len(nums)
        res = []
        # for i in range(2**n,2**(n+1)):
        #     b = bin(i)[3:]
        #     if 
        nth_bit = 1 << n
        for i in range(2**n):
            b = bin(i | nth_bit)[3:]
            res.append([nums[j] for j in range(n) if b[j] == '1'])
        return res