class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        if len(num) == 1:
            return num
        for i in range(len(num)-1, -1, -1):
            if num[i] != "0":
                return num[:i+1]
        