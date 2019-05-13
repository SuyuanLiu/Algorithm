# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def isSameTree(self, pRoot1, pRoot2):
        if not pRoot1 and not pRoot2:
            return True
        elif (pRoot1 and not pRoot2) or (not pRoot1 and pRoot2) or pRoot1.val != pRoot2.val:
            return False
        return self.isSameTree(pRoot1.left, pRoot2.left) and self.isSameTree(pRoot1.right, pRoot2.right)
    
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        if not pRoot1 or not pRoot2:
            return False
            
        if self.isSameTree(pRoot1, pRoot2):
            return True
        else:
            return self.HasSubtree(pRoot1.left, pRoot2) or self.HasSubtree(pRoot1.right, pRoot2)
        
a,b,c,d,e,f,g = TreeNode(8), TreeNode(8), TreeNode(7), TreeNode(9), TreeNode(2), TreeNode(4), TreeNode(7)
a.left, a.right = b, c
b.left, b.right = d, e
e.left, e.right = f, g

aa, bb, cc = TreeNode(8), TreeNode(9), TreeNode(2)
aa.left, aa.right = bb, cc

s = Solution()
print(s.HasSubtree(a, aa))
