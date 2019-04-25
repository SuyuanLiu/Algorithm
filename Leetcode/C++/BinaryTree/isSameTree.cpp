/*
Solution: 递归，时间复杂度O(n)
- 说明：代码参考高票答案，简洁规范；注释掉的代码是自己写的代码，看起来有点混乱...
*/
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    bool isSameTree(TreeNode* p, TreeNode* q) {
        if(p == NULL || q == NULL)
            return p == q;
        return(p->val == q->val && isSameTree(p->left, q->left) && isSameTree(p->right, q->right));
 
//         if(!p && !q)
//             return true;
//         if((p && !q) || (!p && q) || (p->val != q->val))
//             return false;
//         else
//             return isSameTree(p->left, q->left) && isSameTree(p->right, q->right);
    }
};