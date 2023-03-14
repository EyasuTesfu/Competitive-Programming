class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def cascade(arr, idx):
            if idx == len(nums):
                return arr
            
            new_arr = []
            for i in range(2**idx):
                new_arr.append(arr[i]+[nums[idx]])
            
            return cascade(arr+new_arr, idx + 1)
        return cascade([[]], 0)
                