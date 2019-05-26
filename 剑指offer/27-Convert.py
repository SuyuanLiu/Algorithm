'''
解题思路：
二叉搜索树的中序遍历是排好序的，所以这边考虑进行中序遍历。使用递归。
对于当前结点root，分别把左子树和右子树分别变为双向链表，然后把他们连接起来。
使用left指向左侧，right指向右侧。具体步骤如下：
参考：https://www.nowcoder.com/profile/163334/codeBookDetail?submissionId=1515508 赞第一的评论
注意：函数Convert返回的是双向链表的第一个结点
- 把左子树转化为双向链表
- 找到左链表的最右端，最后一个结点
- 把左侧链表与root相连
- 把右子树转化为双向链表
- 把右侧链表与root相连

时空复杂度：
- 时间复杂度 O(n)
- 空间复杂度 O(1)

Test Cases：
- 空树
- 只有一个结点，无子树
- 完全二叉树

'''
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Convert(self, pRootOfTree):
        # write code here
        if not pRootOfTree:
            return pRootOfTree
        
        # 把左子树转化为双向链表
        left = self.Convert(pRootOfTree.left)
        pre = left
        # 找到左侧链表的最右端
        while pre and pre.right:
            pre = pre.right
        # 与root相连
        if pre:
            pre.right = pRootOfTree
        pRootOfTree.left = pre 
        
        
        # 把右子树转化为双向链表
        right = self.Convert(pRootOfTree.right)
        pRootOfTree.right = right
        # 与root相连
        if right:
            right.left = pRootOfTree
            
        return left if left else pRootOfTree
