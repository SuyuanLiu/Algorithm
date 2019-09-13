'''
@lsy  2019.9.13
注意边界条件，画图辅助。
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        pre, cur = None, head
        while cur:
            _next = cur.next
            cur.next = pre
            pre = cur
            cur = _next
            
        return pre
        
