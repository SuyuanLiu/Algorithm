# -*- coding:UTF-8 -*-
'''
Solution:
- 递归判断左边值是否等于右边的值
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isEqual(self, left, right):
        if (not left and right) or (left and not right):
            return False
        if not left and not right:
            return True
        return (left.val == right.val) and self.isEqual(left.left, right.right) and self.isEqual(left.right, right.left)
    
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        
        return self.isEqual(root.left, root.right)
        