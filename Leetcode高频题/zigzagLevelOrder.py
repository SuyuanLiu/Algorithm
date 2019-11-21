'''
@lsy 2019.11.21
队列。
使用一个标记来记录当前层的数字是否需要翻转。
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        res, queue = [], [root]
        flag = 0
        while queue:
            tmp = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                tmp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
            if flag:
                res.append(tmp[::-1])
            else:
                res.append(tmp)
                
            flag ^= 1
        
        return res