class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        count0 = 0
        count1 = 0
        temp0 = 0
        temp1 = 0

        for i in s:
            if i == '1':
                temp1 += 1
                temp0 = 0 
            elif i == '0':
                temp0 += 1
                temp1 = 0  

            if temp1 > count1:
                count1 = temp1

            if temp0 > count0:
                count0 = temp0
        
        return count1 > count0