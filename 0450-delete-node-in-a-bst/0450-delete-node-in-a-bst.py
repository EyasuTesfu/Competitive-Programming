# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root == None:
            return
        if root.val == key:
            if not root.left and not root.right:
                return None
            if not root.left:
                return root.right
            
            elif not root.right:
                return root.left
                
            elif root.left and root.right:
                inorder = root.right
                
                if not inorder.left:
                    root.val = inorder.val
                    root.right = inorder.right
                else:
                    fast = inorder.left
                    slow = inorder
                    while fast and fast.left:
                        slow = fast
                        fast = fast.left
                    root.val = fast.val
                    if fast.right:
                        fast.val = fast.right.val
                        fast.left = fast.right.left
                        fast.right = fast.right.right
                    else:
                        slow.left = None
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        return root
                