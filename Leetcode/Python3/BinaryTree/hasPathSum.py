# -*- coding:UTF-8 -*-
'''
Solution:
- 利用递归
- 注意：找到等于Sum的路径，还要判断当前结点是否为叶子节点（即：没有子结点）
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        
        if root.val == sum and not root.left and not root.right:
            return True
        
        sum = sum - root.val
        temp = self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)
        
        return temp
        