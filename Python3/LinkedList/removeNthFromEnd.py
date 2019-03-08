# -*- coding:UTF-8 -*-
'''
Solution:
- head有可能被删掉，用dummy node
- 使用快慢指针，快的先走n步，然后和慢指针一起走，当快指针到达尾部时，慢指针刚好到达Nth；
- 这边我让slow，fast都从dummy开始，fast走n步，最后slow到达(n-1)th位置，直接让slow指向next.next即可；
    就不用再另外设置pre指针了；
- 注意自己画图尝试一下，怎样使得slow走到前一个位置；（顺便可以解决list只有一个元素的情况）
- 注意这边判断的是fast.next
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        
        slow, fast = dummy, dummy
        for i in range(n):
            fast = fast.next
            
        while fast.next:
            slow = slow.next
            fast = fast.next
            
        slow.next = slow.next.next
        return dummy.next
