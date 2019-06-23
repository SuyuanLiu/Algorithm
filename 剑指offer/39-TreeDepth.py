'''
解题思路：
Solution 1:
递归遍历

Solution 2:
分治法

时空复杂度：
- 时间复杂度 O(n)
- 空间复杂度 O(1)

Test Cases：
- 普通二叉树，所有结点没有左结点/没有右结点
- 空二叉树，只有一个结点
'''
# Solution 1
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def TreeDepth(self, root):
        # write code here
        if not root:
            return 0
        return 1 + max(self.TreeDepth(root.left), self.TreeDepth(root.right))

# Solution 2
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def TreeDepth(self, root):
        # write code here
        if not root:
            return 0
        left = self.TreeDepth(root.left)
        right = self.TreeDepth(root.right)
        return 1 + max(left, right)
