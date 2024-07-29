class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        for i in range(1, n+1):
            if n%2==0 and i%n == 0:
                return i
        return n*2
    