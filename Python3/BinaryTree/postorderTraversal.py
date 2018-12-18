# -*- coding:UTF-8 -*-
'''
Solution: 后序遍历
- 后序遍历的顺序： 左 右 根

Solution 1
- 定义一个栈，定义pre,cur，分别表示当前访问节点与上一次访问节点；
- 保证根节点在孩子节点访问后才能访问，因此对任意节点先将其入栈。以下两种情况可以访问这个根节点：
    - 如果cur没有左右孩子，可以直接访问这个节点；
    - 或者pre是cur的左/右孩子，说明上次已经访问过了cur的孩子结点，这次到根节点了，可以直接输出；
- 剩余的情况，就把cur节点的右孩子、左孩子分别入栈；（因为每次取栈顶元素，保证左孩子先被访问）

Solution 2
- 
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        
        pre, cur = None, None
        res, stack = [], []
        
        stack.append(root)
        while stack:
            cur = stack.pop()
            if (not cur.left and not cur.right) or (pre and (pre == cur.left or pre == cur.right)):
                res.append(cur.val)
                pre = cur
            else:
                stack.append(cur)
                if cur.right:
                    stack.append(cur.right)
                if cur.left:
                    stack.append(cur.left)
        return res
            
        
        
        