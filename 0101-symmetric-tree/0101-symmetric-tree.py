# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # perform 2 types of traversal
        # preorder L, R and preorder R, L
        return self.isSymmetric_helper(root.left, root.right)
    def isSymmetric_helper(self,root1, root2):
        if not root1 or not root2:
            return root1 == root2
        if root1.val != root2.val:
            return False
        return self.isSymmetric_helper(root1.right, root2.left) and self.isSymmetric_helper(root1.left, root2.right)