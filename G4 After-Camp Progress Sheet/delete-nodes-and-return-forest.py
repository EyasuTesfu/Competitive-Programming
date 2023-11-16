# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        to_delete_set = set(to_delete)
        output = []
        if root.val not in to_delete_set:
            output.append(root)
        def dfs(node):
            left = node.left
            right = node.right
            if node.val in to_delete_set:
                if left:
                    if left.val not in to_delete_set:
                        output.append(left)
                    dfs(left)
                if right:
                    if right.val not in to_delete_set:
                        output.append(right)
                    dfs(right)
            else:
                if left:
                    if left.val in to_delete_set:
                        node.left = None
                    dfs(left)
                if right:
                    if right.val in to_delete_set:
                        node.right = None
                    dfs(right)
        dfs(root)
        return output
            
            
