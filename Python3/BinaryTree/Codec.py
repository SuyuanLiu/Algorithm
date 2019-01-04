# -*- coding:UTF-8 -*-
'''
Solution:
- 序列化与反序列化，这边使用的是一个队列，注意二者要通过相同的遍历模式；
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''
        
        res = ''
        s = [root]
        while s:
            node = s.pop(0)
            if node:
                res += ',' + str(node.val)
                s.append(node.left)
                s.append(node.right)
            else:
                res += ',None'

        return res
 

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        
        data = data.split(',')
        data.pop(0)
        root = TreeNode(int(data.pop(0)))
        s = [root]
        while s:
            node = s.pop(0)
            if node:
                l, r = data.pop(0), data.pop(0)
                node.left = None if l =='None' else TreeNode(int(l))
                node.right = None if r =='None' else TreeNode(int(r))
                s.append(node.left)
                s.append(node.right)

        return root
        
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))