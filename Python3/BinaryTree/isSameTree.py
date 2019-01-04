# -*- coding:UTF-8 -*-
'''
Solution:
- 注意使用 p == q无法判断这两个节点是否相同，即使他们val相同，left，right都相同，使用p==q还是判为FALSE；
- 要用.val来判断，再分别对其左右的val判断
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not(p and q):   # 说明p,q中至少有一个为None
            return p == q
        
        if p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    
        return False
        