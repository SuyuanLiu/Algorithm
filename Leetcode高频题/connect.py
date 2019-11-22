'''
@lsy 2019.11.22

用一个preNode记录当前节点左边的节点。
注意：
    如果preNode不为空的话，当前root的left的左侧节点就是preNode的右节点。
'''
"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return 
        return self.helper(root, None)
        
    def helper(self, root, preNode):
        if not root or not root.left:
            return root
        
        root.left.next = root.right
        
        if preNode:
            preNode.right.next = root.left
            self.helper(root.left, preNode.right)
        else:
            self.helper(root.left, None)
        
        self.helper(root.right, root.left) 
        
        return root
