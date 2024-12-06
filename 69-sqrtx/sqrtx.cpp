class Solution {
public:
    int mySqrt(int x) {
        long low, high, mid;
        low = 1;
        high = x;

        if(x <=1){
            return x;
        }

        while (low <= high) {
            mid = (low + high) / 2;

            if( mid * mid == x){
                return mid;
            }
            else if(mid*mid < x) {
                low = mid + 1;
            }
            else{
                high = mid - 1;
            }
        }

        return high;
    }
};