# -*- coding:UTF-8 -*-
'''
Solution:

参考链接：https://leetcode.com/problems/path-sum-ii/discuss/36829/Python-solutions-(Recursively-BFS%2Bqueue-DFS%2Bstack)

- 用一个栈path存储当前已经走过的路径；
- 对当前访问节点判断，是否为叶子节点，是的话，这条路径值是否满足要求；
  如果不是叶子节点的话，分别对它左右孩子节点进行判断；
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findPath(self, root, target, path, res):
        path.append(root)
        isLeaf = not root.left and not root.right
        if isLeaf and root.val == target: 
            res_path = [node.val for node in path]
            res.append(res_path)
        
        if root.left:
            path, res = self.findPath(root.left, target - root.val, path, res)
        if root.right:
            path, res = self.findPath(root.right, target - root.val, path, res)
            
        path.pop()
        
        return path, res
        
    
    
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        path, res = self.findPath(root, sum, [], [])
        return res
