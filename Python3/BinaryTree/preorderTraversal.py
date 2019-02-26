# -*- coding:UTF-8 -*-
'''
Solution：前序遍历
- 前序遍历顺序：根，左，右
- 三种方法：非递归（推荐），遍历递归，分治法


Solution 1:非递归
- 利用一个栈（先进后出）
- 弹出栈顶元素，依次把栈顶元素的右孩子、左孩子入栈；
- 注意左孩子后入栈，这样可以保证下次访问时左孩子先被访问； 

Solution 2：traversal

Solution 3：divide and conquer

注意：
- 遍历和分治的一个区别在于遍历没有返回值，分治有；
- 遍历法没办法用多线程，分治法可以；

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Solution 1
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        res, stack = [], [root]
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return res
        
        
        
        
# Solution 3 ： divide and conquer       
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        # divide
        left = self.preorderTraversal(root.left)
        right = self.preorderTraversal(root.right)
        
        # conquer
        res = [root.val] + left + right
        return res
        
    
    
    


# Solution 2 ：traversal      
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.traverse(root, res)
        return res
    
    def traverse(self, root, res):
        if not root:
            return 
        
        res.append(root.val)
        self.traverse(root.left, res)
        self.traverse(root.right, res)
        
        
        
        
        