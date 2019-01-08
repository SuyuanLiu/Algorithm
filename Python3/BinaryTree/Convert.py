# -*- coding:UTF-8 -*-
'''
Question:
    输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。
    要求不能创建任何新的结点，只能调整树中节点指针的指向。
    （左指针指向前一个，右指正指向后一个节点）

Solution:
- 变成有序链表，对二叉搜索树做中序遍历即可；
- 把一棵二叉搜索树看成三个部分：根节点，左子树，右子树；
  根节点的left指向左子树形成链表的最后一个节点；根节点的right指向右子树形成链表的第一个节点；
  然后再对左右递归以上操作；

'''
class Solution:
    def __init__(self):
        self.pre = None
        self.head = None


    def inOrder(self, node):
        if not node:
            return 

        self.inOrder(node.left)
        node.left = self.pre 
        if self.pre:
            self.pre.right = node 
        self.pre = node 
        if not self.head:
            self.head = node 
        
        self.inOrder(node.right)


    def Convert(self, root):
        if not root:
            return 

        self.inOrder(root)
        return self.head
