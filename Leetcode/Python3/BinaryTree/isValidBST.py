# -*- coding:UTF-8 -*-
'''
Solution 1:
- 利用BST的中序遍历是升序序列；
- 对这棵树做中序遍历，然后检查中序遍历的结果是否为升序序列

Solution 2:(TODO)
- 根据定义，使用分治法
- 要使得左右子树都为BST，同时左子树的最大值要小于root，右子树的最小值要大于root，这就要在这过程中去记录对应的min，max；
- 感觉比较复杂
'''

# Solution 1
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        inOrder, s = [], []
        node = root
        
        while s or node:
            while node:
                s.append(node)
                node = node.left
            node = s.pop()
            inOrder.append(node.val)
            node = node.right
            
        for i in range(1, len(inOrder)):
            if inOrder[i-1] >= inOrder[i]:
                return False
            
        return True
