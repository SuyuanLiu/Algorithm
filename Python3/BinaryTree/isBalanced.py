# -*- coding:UTF-8 -*-
'''
Solution:

时间复杂度：O（n）

- 平衡二叉树：所有左右子树的高度相差不超过1
- 分别求出左右子树的高度，判断相差是否超过1；再分别判断左右子树是否平衡；（Solution 1）
- 或者在求二叉树高度里面进行判断左右子树是否平衡，不平衡的话，直接传递一个-1，表示不平衡。（Solution 2，分治法）
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Solution 2
class Solution:
    def depth(self, root):
        if not root:
            return 0
            
        # divide 
        LDepth = self.depth(root.left)
        RDepth = self.depth(root.right)
        # conquer
        if LDepth == -1 or RDepth == -1 or abs(LDepth - RDepth) > 1:
            return -1
        return max(LDepth, RDepth) + 1
        
    
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.depth(root) != -1




# Solution 1
class Solution:
    def depth(self, root):
        if not root:
            return 0
        return 1 + max(self.depth(root.left), self.depth(root.right))
    
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        
        left_depth = self.depth(root.left)
        right_depth = self.depth(root.right)
        
        return abs(left_depth - right_depth) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)
