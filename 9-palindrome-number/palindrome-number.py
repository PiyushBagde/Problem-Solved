class Solution:
    def isPalindrome(self, x: int) -> bool:
        reverse = 0
        temp = x

        if temp < 0:
            return False

        while temp > 0:
            rem = temp % 10
            reverse = reverse * 10 + rem
            temp = temp // 10
        
        return reverse == x



        