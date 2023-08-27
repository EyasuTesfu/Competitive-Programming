# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = []
        def dfs(node):
            if not node:
                return 0
            if node.left:
                left = dfs(node.left)
            else:
                left = -1001
            if node.right:
                right = dfs(node.right)
            else:
                right = -1001
            max_sum = max(left + node.val, right + node.val, node.val)
            max_left_right = left + right + node.val
            res.append(max_left_right)
            res.append(left)
            res.append(right)
            return max_sum
        _max = dfs(root)
        return max(max(res), _max)