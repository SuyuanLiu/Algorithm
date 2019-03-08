# -*- coding:UTF-8 -*-
'''
Solution:
- 因为这边的head是确定的，不会变的，所以这边可以不用dummy node；
- 设置pre，cur指针，如果二者val相等，令pre指向cur的下一个；
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        
        pre, cur = head, head.next
        while cur:
            if pre.val == cur.val:
                pre.next = cur.next
            else:
                pre = cur
            cur = cur.next

        return head
