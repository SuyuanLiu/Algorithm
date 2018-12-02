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
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> medium;
        if(root == NULL)
            return medium;
        else
            medium.push_back(root->val);
        vector<int> l = inorderTraversal(root->left);
        vector<int> r = inorderTraversal(root->right);
        l.insert(l.end(), medium.begin(), medium.end());
        l.insert(l.end(), r.begin(), r.end());
        return l;
    }
};