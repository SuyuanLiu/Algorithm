# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def isLeaf(self, root):
        if not root.left and not root.right:
            return True
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

s = Solution()
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(12)
root.left.left = TreeNode(4)
root.left.right = TreeNode(7)
print(s.FindPath(root, 22))
