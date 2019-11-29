'''
@lsy 2019.11.29
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
            return None
        
        dic = {head : Node(head.val, None, None), None : None}
        cur = head
        
        while cur:
            next = cur.next
            random = cur.random
            if next and next not in dic.keys():
                dic[next] = Node(next.val, None, None)
            if random and random not in dic.keys():
                dic[random] = Node(random.val, None, None)
                
            dic[cur].next = dic[next]
            dic[cur].random = dic[random]
            
            cur = cur.next

        return dic[head]
            