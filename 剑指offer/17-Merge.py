'''
解题思路：
- 处理特殊情况，其中一个/两个链表为空
- 设置一个dummyNode，用来指向合并后的链表的head；
  设置两个指针node1，node2，设置cur指针，指向当前合并后的最后一个结点；比较node1，node2的值，放到cur后面；
  如果一个链表元素全部被合并完，还剩一个链表有最后的元素，直接把最后的部分加进去即可。

时空复杂度：
- 时间复杂度 O(n+m)
- 空间复杂度 O(1)

Test Cases：
- 其中一个/两个链表为空
- 普通测试用例

'''
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        if not pHead1 or not pHead2:
            return pHead1 if not pHead2 else pHead2
        
        dummyNode = ListNode(0)
        node1, node2 = pHead1, pHead2
        cur = dummyNode
        while node1 and node2:
            if node1.val < node2.val:
                cur.next = node1
                cur = node1
                node1 = node1.next
            else:
                cur.next = node2
                cur = node2
                node2 = node2.next
                
        while node1:
            cur.next = node1
            node1 = node1.next
        while node2:
            cur.next = node2
            node2 = node2.next
        return dummyNode.next
