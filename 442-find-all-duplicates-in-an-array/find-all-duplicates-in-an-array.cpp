class Solution {
public:
    vector<int> findDuplicates(vector<int>& nums) {
        unordered_set<int> hashset;
        vector<int> res;

        for (int i=0; i < nums.size(); i ++) {
            if ( hashset.contains(nums[i])) {
                res.push_back(nums[i]);
            }
            else {
                hashset.insert(nums[i]);
            }
        }

        return res;


        
    }
};