# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parent = defaultdict()
        queue = deque()
        queue.append(root)
        initial = root
        while queue:
            node = queue.popleft()
            if node.val == target.val:
                initial = node
                break
            # have the child to parent mapping
            if node.left:
                left = node.left
                parent[left] = node
                queue.append(left)
            if node.right:
                right = node.right
                parent[right] = node
                queue.append(right)

        queue = deque()
        queue.append((initial, 0))
        vis = set()
        vis.add(initial)
        res = []
        while queue:
            node, dist = queue.popleft()
            if dist == k:
                res.append(node.val)
            if dist >= k:
                continue
            if node in parent:
                if parent[node] not in vis:
                    queue.append((parent[node], dist+1))
                    vis.add(node)
            if node.left:
                if node.left not in vis:
                    queue.append((node.left, dist + 1))
                    vis.add(node)
            if node.right:
                if node.right not in vis:
                    queue.append((node.right, dist + 1))
                    vis.add(node)
        return res