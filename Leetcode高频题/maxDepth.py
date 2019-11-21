'''
@lsy 2019.11.21

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Solution 1
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return self.height(root, 0)
        
    def height(self, root, depth):
        if not root:
            return depth
        return max(self.height(root.left, depth), self.height(root.right, depth)) + 1

# more concise
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))