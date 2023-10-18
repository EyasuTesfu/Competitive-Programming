# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, _min, _max):
            if not root:
                return True
            if _min < root.val < _max:
                return dfs(root.left, _min, root.val) and dfs(root.right, root.val, _max)
        return dfs(root, float('-inf'), float('inf'))