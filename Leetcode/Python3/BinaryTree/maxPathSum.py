# -*- coding:UTF-8 -*-
'''
Solution: 分治法
- 时间复杂度：O(n)
- 求最大路径和maxPath，有三种情况：最大路径和在左子树，最大路径和在右子树，最大路径和跨过root
- 对于跨过root的情况，可以看成： 从左子节点出发的最大路径和 + root.val + 从右子节点出发的最大路径和
  从左/右子节点出发的路径和，记做singlePath，singlePath可以不包含任何节点，也就是说singlePath最小可以是0；
  (这不违背题意，对于第三种情况，至少包含了root节点)
- 定义一个helper函数，返回从当前节点出发的最大路径和SinglePath，和在当前节点为root情况下的最大路径和maxPath；
  注意当root为空时，signlePath就返回0，maxPath返回负无穷，
  因为maxPath至少要包含一个节点，可以看作是包含了这个空节点，由于取不到这个空节点，所以返回负无穷；
- 定义一个新的数据类型path，包含singlePath和maxPath
  不需要也行，直接helper返回一个列表，这边是为了更好的理解才使用这个数据类型；

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Path:
    def __init__(self, a, b):
        self.singlePath = a
        self.maxPath = b

class Solution:
    def helper(self, root):
        if not root:
            return Path(0, -float('inf'))
        
        # divide 
        left = self.helper(root.left)
        right = self.helper(root.right)
        
        # conquer        
        maxPath = max(left.maxPath, right.maxPath)
        maxPath = max(maxPath, left.singlePath+right.singlePath+root.val)
        
        singlePath = max(left.singlePath, right.singlePath) + root.val  
        singlePath = max(singlePath, 0)          # 更新singlepath，后面要用，与0做比较，如果比0还小，那就一个点都不取了
        
        return Path(singlePath, maxPath)
        
        
    def maxPathSum(self, root: TreeNode) -> int:
        return self.helper(root).maxPath
