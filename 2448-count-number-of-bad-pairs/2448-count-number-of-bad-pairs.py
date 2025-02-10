class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        counter = {}
        for i in range(len(nums)):
            if (nums[i] - i not in counter):
                counter[nums[i] - i] = 1
            else:
                counter[nums[i] - i] += 1

        good_pair = 0

        for num in counter:
            if counter[num] > 1:
                good_pair += math.factorial(counter[num]) / (math.factorial(counter[num] - 2)*2)
        if len(nums) > 2:
            total_pair = math.factorial(len(nums)) / (math.factorial(len(nums) - 2) * 2)
        else:
            total_pair = 1
        return int(total_pair-good_pair)

        

