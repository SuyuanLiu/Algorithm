# -*- coding:UTF-8 -*-
'''
Solution: Z字形遍历
- 维护一个队列，先进先出；因为是Z字形，可以维护一个flag，来表示当前层是否顺序是否需要翻转；
- 一层一层遍历，情况类似层序遍历：需要记录每层节点的数量；
    - 可以用len(Q)来记录；
    - 或者维护两个queue；
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        res = []
        Q = [root]
        flag = 1
        while Q:
            level_res = []
            for i in range(len(Q)):
                temp = Q.pop(0)
                level_res.append(temp.val)
                if temp.left:
                    Q.append(temp.left)
                if temp.right:
                    Q.append(temp.right)
            
            if flag == 1:
                res.append(level_res)
                flag = -1
            else:
                res.append(level_res[::-1])
                flag = 1
                
        return res