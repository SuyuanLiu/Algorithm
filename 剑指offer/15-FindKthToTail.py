'''
解题思路：
可以先把链表遍历一遍，得到链表的长度，然后找到倒数第k个结点，这个方法需要遍历链表两遍，不过时间复杂度还是O(n)。
优化：
只遍历一遍链表，设置两个指针，第一个指针先走k步，然后另一个指针从头开始，两个指针一起走，第一个指针到尾部时，第二个指针就是倒数第k个。
举例子来注意边界，+1，-1的。（第一个指针从head出发，走k-1步，如果走k步并且k等于链表长度时，就会走到None）

时空复杂度：
- 时间复杂度 O(n)
- 空间复杂度 O(1)

Test Cases：
- 空链表
- k <= 0
- k = len(linkedlist)
- k > len(linkedlist)
- 一般测试用例

⚠️
- 要问链表第一个元素是算第0个还是第1个
- 链表为空或k为非正数
'''
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if not head or k <= 0:
            return None
        
        cur = head 
        for i in range(k-1):
            cur = cur.next
            if not cur:
                return None
        node = head
        while cur.next:
            node = node.next
            cur = cur.next
        return node
