# problem link: https://leetcode.com/problems/binary-tree-inorder-traversal/description/?envType=study-plan&id=data-structure-i
# time complexity: O(n)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# -------------------------Iterative Solution------------------
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        stack = []
        output = []
        # return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
        while(root or stack):
            while(root):
                stack.append(root)
                root = root.left
            root = stack.pop()
            output.append(root.val)
            root = root.right
        return output
# -----------------------recursive-----------------------
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)