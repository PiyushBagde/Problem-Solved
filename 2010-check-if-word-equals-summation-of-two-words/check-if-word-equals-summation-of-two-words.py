class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        sum1 = ""
        sum2 = ""
        sum3 = ""
        for i in firstWord:
            sum1 += str(ord(i) - 97)
        for j in secondWord:
            sum2 += str(ord(j) -97)

        for k in targetWord:
            sum3 += str(ord(k) - 97)
    
        total = int(sum1)+int(sum2)

        return total == int(sum3)


        