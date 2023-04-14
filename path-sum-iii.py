# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        prefix_sum = defaultdict(int)
        prefix_sum[0] = 1
        def dfs(node, _sum):
            count = 0
            if node:
                _sum += node.val
                count = prefix_sum[_sum - targetSum]
                prefix_sum[_sum] += 1
                count += dfs(node.left, _sum) + dfs(node.right, _sum)
                prefix_sum[_sum] -= 1

            return count
        return dfs(root, 0)