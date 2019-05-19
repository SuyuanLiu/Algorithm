'''
解题思路：
- 二叉搜索树：左子树结点 < 根结点 < 右子树结点； 
  后序遍历：左 右 根
- 根据根结点（数组最后一个值），找出左子树和右子树（比根结点小的部分为左子树），然后判断右子树的值是不是都大于根结点；
  递归判断左右子树是不是二叉搜索树

时空复杂度：
- 时间复杂度 O(n)
- 空间复杂度 O(1)

Test Cases：
- 空数组
- 是二叉搜索树，不是二叉搜索树
- 只有右结点/左结点

⚠️
沟通数组为空的情况算True or False
'''
# -*- coding:utf-8 -*-
class Solution:
    def findIdx(self, sequence, start, end):
        for i in range(start, end):
            if sequence[i] > sequence[end]:
                return i 
        return -1
    
    def helper(self, sequence):
        if len(sequence) < 2:
            return  True
        idx = self.findIdx(sequence, 0, len(sequence)-1)
        if idx != -1 and min(sequence[idx:-1]) < sequence[-1]:
            return False
        left = self.helper(sequence[:idx])
        right = self.helper(sequence[idx:-1])
        return left and right
    
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if not sequence:
            return False
        return self.helper(sequence)
