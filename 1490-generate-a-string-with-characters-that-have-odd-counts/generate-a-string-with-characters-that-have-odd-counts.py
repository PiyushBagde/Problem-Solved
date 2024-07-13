class Solution:
    def generateTheString(self, n: int) -> str:
        if n % 2 != 0:
            return "a" *n
        else:
            str1 = "a" * (n-1)
            return str1+"b"
        