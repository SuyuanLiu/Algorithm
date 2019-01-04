# -*- coding:UTF-8 -*-
'''
Solution:
Solution 1:
- 定义一个函数isAncestor()用来判断当前结点是否为目标结点的祖先；
- 然后对二叉树的每一个结点判断是否为p,q的祖先，是的话就先记录下来，直到找到最后一个；
- 时间复杂度太高，超时没通过；

Solution 2:
- 分别记录在二叉树找到p,q的路径；比较二者路径，若二者有共同祖先，前面部分的路径一定相同，相同部分的最后一个节点就是最低公共祖先；
- 记录路径findNode中，使用了path，route两个变量，path记录现在所处路径，route为最终的结果；
  注意当root==p时，不可以route=path,这是浅拷贝，最终的结果是二者指向共同区域，随着path变化，route也在变化!!!

Solution 3:
- 参考：https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/discuss/152682/Python-simple-recursive-solution-with-detailed-explanation
- 如果p,q都在当前这棵最小的树里，那么它们的最小公共祖先就是当前的root；
  否则他们共存于当前root的左子树或者右子树中。（具体看代码中注释）


如果是一棵二叉搜索树，题目：https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
                    解法：Python3/BinaryTree/lowestCommonAncestorBST.py
如果只是一棵树，连二叉树都不是:(TODO)
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Solution 3
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if p == root or q == root:
            return root
        
        L, R = None, None
        
        if root.left:
            L = self.lowestCommonAncestor(root.left, p, q)
        if root.right:
            R = self.lowestCommonAncestor(root.right, p, q)
        
        # 说明p,q分别在root的左右两个子树里，那么root就是二者的LCA
        if L and R:  
            return root
        # 要么L为None，要么R为None，说明p,q共存于左子树或者右子树中
        return L if L else R



# Solution 2
class Solution:
    def findNode(self, root, p, path, route):
        path.append(root)
        if root == p:
            route = [n for n in path]   # don't use: route = path
            return path, route
    
        if root.left:
            path, route = self.findNode(root.left, p, path, route)
        if root.right:
            path, route = self.findNode(root.right, p, path, route)
        path.pop()
        return path, route
        

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if p == root or q == root:
            return root
        if p == q:
            return p
        
        path, routeP = self.findNode(root, p, [], [])
        path, routeQ = self.findNode(root, q, [], [])
        
        ancestor = None
        i, j = 0, 0
        while i < len(routeP) and j < len(routeQ) and routeP[i] == routeQ[j]:
            i += 1
            j += 1
        ancestor = routeP[i-1]
        return ancestor
        


# Solution 1

class Solution:
    def isAncestor(self, root, p):
        s = [root]
        while s:
            node = s.pop()
            if p == node:
                return True
            if node.right:
                s.append(node.right)
            if node.left:
                s.append(node.left)
        return False
    
    
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        ancestor = None
        s = [root]
        while s:
            node = s.pop()
            if self.isAncestor(node, p) and self.isAncestor(node, q):
                ancestor = node
            if node.right:
                s.append(node.right)
            if node.left:
                s.append(node.left)    
                
        return ancestor
        