class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        def findAllCases(nums: List[int], p1: int, p2: int, turn):
            if len(nums) == 1:
                if turn == True:
                    p1 += nums[0]
                else:
                    p2 += nums[0]
                if p1 >= p2:
                    return True
                else:
                    return False
            if turn == True:
                return findAllCases(nums[1:], p1+nums[0], p2, False) or findAllCases(nums[:-1], p1+nums[-1], p2, False)
            else:
                return findAllCases(nums[1:], p1, p2+nums[0], True) and findAllCases(nums[:-1], p1, p2+nums[-1], True)
        return findAllCases(nums[1:], nums[0], 0, False) or findAllCases(nums[:-1], nums[-1], 0, False)
            