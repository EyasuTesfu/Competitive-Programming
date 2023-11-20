# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            left = node.left
            right = node.right
            _sum = 0
            if left:
                if not left.left and not left.right:
                    _sum += left.val
                else:
                    _sum += dfs(left)
            if right:
                _sum += dfs(right)
            
            return _sum
        return dfs(root)
                    