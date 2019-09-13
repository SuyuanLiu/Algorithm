'''
@lsy 2019.9.13

深拷贝，要注意建立节点之间的连接，一一对应，使用dic。
同时注意边界条件。
'''
"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return 
        
        dic = {head: Node(head.val, None, None), None: None}
        cur = head 
        
        while cur:
            next = cur.next
            random = cur.random
            if next and next not in dic.keys():
                dic[next] = Node(next.val, None, None)
            if random and random not in dic.keys():
                dic[random] = Node(random.val, None, None)
            
            copyNode = dic[cur]
            copyNode.next = dic[next]
            copyNode.random = dic[random]
            
            cur = cur.next
        
        return dic[head]
