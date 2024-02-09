class Solution:
    def reverse(self, x: int) -> int:
        num = str(x)
        flag = 0
        rev = 0
        max_num = 2**31 -1
        
        if num[0] == "-":
            flag = 1
            num = num[1:]
        
        rev = int(num[::-1])
        if rev >= max_num:
            return 0
        
        if flag == 1:
            return -rev
        else:
            return rev
            

        