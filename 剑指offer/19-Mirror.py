'''
解题思路：
直接遍历每一个结点即可，把当前结点的左右结点进行交换。

时空复杂度：
- 时间复杂度 O(n)
- 空间复杂度 O(1)

Test Cases：
- 空树
- 只有左子结点，只有右子结点
- 普通二叉树
'''
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        if not root:
            return 
        tmp = root.left
        root.left = root.right
        root.right = tmp
        
        root.left = self.Mirror(root.left)
        root.right = self.Mirror(root.right)
        
        return root
