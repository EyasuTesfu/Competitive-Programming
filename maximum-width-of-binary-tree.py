# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        queue = []
        queue.append((root, 0, 0))
        width = 0
        left = 0
        curr_depth = 0
        for node, pos, depth in queue:
            if node:
                queue.append((node.left, pos*2, depth+1))
                queue.append((node.right, 2*pos+1, depth+1))
                
                if curr_depth != depth:
                    left = pos
                    curr_depth = depth
                width = max(width, pos-left+1)
        return width