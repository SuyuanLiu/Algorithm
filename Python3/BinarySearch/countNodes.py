# -*- coding:UTF-8 -*-
'''
Solution:
    - 利用二分思想和完全二叉树的性质(完全二叉树必然是从右侧缺少子树)；
    - 首先遍历根节点左子树的最左边，看左子树的深度depthL，再遍历根节点右子树的最左边，看右子树的深度depthR；
    - 比较depthL和depthR，相等说明左子树是一颗满二叉树，可用2^n - 1计算（n为深度）；递归上述算法，计算右子树节点数；
    - 若depthL > depthR,说明右子树是深度浅一层的满二叉树；递归上述算法，计算左子树节点数；
    - 记得加1，用来加上根节点；
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def treeLeftDepth(self, root):
        depth = 0
        while root:
            depth += 1
            root = root.left
        return depth

    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        nodeNum = 0
        depthL = self.treeLeftDepth(root.left) 
        depthR = self.treeLeftDepth(root.right)
        if depthL == depthR:
            nodeNum = 2 ** depthL - 1 + 1
            return nodeNum + self.countNodes(root.right)
        else:
            nodeNum = 2 ** depthR - 1 + 1
            return nodeNum + self.countNodes(root.left)
        
        