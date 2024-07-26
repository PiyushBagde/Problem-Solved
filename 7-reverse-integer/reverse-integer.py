class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        if x < 0:
            flag  = 1
            x = x * -1
        else:
            flag = 0
        while x > 0:
            rem = x % 10
            res = (res * 10) + rem 
            x = x // 10
        
        if (-2**31) <= res <=( 2**31) - 1:
            if flag == 1:
                return res * -1
            else:
                return res
        else:
            return 0

        
        