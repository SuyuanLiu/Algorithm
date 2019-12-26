'''
@lsy 2019.12.26
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return 
        
        pre, cur = None, head
        while cur:
            next = cur.next
            cur.next = pre
            pre = cur 
            cur = next
        return pre