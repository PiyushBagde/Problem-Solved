class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        i = 0
        while n != 0:
            if (n & 1)^((n>>1)&1) != 1:
                return False
            n >>= 1
        return True

        