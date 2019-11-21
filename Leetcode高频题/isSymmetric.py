'''
@lsy 2019.11.21
递归。
判断 左子树的left == 右子树的right ?
     左子树的right == 右子树的left ?
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.helper(root.left, root.right)
        
    def helper(self, left, right):
        if not left and not right:
            return True
        if (left and not right) or (not left and right) or (left.val != right.val):
            return False
        return self.helper(left.left, right.right) and self.helper(left.right, right.left)