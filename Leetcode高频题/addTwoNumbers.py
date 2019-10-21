'''
@lsy 2019.10.21

注意：边界条件
- 比如两个链表长度不一致
- 链表相加在最后一位时产生进位，比如 5 + 5， 9999 + 1

Discuss部分找了一个简洁版的答案。
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# clear code
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 or not l2:
            return l1 if not l2 else l2
        
        carry = 0
        dummyNode = cur = ListNode(0)
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            carry, val = divmod(carry, 10)
            cur.next = ListNode(val)
            cur = cur.next
        return dummyNode.next



# my code
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 or not l2:
            return l1 if not l2 else l2
        
        node1, node2 = l1, l2
        dummyNode = ListNode(0)
        cur = dummyNode
        flag = 0
        while node1 and node2:
            num = node1.val + node2.val + flag
            flag = 1 if num > 9 else 0
            cur.next = ListNode(num%10)
            cur = cur.next
            node1 = node1.next
            node2 = node2.next

        while node1:
            num = flag + node1.val
            flag = 1 if num > 9 else 0
            cur.next = ListNode(num%10)
            cur = cur.next
            node1 = node1.next   
        while node2:
            num = flag + node2.val
            flag = 1 if num > 9 else 0
            cur.next = ListNode(num%10)
            cur = cur.next
            node2 = node2.next            
        if flag:
            cur.next = ListNode(1)
            
        return dummyNode.next
            