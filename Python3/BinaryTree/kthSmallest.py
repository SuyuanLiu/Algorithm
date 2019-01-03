# -*- coding:UTF-8 -*-
'''
Solution：
- 二叉搜索树：是指左结点的值 < 根节点 < 右节点，所以二叉搜索树的中序遍历是一个有序数组；

Solution 1：
- 根据以上思路，可以直接对二叉搜索树进行中序遍历，把遍历结果放在数组中，找到第k个即可；

Solution 2：
- 对Solution 1优化，不需要保存遍历结果，也不需要遍历整个二叉树，在遍历过程中对K--,判断当前已经遍历了几个，找到第K个就输出并停止遍历。
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Solution 1
class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        res = []
        S = []
        node = root
        while S or node:
            while node:
                S.append(node)
                node = node.left
            node = S.pop()
            res.append(node.val)
            node = node.right
                
        return res[k-1]
        


# Solution 2
class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        S = []
        node = root
        while S or node:
            while node:
                S.append(node)
                node = node.left
            node = S.pop()
            k -= 1
            if k == 0:
                return node.val
            node = node.right
            
        
        