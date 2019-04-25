# -*- coding:UTF-8 -*-
'''
Solution:
- 👇链接中有图解原因
https://leetcode.com/problems/linked-list-cycle-ii/discuss/249727/Python-Two(Three)-Pointers
- 从head出发到环入口的路径长 = 相遇点到环入口路径长
- 当相遇时，让slow从head出发，和fast一起，一次一步，直到二者再次相遇，就是环的入口；
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return None
        
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return fast
  
        return None
