"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        def dfs(node):
            if not node:
                return 0
            depth = 1
            for child in node.children:
                depth = max(depth, 1 + dfs(child))
            return depth
        return dfs(root)