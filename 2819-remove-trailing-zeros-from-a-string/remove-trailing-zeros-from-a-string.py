class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        end = len(num) -1
        for i in range(len(num)-1,-1, -1):
            if num[i] != "0":
                end = i
                break
        return num[:end+1]
                


        