'''
@lsy 2019.11.20
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        stack, res = [], []
        node = root
        while stack or node:
            while node:
                s tack.append(node)
                node = node.left
            if stack:
                tmp = stack.pop()
                res.append(tmp.val)
                node = tmp.right
        return res
