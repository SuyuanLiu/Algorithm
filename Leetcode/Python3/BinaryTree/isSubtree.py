# -*- coding:UTF-8 -*-
'''
Solution:
- 找到s中与t值相同的结点，判断他们是否可能为相同的树，不是的话再继续在s中找；
- 注意因为判断的是val，所以很有可能树中有多处值相同的，比如[1,1],[1]两棵树，不能武断的看到val相同的就直接判断这两棵树是否相同；
'''
class Solution:
    def isSameTree(self, a, b):
        if not (a and b):
            return a is b
        if a.val == b.val:
            return self.isSameTree(a.left, b.left) and self.isSameTree(a.right, b.right)
        return False
                
    
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if not t:
            return True
        if not s:
            return False
        
        if self.isSameTree(s, t): return True 
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
            
            