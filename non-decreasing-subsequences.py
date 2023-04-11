class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = set()
        def dfs(arr, idx):
            if len(arr) >= 2:
                res.add(tuple(arr))
            for i in range(idx, len(nums)):
                if arr:
                    if nums[i] >= arr[-1]:
                        arr.append(nums[i])
                        dfs(arr[:], i+1)
                else:
                    arr.append(nums[i])
                    dfs(arr[:], i+1)
                arr.pop()
                
        dfs([], 0)
        return list(res)