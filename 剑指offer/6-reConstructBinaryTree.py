'''
解题思路：
前序遍历：根左右，中序遍历：左根右。
通过前序遍历找到根结点，再通过中序遍历划分出左子树和右子树，递归实现。

时空复杂度：
- 时间复杂度 O(n)
- 空间复杂度 O(1)

Test Cases：
- 空树，前序遍历与中序遍历序列不匹配
- 左子树为空/右子树为空
- 正常的例子

⚠️
要询问面试官，数组中是否有重复的数字（如果用重复的数字，要通过判断子树长度来寻找根结点）
'''
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def reConstructBinaryTree(self, pre, tin):
        if not pre or not tin or len(pre) != len(tin): 
            return None
        
        node = TreeNode(pre[0])
        idx = tin.index(pre[0])
        node.left = self.reConstructBinaryTree(pre[1:idx+1], tin[:idx])
        node.right = self.reConstructBinaryTree(pre[idx+1:], tin[idx+1:])
        return node
