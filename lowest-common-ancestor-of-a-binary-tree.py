# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parent = {}
        def dfs(node):
            if not node:
                return
            if node.left:
                parent[node.left] = node
            if node.right:
                parent[node.right] = node
            dfs(node.left)
            dfs(node.right)
        num1_parents = []
        num2_parents = set()
        def collect_path(node, is_num1):
            if node == root:
                num1_parents.append(node)
                num2_parents.add(node)
                return
            if not node:
                return
            if is_num1:
                if node in parent:
                    num1_parents.append(parent[node])
                    collect_path(parent[node], True)
            else:
                if node in parent:
                    num2_parents.add(parent[node])
                    collect_path(parent[node], False)
        dfs(root)
        collect_path(p, True)
        collect_path(q, False)
        num1_parents.insert(0, p)
        num2_parents.add(q)
        for i in range(len(num1_parents)):
            if num1_parents[i] in num2_parents:
                return num1_parents[i]