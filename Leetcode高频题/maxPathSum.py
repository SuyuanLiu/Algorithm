'''
@lsy 2019.11.26

定义函数maxToRoot，计算的是从任意node开始，以root为结尾最大的和；
self.max_sum及时更新结果。
在计算left，right时，与0作比较，负数则不取。

看自己以前提交的代码中，有用到另一种方法。（之后再看）
还是感觉下面这个方法更容易明白一点。
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.max_sum = -float('inf')
        
    def maxPathSum(self, root: TreeNode) -> int:
        self.maxToRoot(root)
        return self.max_sum
        
    def maxToRoot(self, root):
        if not root:
            return 0
        left = max(0, self.maxToRoot(root.left))
        right = max(0, self.maxToRoot(root.right))
        self.max_sum = max(self.max_sum, root.val + left + right)
        
        return root.val + max(left, right)
             