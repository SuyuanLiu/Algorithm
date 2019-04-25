# -*- coding:UTF-8 -*-
'''
Question:
    输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。是的话返回TRUE，否则FALSE。
    假设输入数组的任意两个数字都互不相同。
Solution：
- 二叉搜索树的特点是：左子树节点值 < 根节点值 < 右子树节点值
- 二叉搜索树的中序遍历是有序数组

Solution 1：
- 利用二叉搜索树中序遍历有序，把输入的nums做排序，得到中序遍历结果；
- 对照中序遍历和后序遍历，看能否构成一棵二叉树即可；

Solution 2：
- 利用：左子树节点值 < 根节点值 < 右子树节点值
- 后序遍历最后一个值是根节点，前面分为左子树和右子树部分；利用左子树节点值小于根节点值，找出左子树部分，剩下就是右子树部分：
  检查右子树部分是否满足值大于根节点值，不满足的话就无法构成BST；
- 然后递归判断左右子树分别是否能构成BST。

- Solution 2 比 1 方法更优，耗费时间空间都小，不需要做排序，也不需要额外空间； 
'''


# Solution 2
class Solution:
    def isBST(self, nums):
        if len(nums) < 2:
            return True

        idx = 0
        while idx < len(nums) and nums[idx] < nums[-1]:
            idx += 1

        for i in range(idx, len(nums)):
            if nums[i] < nums[-1]:
                return False

        return self.isBST(nums[:idx]) and self.isBST(nums[idx:-1])


# Solution 1
class Solution:
    def isEqual(self, inOrder, postOrder):
        l1, l2 = len(inOrder), len(postOrder)
        if l1 < 2 and inOrder == postOrder:
            return True
        if l1 != l2 or postOrder[-1] not in inOrder:
            return False 

        idx = inOrder.index(postOrder[-1])
        return self.isEqual(inOrder[:idx], postOrder[:idx]) and self.isEqual(inOrder[idx+1:], postOrder[idx:-1])

    def isBST(self, nums):
        if len(nums) < 2:
            return True

        postOrder = [n for n in nums]
        nums.sort()
        inOrder = nums
        return self.isEqual(inOrder, postOrder)