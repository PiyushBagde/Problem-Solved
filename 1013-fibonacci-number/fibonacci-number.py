class Solution:
    def fib(self, n: int) -> int:
        first , second = 0, 1
        i = 0
        total = 0
        count = 0

        if n == 0:
            return 0

        if n == 1:
            return 1

        while i < n-1:
            total = first + second
            first, second = second, total
            i += 1
        
        return second
