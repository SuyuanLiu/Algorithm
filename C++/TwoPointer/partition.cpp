/*
Solution: 时间复杂度O(n),空间复杂度O(n)
- 另外定义两个链表，分别存放小于x的node和>=x的node；
- 注意p2->next = NULL，因为p2是原来链表中的结点，后面可能还有其他结点，不置空会导致返回的新链表成环；
- 这里注意点操作符(.)和箭头操作符(->)的使用，.左边必须是实体，->左边必须是指针，具体看https://blog.csdn.net/qq457163027/article/details/54237782.

Solution 2：时间复杂度O(n),空间复杂度O(1) 有待完成（TODO）。
*/
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* partition(ListNode* head, int x) {
        ListNode dummy1(0), dummy2(0);
        ListNode *p1 = &dummy1, *p2 = &dummy2;
        while(head){
            if(head->val < x){
                p1->next = head;
                p1 = p1->next;
            }
            else{
                p2->next = head;
                p2 = p2->next;
            }
            head = head->next;
        }
        p1->next = dummy2.next;
        p2->next = NULL;
        return dummy1.next;
        
    }
};