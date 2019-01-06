# -*- coding:UTF-8 -*-
'''
Question:
    在一棵二叉树中，给定一个节点，找出中序遍历序列的下一个节点；
    树中节点除了指向左右子结点的指针，还有一个指向父节点的指针。

Solution:
- 中序遍历： 左 根 右
- 画出一棵具体的二叉树进行分析，得出以下三种情况：
    ~ 当node有右子结点：顺着右子树去找最左的结点，它就是下一个节点；
    ~ 当node没有右子结点：如果node是其parent的左子结点，那么下一个节点就是parent；
    ~ 当node没有右子结点：如果node是其parent的右子结点，需要向上去找，直到找到一个target，
      使得target为其parent的左子结点（！！！），那么下一个节点就是target.parent。

- Solution 2: 一样的idea，代码更简洁一点。
- 注意：Python中无法通过 node1 == node2 来判断两个节点是否相同，只能使用 node1.val == node2.val,
       所以在代码里面要首先判断node是否为None。
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.parent = None

class Solution:
    def nextNode(self, node):
        if not node:
            return 
        if node.right:             # 
            target = node.right
            while target.left:
                target = target.left
            return target

        elif not node.parent:
            return None

        else:
            if node.parent.left and node.val == node.parent.left.val:
                return node.parent 
            elif node.parent.right and node.val == node.parent.right.val:
                target = node.parent
                while target.parent:
                    if target.parent.left and target.val == target.parent.left.val:
                        return target.parent
                    else:
                        target = target.parent
                return None 



# Solution 2: more concise
class Solution:
    def nextNode(self, node):
        if not node:
            return 

        pNext = None
        if node.right:
            pNext = node.right
            while pNext.left:
                pNext = pNext.left 
        elif node.parent:
            pCur = node
            pParent = node.parent 
            while pParent and pParent.right and pCur.val == pParent.right.val:
                pCur = pParent
                pParent = pParent.parent
            pNext = pParent

        return pNext