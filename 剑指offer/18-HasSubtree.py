'''
解题思路：
- 转化为判断两棵树是否相同，使用递归；
- 注意子树的定义是属于，不一定要二者都到最后到叶子结点，在isSameTree里面如果pRoot1不为空，但是pRoot2为空时，也要返回True；
- 注意两棵树中可能有多个相同的值
- 注意一定是事先判断这个点是否None，如果None，就没有val属性

时空复杂度：
- 时间复杂度 O(n*m)
- 空间复杂度 O(1)

Test Cases：
- 一棵/两棵树为空
- 有多个相同值的结点
- 一个树只有左子树/右子树
- 普通测试用例

⚠️
跟面试官沟通空树究竟算不算子树
'''
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def isSameTree(self, pRoot1, pRoot2):
        if (not pRoot1 and not pRoot2) or (pRoot1 and not pRoot2):
            return True
        elif (not pRoot1 and pRoot2) or pRoot1.val != pRoot2.val:
            return False
        return self.isSameTree(pRoot1.left, pRoot2.left) and self.isSameTree(pRoot1.right, pRoot2.right)
    
    def HasSubtree(self, pRoot1, pRoot2):
        if not pRoot1 or not pRoot2:
            return False
        
        if self.isSameTree(pRoot1, pRoot2):
            return True
        else:
            return self.HasSubtree(pRoot1.left, pRoot2) or self.HasSubtree(pRoot1.right, pRoot2)
