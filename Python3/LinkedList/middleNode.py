# -*- coding:UTF-8 -*-
'''
Solution:
- slow和fast都从head开始，while判断是判断fast和fast.next即可；

说明：
- slow和head从同一个位置出发，当有偶数个，返回的中点是后面一个中点；
- 当slow=head, fast=head.next, 偶数个时返回第一个中点；
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
