# -*- coding:UTF-8 -*-
'''
Solution：前序遍历
- 前序遍历顺序：根，左，右

- 利用一个栈（先进后出）
- 弹出栈顶元素，依次把栈顶元素的右孩子、左孩子入栈；
- 注意左孩子后入栈，这样可以保证下次访问时左孩子先被访问； 
'''
# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        
        res, stack = [], []
        stack.append(root)
        while(stack):
            temp = stack.pop()
            res.append(temp.val)
            if temp.right:
                stack.append(temp.right)
            if temp.left:
                stack.append(temp.left)
        return res
        
        
        
        