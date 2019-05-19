'''
解题思路：
- dfs
- 用path保存走过的路径，回溯时要弹出path最后一个结点。

Test Cases：
- 空树
- 没有符合条件的路径
- 有一条/多条符合条件路径
'''
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def isLeaf(self, root):
        if not root.left and not root.right:
            return Truee
        return False
    
    def dfs(self, root, expect, path, res):
        if root.val == expect and self.isLeaf(root):
            path.append(root.val)
            res.append([n for n in path])
            return res
            
        if root.left:
            res = self.dfs(root.left, expect-root.val, path+[root.val], res)
        if root.right:
            res = self.dfs(root.right, expect-root.val, path+[root.val], res)
        return res
    
    def FindPath(self, root, expectNumber):
        # write code here
        res = []
        if not root:
            return []
        return self.dfs(root, expectNumber, [], res)
