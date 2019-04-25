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
    vector<int> postorderTraversal(TreeNode* root) {
        vector<int> res;
        if(root == NULL)
            return res;
        res.push_back(root->val);
        
        vector<int> left = postorderTraversal(root->left);
        vector<int> right = postorderTraversal(root->right);
        
        left.insert(left.end(), right.begin(), right.end());
        left.insert(left.end(), res.begin(), res.end());
        
        return left;
    }
};