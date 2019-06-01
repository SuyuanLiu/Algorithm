'''
解题思路：
- 分别遍历一遍两个链表，计算每个链表的长度l1, l2
- 让较长的那个链表先走 abs(l1 - l2)步，然后两个链表一起走，判断两个当前结点是否相同

时空复杂度：
- 时间复杂度 O(m+n)
- 空间复杂度 O(1)

Test Cases：
- 空链表
- 无公共结点
- 第一个公共结点是head/在中间/在最后

另：
可以把两个链表的元素分别放到两个栈里面，然后从栈顶元素比较，直到最后一个相同的元素就是公共结点。
但是这个方法需要额外的辅助空间。
'''
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def lengthOfLinkedList(self, head):
        l = 0
        while head:
            l += 1
            head = head.next
        return l 
    
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        if not pHead1 or not pHead2:
            return None
        
        l1, l2 = self.lengthOfLinkedList(pHead1), self.lengthOfLinkedList(pHead2)
        node1, node2 = pHead1, pHead2
        if l1 < l2:
            l1, l2 = l2, l1
            node1, node2 = node2, node1
            
        for i in range(l1 - l2):
            node1 = node1.next
        while node1 != node2:
            node1, node2 = node1.next, node2.next
        return node1
