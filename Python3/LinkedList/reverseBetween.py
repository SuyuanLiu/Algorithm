# -*- coding:UTF-8 -*-
'''
- 如果m==1的话，head可能就无法确定，所以这边要用到dummy node.
- 把位置[m,n]的进行翻转，关键要记住m前面的node，m位置的node，n位置的node，n后面的node；
- 翻转完[m,n]后，把对应的部分连接起来即可；

Solution 1:
- 找到m位置的值，然后用for循环直接对m之后到n位置的进行翻转

Solution 2:
- 先找出四个关键的node位置
- 然后对[m,n]位置的进行翻转
'''
# Solution 2
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head, pre):
        cur = head
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre
    
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        
        cnt, cur = 0, dummy
        pre_m, n_next, m_node, n_node = None, None, None, None
        while cur:
            if cnt == m - 1:
                pre_m = cur
            if cnt == m:
                m_node = cur
            if cnt == n:
                n_node = cur
                n_next = cur.next
            cur = cur.next
            cnt += 1
            
        n_node.next = None
        node = self.reverseList(m_node, n_next)
        pre_m.next = node
        
        return dummy.next
            
        
                
        


# Solution 1
class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        
        m_pre, n_next = dummy, None
        for i in range(m - 1):
            m_pre = m_pre.next
          
        m_ = m_pre.next
        pre, cur = None, m_
        for i in range(m - 1, n):
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        n_ = pre
        n_next = temp
        
        m_pre.next = n_
        m_.next = n_next
        
        return dummy.next
