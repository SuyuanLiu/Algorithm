'''
解题思路：
使用队列，依次访问结点的左右子节点并入队。

时空复杂度：
- 时间复杂度 O(n)
- 空间复杂度 O(n)

Test Cases：
- 空树
- 普通二叉树

'''
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        if not root:
            return []
        res = []
        q = [root]
        while q:
            node = q.pop(0)
            res.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return res
