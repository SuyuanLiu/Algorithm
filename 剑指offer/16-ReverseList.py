'''
解题思路：
- 先判断特殊情况，空链表/只一个node的链表
- 设置指针pre，cur，操作指针即可
- 注意while的判断条件，用while cur.next，最后的结点没有被连接上；

时空复杂度：
- 时间复杂度 O(n)
- 空间复杂度 O(1)

Test Cases：
- 空链表/只一个node的链表
- 一般测试例子

⚠️
'''
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        if not pHead or not pHead.next:
            return pHead
        
        pre, cur = None, pHead
        while cur:
            tmp = cur.next
            cur.next = pre 
            pre = cur
            cur = tmp
        return pre
