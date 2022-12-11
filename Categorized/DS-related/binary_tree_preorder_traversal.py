# problem link: https://leetcode.com/problems/binary-tree-preorder-traversal/description/?envType=study-plan&id=data-structure-i
# time-complexity: O(nm)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# -----------------my naive approach-------------
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return root
        output = [root.val]
        return self.preorderTraversalDFS(root, output)

    def preorderTraversalDFS(self, root, output=[]):
        if root.left:
            output.append(root.left.val)
            root.left = self.preorderTraversalDFS(root.left, output)
        if root.right:
            output.append(root.right.val)
            root.right = self.preorderTraversalDFS(root.right, output)
        return output
# ------------------------Easy Answer--------------


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
# -------------------------Iterative Solution--------------------------


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return
        output = []
        stack = []
        while(root or stack):
            while(root):
                output.append(root.val)
                stack.append(root)
                root = root.left
            root = stack.pop()
            root = root.right
        return output
