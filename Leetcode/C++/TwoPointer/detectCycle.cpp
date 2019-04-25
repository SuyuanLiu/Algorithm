/*
Solution: 双指针，时间复杂度O(n),空间复杂度O(1)
- 定义两个指针slow，fast，从head开始，一个走一步，一个走两步，如果有环一定相遇，而且slow的步数就是环的长度；

- 考虑如下链表，设 E 为环的入口，X是fast和slow的相遇点：
    H：从head到环的入口E的距离
    a: 入口E到相遇点X的距离
    b: 相遇点X到入口E的距离
                          _____
                         /     \
        head_____H______E       \
                        \       /
                         \__X__/   
        
    设 fast 和 slow 都从 head 开始，slow一次一步，fast一次两步，当二者相遇时，二者走的距离分别是：
    slow: H + a           fast: H + 2a + b
    fast 速度是 slow 两倍，所以 2(H + a) = H + 2a + b, 得 b = H.
    所以slow走的距离 H + a = b + a, 就是环的长度；

    要找到入口，可以让 fast 从 head 开始，slow 在相遇点 X，二者同时走（一次一步），再次相遇就是环的入口（H = b）。
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
    ListNode *detectCycle(ListNode *head) {
        if(head == NULL)
            return NULL;
        ListNode *slow = head, *fast = head;
        while(fast->next && fast->next->next){
            slow = slow->next;
            fast = fast->next->next;
            if(slow == fast){
                fast = head;
                while(slow != fast){
                    slow = slow->next;
                    fast = fast->next;
                }
                return slow;
            }
        }
        return NULL;
    }
};