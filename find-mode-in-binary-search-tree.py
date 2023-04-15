# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        mode_dict = defaultdict(int)
        def dfs(node):
            if node:
                mode_dict[node.val] += 1
                dfs(node.left)
                dfs(node.right)

        dfs(root)
        res = []
        _max = max(mode_dict.values())
        for key in mode_dict.keys():
            if mode_dict[key] == _max:
                res.append(key)
   
        return res