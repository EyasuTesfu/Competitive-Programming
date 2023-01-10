class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        res = []
        i = j = 0
        while(len(res) != len(nums)):
            while(i < len(nums)):
                if nums[i] > 0:
                    res.append(nums[i])
                    i += 1
                    break
                i += 1
            while(j < len(nums)):
                if nums[j] < 0:
                    res.append(nums[j])
                    j += 1
                    break
                j += 1
        return res
            