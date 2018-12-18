# -*- coding:UTF-8 -*-
'''
Solution：前序遍历
- 前序遍历顺序：根，左，右
- 利用一个栈（先进后出），把根节点先放进去，
    - 然后弹出根节点，再放根节点的右节点，然后是左节点；
    - 下次再弹出左节点，然后再放它的右节点，左节点； 
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
        
        
        
        