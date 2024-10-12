class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int* ptr;
        int hold;
        ptr = &nums[0];

        for(int i=0; i < nums.size(); i++) {
            if (nums[i] != 0) {
                hold = *ptr;

                *ptr = nums[i];
                nums[i] = hold;
                ptr++;
            }
        }
        
        
    }
};