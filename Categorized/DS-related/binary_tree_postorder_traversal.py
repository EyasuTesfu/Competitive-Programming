# problem link:https://leetcode.com/problems/binary-tree-postorder-traversal/description/
# -------------------------Iterative Solution-------------------
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        # return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]
        stack = [root]
        output = []
        while(stack):
            root = stack.pop()
            output.insert(0, root.val)
            if root.left:
                stack.append(root.left)
            if root.right:
                stack.append(root.right)
        return output
# -------------------------Recursive ---------------------------


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]
