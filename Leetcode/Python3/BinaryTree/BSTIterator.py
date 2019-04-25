# -*- coding:UTF-8 -*-
'''
Solution:
- 本质就是中序遍历
- 把中序遍历的代码拆一下
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        self.curNode = root
        

    def next(self) -> int:
        """
        @return the next smallest number
        """
        while self.curNode:
            self.stack.append(self.curNode)
            self.curNode = self.curNode.left  
            
        self.curNode = self.stack.pop()
        val = self.curNode.val
        self.curNode = self.curNode.right
        return val
        
        

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.curNode != None or self.stack != []
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
