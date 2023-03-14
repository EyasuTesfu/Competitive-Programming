class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(start = 0, curr = []):
            res.append(curr)
            
            for i in range(start, len(nums)):
                # go through
                curr.append(nums[i])
                # call the function
                dfs(i + 1, curr[:])
                # backtrack
                curr.pop()
        dfs(0, [])
        return res
                
            
                