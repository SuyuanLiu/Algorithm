# -*- coding:UTF-8 -*-
'''
Solution 2,3
应该都算是分治法，3的分治法更简洁一点，要学会用分治法。

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# Solution 3
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        # divide
        LDepth = self.maxDepth(root.left)
        RDepth = self.maxDepth(root.right)
        
        # conquer
        depth = max(LDepth, RDepth) + 1
        return depth

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    
# Solution 2
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        return self.traversal(root, 0)        
        
    def traversal(self, root, depth):
        if not root:
            return depth
        
        l = self.traversal(root.left, depth)
        r = self.traversal(root.right, depth)
        
        depth = max(l, r) + 1
        return depth
