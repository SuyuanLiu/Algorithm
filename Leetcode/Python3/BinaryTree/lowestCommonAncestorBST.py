# -*- coding:UTF-8 -*-
'''
Solution:
- 二叉搜索树特点：左子树节点值小于根节点，小于右子树节点值；
- 利用以上特点，判断p,q与当前结点值的大小关系，如果都小于root.val的话，那么LCA一定在左子树；
                                           如果都大于root.val的话，那么LCA一定在右子树；

题目延伸：
如果只是一颗普通的二叉树：题目：https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
                        解法：https://github.com/SuyuanLiu/Leetcode/blob/master/Python3/BinaryTree/lowestCommonAncestor.py                                          
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)      
        
        else:
            return root
        
        