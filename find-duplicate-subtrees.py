# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        val_str = defaultdict(int)
        res = []
        def dfs(node):
            if not node:
                return ''
            left = node.left
            right = node.right
            the_node = str(node.val) + "/" + dfs(node.left) + "/" + dfs(node.right)
            val_str[the_node] += 1
            if val_str[the_node] == 2:
                res.append(node)
            return the_node
        dfs(root)
        return res