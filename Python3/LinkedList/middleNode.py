# -*- coding:UTF-8 -*-
'''
Solution:
- 注意slow和fast都从head开始，while判断是判断fast和fast.next即可；
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        if not head:
            return 
        
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        return slow
