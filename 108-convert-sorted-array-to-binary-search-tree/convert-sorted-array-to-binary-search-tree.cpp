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

private:
    TreeNode* convert(vector<int>& arr, int low, int high) {
        if (low > high) {
            return nullptr;
        }

        int mid = (low + high) / 2;

        TreeNode* node = new TreeNode(arr[mid]);

        

        node->left = convert(arr, low, mid - 1);
        node->right = convert(arr, mid + 1, high);

        return node;
    }

public:
    TreeNode* sortedArrayToBST(vector<int>& nums) {
        if (sizeof(nums) == 0) {
        return nullptr;
        }

        return convert(nums, 0, nums.size() - 1);
    }
};