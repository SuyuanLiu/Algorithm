# -*- coding:UTF-8 -*-
'''
Solution:
- 直接比较root与val的大小，val比较大就到右边去看，比较小就到左边去看；
- 直到找到一个节点的子节点为空，可以放下val就行了；
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        node = root
        while 1:
            if val > node.val:
                if node.right:
                    node = node.right
                else:
                    node.right = TreeNode(val)
                    return root
            elif val < node.val:
                if node.left:
                    node = node.left
                else:
                    node.left = TreeNode(val)
                    return root
