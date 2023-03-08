# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque()
        queue.append(root)
        res = []
        while queue:
            level_node = []
            i = 0
            while queue:
                level_node.append(queue.popleft())
            res.append([])
            for i in range(len(level_node)):
                res[-1].append(level_node[i].val)
                if level_node[i].left:
                    queue.append(level_node[i].left)
                if level_node[i].right:
                    queue.append(level_node[i].right)
        return res
                