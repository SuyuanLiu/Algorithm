# -*- coding:UTF-8 -*-
'''
用到dummy node
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        
        pre, cur = dummy, head
        while cur:
            if cur.val == val:
                pre.next = cur.next
                cur = cur.next
            else:
                tmp = cur.next
                pre = cur
                cur = tmp
                
        return dummy.next
