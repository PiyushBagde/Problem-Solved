/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int rangeSumBST(TreeNode* root, int low, int high) {
        int add_num = 0;
        if (root == nullptr){
            return 0;
        }

        int left_sum = rangeSumBST(root->left, low, high);
        int right_sum = rangeSumBST(root->right, low, high);

        if (root->val >= low && root->val <= high) {
            add_num = root->val;
        }
        

        return add_num + left_sum + right_sum;
        
    }
};