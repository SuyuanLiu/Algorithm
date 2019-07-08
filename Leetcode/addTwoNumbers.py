'''
Solution 1
写的比较繁琐
- 从最后一位，一位一位相加，判断是否有进位carry
- 要注意：如果p1，p2都走完了，还有只剩一个进位carry的情况
- 在只剩下p1/p2时，也要考虑只剩一个进位的情况

时空复杂度：
- 时间复杂度 O(n)
- 空间复杂度 O(1)

⚠️很多细节遗漏

Solution 2:
简洁版，判断l1，l2，carry有一个不空即可继续a
'''
# Solution 2
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2:
            return 
        if not l1 or not l2:
            return l2 if not l1 else l1
        
        carry = 0
        dummy = ListNode(-1)
        cur = dummy
        
        while l1 or l2 or carry == 1:
            tmp = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            node = ListNode(tmp % 10)
            carry = tmp // 10
            
            cur.next = node
            cur = cur.next
            
            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2
            
        return dummy.next
        


# Solution 1
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def helper(self, p, dummy, cur, carry):
        while p:
            if carry == 0:
                cur.next = p
                return dummy.next
            
            sumBit = p.val + carry 
            if sumBit > 9:
                sumBit, carry = sumBit % 10, 1
            else:
                cur.next = ListNode(sumBit)
                cur.next.next = p.next
                return dummy.next
            cur.next = ListNode(sumBit)
            p, cur = p.next, cur.next
        if carry == 1:
            cur.next = ListNode(1)
            return dummy.next
    
    def addTwoNumbers(self, l1, l2):
        if not l1 and not l2:
            return None
        if not l1 or not l2:
            return l1 if not l1 else l2
        
        dummy = ListNode(-1)
        cur = dummy
        p1, p2 = l1, l2
        carry, sumBit = 0, 0
        
      
        while p1 and p2:
            sumBit = p1.val + p2.val + carry
            if sumBit > 9:
                sumBit, carry = sumBit % 10, 1
            else:
                carry = 0
            
            cur.next = ListNode(sumBit)
            cur = cur.next
            p1, p2 = p1.next, p2.next
            
        if p1:
            return self.helper(p1, dummy, cur, carry)
        if p2:
            return self.helper(p2, dummy, cur, carry)
        if carry:
            cur.next = ListNode(1)
        return dummy.next
