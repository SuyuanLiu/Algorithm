# -*- coding:UTF-8 -*-
'''
Solution:
- 应该是分治吧
- 分为三种情况，root.val == key, 特殊情况
              root.val > key, 在root右侧删除节点, root.right = self.deleteNode(root.right, key)
              root.val < key, 在root左侧删除节点, root.left = self.deleteNode(root.left, key)
- 当root.val== key，如果left为空，直接返回右子树；如果右子树为空，直接返回左子树；
  都不为空时，找到左子树的最大值，代替root这里的val，然后再在左子树中删除刚刚找到的最大值，root.left = self.deleteNode(root.left, node.val)。
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None
        
        if root.val == key:
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            node = self.findMaxFromLeft(root)
            root.val = node.val
            root.left = self.deleteNode(root.left, node.val)
            
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)
        return root
            
    
    def findMaxFromLeft(self, root):
        node = root.left
        while node.right:
            node = node.right
        return node    
