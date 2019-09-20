'''
@lsy  2019.9.20
读半天题目，才理解题意...
题意：
给出最深的leaf的公共祖先LCA。
如果最深的叶子节点只有一个，那么LCA就是这个节点。
如果最深叶子节点有多个，那么LCA就是最左和最右的root。

实际上，就是看左右子树的深度，当左右子树深度相同时，当前的root就是LCA。
对于只有一个最深leaf来说，左右子树为空，深度相同。

用递归，要返回当前树的最大深度。
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.LCA = None
        self.max_depth = -1
        
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        self.dfs(root, 0)
        return self.LCA
        
    def dfs(self, root, depth):
        if not root:
            return depth 
        depth += 1
        left = self.dfs(root.left, depth)
        right = self.dfs(root.right, depth)
        
        self.max_depth = max(self.max_depth, left, right)
        
        if left == right and left >= self.max_depth:
            self.LCA = root
        
        return max(left, right) 
        
        