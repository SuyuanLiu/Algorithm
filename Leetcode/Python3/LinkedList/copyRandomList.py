'''
Solution:
- 思路类似与Clone Graph
- 要用一个map（dic）把之前的node与新生成的node给联系起来
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
            return head
        
        cur = head
        dic = {head: Node(head.val, None, None)}
        while cur:
            next = cur.next
            random = cur.random
            if next and next not in dic:
                 dic[next] = Node(next.val, None, None)
            if random and random not in dic:
                 dic[random] = Node(random.val, None, None)
                    
            copyNode = dic[cur]
            copyNode.next = dic[next] if next else None
            copyNode.random = dic[random] if random else None
            
            cur = cur.next
            
        return dic[head]
