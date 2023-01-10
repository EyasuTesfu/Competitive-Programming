class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        nums_dict = {}
        for i in range(len(nums)):
            nums_dict[nums[i]] = i
        for i in range(len(operations)):
            index = nums_dict[operations[i][0]]
            nums[nums_dict[operations[i][0]]] = operations[i][1]
            del nums_dict[operations[i][0]]
            nums_dict[operations[i][1]] = index
        return nums
        