# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.memo = {}
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0
            if not node.left and node.right:
                return max(dfs(node.right), dfs(node.right.left) + dfs(node.right.right) + node.val)
            if not node.right and node.left:
                return max(dfs(node.left), dfs(node.left.left) + dfs(node.left.right) + node.val)
            
            if not node.right and not node.left:
                return node.val
            if node not in self.memo:
                self.memo[node] = max(dfs(node.left) + dfs(node.right), dfs(node.left.left) + dfs(node.left.right) + dfs(node.right.left) + dfs(node.right.right) + node.val)
            return self.memo[node]
        return dfs(root)