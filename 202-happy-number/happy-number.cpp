class Solution {

private:
    int next_num(int n) {
        int num = 0, rem = 0;

        while( n!= 0 ) {
            rem = n%10;
            num += rem*rem;
            n /= 10;
        }
        
        return num;
    }

public:
    bool isHappy(int n) {
        set<int> num_visited;

        while (num_visited.count(n) == 0) {
            num_visited.insert(n);
            n = next_num(n);

            if (n == 1) {
                return true;
            }
        }

        return false;
        
    }
};