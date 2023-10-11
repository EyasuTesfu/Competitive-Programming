# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        res = []
        def dfs(node, _sum, path):
            if not node:
                if _sum == targetSum:
                    res.append(path)
                    return
                return
            if node.left and node.right:
                dfs(node.left, _sum + node.val, path + [node.val])
                dfs(node.right, _sum + node.val, path + [node.val])
            elif node.left:
                dfs(node.left, _sum + node.val, path + [node.val])
            else:
                dfs(node.right, _sum + node.val, path + [node.val])
        dfs(root, 0, [])
        return res