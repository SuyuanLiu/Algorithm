# -*- coding:UTF-8 -*-
'''
Solution：
- 把位置[m,n]的进行翻转，关键要记住m前面的node，m位置的node，n位置的node，n后面的node；
- 翻转完[m,n]后，把对应的部分连接起来即可；
'''
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
        
        