# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        # Initialize an empty list to store serialized node values
        ans = []

        # Define a depth-first search (DFS) function to serialize the tree
        def DFS(root):
            # Base case: If the current node is None, append "N" to represent null node
            if not root:
                ans.append("N")
                return

            # Append the value of the current node to the list
            ans.append(str(root.val))
            
            # Recursively serialize left and right subtrees
            DFS(root.left)
            DFS(root.right)

        # Call the DFS function to serialize the tree
        DFS(root)
        
        # Join the list elements into a string separated by commas and return
        return ",".join(ans)        

    def deserialize(self, data):
        # Split the serialized string into a list of node values
        value = data.split(",")
        
        # Initialize index to keep track of current position in the list
        self.index = 0

        # Define a DFS function to reconstruct the tree from serialized data
        def DFS():
            # If the current value is "N", indicating a null node, return None
            if value[self.index] == "N":
                self.index += 1
                return None

            # Create a new TreeNode with the current value
            root = TreeNode(int(value[self.index]))
            self.index += 1
            
            # Recursively construct left and right subtrees
            root.left = DFS()
            root.right = DFS()
            
            return root

        # Call the DFS function to deserialize the tree and return the root
        return DFS()                               
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))