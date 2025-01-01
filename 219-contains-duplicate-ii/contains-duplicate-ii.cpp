class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        unordered_map<int, int> hashh;

        for (int i = 0; i < nums.size(); i++) {
            if( hashh.count(nums[i]) != 0 && abs(i - hashh[nums[i]]) <= k ) {
                return true;
            }
            
            hashh[nums[i]] = i;
            
        }

        return false;
        
    }
};