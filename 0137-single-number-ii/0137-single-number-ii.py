class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones = 0
        twos = 0
        for num in nums:
            ones = (ones ^ num)
            ones = ones & ~twos
            twos = twos ^ num
            twos = twos & ~ones
        if ones != 0:
            return ones
        else:
            return twos