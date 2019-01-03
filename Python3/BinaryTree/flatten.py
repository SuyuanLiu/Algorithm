# -*- coding:UTF-8 -*-
'''
Solution:
- 实际上是前序遍历
- 需要额外定义一个TreeNode指向root
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        
        cur = TreeNode(0)
        s = [root]
        while s:
            node = s.pop()
            cur.left = None
            cur.right = node
            cur = cur.right
            
            if node.right:
                s.append(node.right)
            if node.left:
                s.append(node.left)


            