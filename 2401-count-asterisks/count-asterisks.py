class Solution:
    def countAsterisks(self, s: str) -> int:
        flag = 0 
        count = 0
        for i in s:
            if i == "*" and flag == 0:
                count += 1
            elif i == "|":
                if flag == 0:
                    flag = 1
                else:
                    flag = 0
        return count
            


            
                

        