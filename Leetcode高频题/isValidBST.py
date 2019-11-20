'''
@lsy 2019.11.20

注意：BST要满足左子树所有的值都要小于根结点；右子树所有的值都要大于根结点。

Solution 1:
使用递归，分别记录对于当前节点，所出现的最大/小的节点值。

Solution 2: TODO
中序遍历中进行判断。
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
        return self.helper(root, -float("inf"), float("inf"))

    def helper(self, root, minVal, maxVal):
        if not root:
            return True
        if root.val <= minVal or root.val >= maxVal:
            return False
        return self.helper(root.left, minVal, root.val) and self.helper(
            root.right, root.val, maxVal)
