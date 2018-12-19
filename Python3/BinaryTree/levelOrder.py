# -*- coding:UTF-8 -*-
'''
Solution：层序遍历
- 使用一个队列，先进先出；
- 由于要一层一层的输出，需要知道每层有几个节点：
    - 可以用len(queue)来判断当前层的节点数；(Solution 1)
    - 或者维护两个队列，当前队列里的子节点全部放到另一个队列；(Solution 2)
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Solution 1
class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        res = []
        Q = [root]
        
        while Q:
            level_res = []
            for i in range(len(Q)):
                temp = Q.pop(0)
                level_res.append(temp.val)
                if temp.left:
                    Q.append(temp.left)
                if temp.right:
                    Q.append(temp.right)
            res.append(level_res)
        
        return res
        

# Solution 2
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        res = []
        Q = [root]
        
        while Q:
            level_res = []
            sub_Q = []
            
            while Q:
                temp = Q.pop(0)
                level_res.append(temp.val)
                if temp.left:
                    sub_Q.append(temp.left)
                if temp.right:
                    sub_Q.append(temp.right)
                    
            res.append(level_res)
            Q = sub_Q
            
        return res
                    