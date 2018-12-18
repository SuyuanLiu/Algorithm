# -*- coding:UTF-8 -*-
'''
Solution: 中序遍历
- 中序遍历顺序： 左 根 右

Solution 1
- 定义一个栈，把root压入，遍历所有左孩子，压入左孩子；
    - 再依次弹出，看是否有右孩子，有的话，再重复前面的操作，把它的左孩子全放进去；
    - 没有右节点的话，就接着弹出栈的内容；

Solution 2
- 高票答案的一个简化版，更清晰一点；
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        
        res, stack = [], []
        stack.append(root)
        
        while(stack):
            temp = stack[-1]
            while temp.left:
                stack.append(temp.left)
                temp = temp.left
            
            temp = stack.pop()
            res.append(temp.val)  
            
            while not temp.right and stack:
                temp = stack.pop()
                res.append(temp.val)
            if temp.right:
                stack.append(temp.right)
            
        return res



# Solution2: 简化一点的
class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        
        res, stack = [], []
        p = root
        while p or stack:
            while p:
                stack.append(p)
                p = p.left
            if stack:
                temp = stack.pop()
                res.append(temp.val)
                p = temp.right
        return res
