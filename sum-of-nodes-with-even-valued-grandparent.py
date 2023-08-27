# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        res = []
        def dfs(node, parent, grandparent):
            if not node:
                return
            if grandparent % 2 == 0:
                _sum = node.val
                res.append(_sum)
            
            dfs(node.left, node.val, parent)
            dfs(node.right, node.val, parent)
        dfs(root, -1, -1)
        return sum(res)