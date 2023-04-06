class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        # subsets
        res = 0
        or_store = []
        n = len(nums)
        nth_bit = 1 << n
        for i in range(1,2**n):
            _or = 0
            bit = bin(i | nth_bit)[3:]
            for j in range(len(bit)):
                if bit[j] == '1':
                    _or |= nums[j]
            if _or != 0:
                or_store.append(_or)
        
        max_or = 0
        for i in range(len(or_store)):
            if or_store[i] == max_or:
                res += 1
            elif or_store[i] > max_or:
                max_or = or_store[i]
                res = 1
        return res