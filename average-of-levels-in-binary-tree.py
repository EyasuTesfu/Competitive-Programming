# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        levels = defaultdict(list)
        queue = deque()
        queue.append((root,0))
        while queue:
            node, level = queue.popleft()
            levels[level].append(node.val)

            if node.left:
                queue.append((node.left, level +1))
            if node.right:
                queue.append((node.right, level + 1))

        arr = []
        for level in levels:
            arr.append(sum(levels[level])/len(levels[level]))
        return arr