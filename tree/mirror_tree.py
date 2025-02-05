#User function Template for python3
# Helper function to print level order traversal
from collections import deque


'''
class Node:
    def _init_(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
# your task is to complete this function

class Solution:
    #Function to convert a binary tree into its mirror tree.
    def mirror(self, root):
        # Code here
        if root is None:
            return None
        # Swap left and right children
        root.left, root.right = root.right, root.left
        # Recursively call for left and right subtrees
        self.mirror(root.left)
        self.mirror(root.right)
        return root

    def levelOrderTraversal(root):
        if not root:
            return []
        queue = deque([root])
        result = []
        while queue:
            node = queue.popleft()
            result.append(node.val if node else "N")
            if node:
                queue.append(node.left)
                queue.append(node.right)
        # Remove trailing "N" values (null nodes) for clean output
        while result and result[-1] == "N":
            result.pop()
        return result
