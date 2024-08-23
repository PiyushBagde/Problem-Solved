class Solution:
    def reverse(self, x: int) -> int:
        rem = 0
        num = 0
        neg = False
        if x < 0:
            neg = True
            x = x * -1


        while x>0:
            rem = x % 10
            num = num *10 + rem
            x = x//10

        if neg :
            num = num * (-1)
        
        if -2**31 < num < (2**31) - 1:
            return num
        else:
            return 0

        