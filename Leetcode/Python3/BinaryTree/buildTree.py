# -*- coding:UTF-8 -*-
'''
Solution:
- 利用递归，分别找到根节点和左右子树
- 前序遍历：根 左 右      中序遍历：左 根 右
- 根据前序遍历，可以确定根，再在中序遍历中找到根，左边的就是左子树，右边就是右子树；
- 在中序遍历中找到根节点后，只要知道左子树节点数即可；
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder:
            return None 
        
        root = TreeNode(preorder[0])
        idx = inorder.index(preorder[0])
        
        root.left = self.buildTree(preorder[1:1+idx], inorder[:idx])
        root.right = self.buildTree(preorder[1+idx:], inorder[idx+1:])
        return root
        
             
            
        
        