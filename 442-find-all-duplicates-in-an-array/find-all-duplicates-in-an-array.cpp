class Solution {
public:
    vector<int> findDuplicates(vector<int>& nums) {
        
        vector<int> res;

        for( auto n : nums){
            n = abs(n);

            if ( nums[ n-1 ] < 0) {
                res.push_back(n);
            }
            else {
                nums[ n-1 ] = -nums[ n-1 ];
            }
        }
        
        return res;
    }
};