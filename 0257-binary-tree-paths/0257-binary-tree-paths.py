# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        arr = []
        def dfs(root, path = []):
            path.append(str(root.val))
            if not root.left and not root.right:
                arr.append("->".join(path))
                return
            
            if root.left:
                dfs(root.left, path)
                path.pop()
            if root.right:
                dfs(root.right, path)
                path.pop()
        dfs(root, [])
        return arr