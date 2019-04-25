# -*- coding:UTF-8 -*-
'''
Solution:
- 因为head不确定，会变，这边使用dummy node
- 从cur判断，cur与cur.next是否相等，然后用while循环找到全部重复的值，直接令pre指向重复元素后面一个；
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return
        
        dummy = ListNode(0)
        dummy.next = head
        
        pre, cur = dummy, head
        while cur and cur.next:
            if cur.val == cur.next.val:
                tmp = cur.next
                while tmp and cur.val == tmp.val:
                    tmp = tmp.next
                pre.next = tmp
                cur = tmp
            else:
                pre = cur
                cur = cur.next
        return dummy.next
