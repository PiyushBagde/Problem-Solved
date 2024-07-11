class Solution:
    def countAsterisks(self, s: str) -> int:
        flag = False
        count = 0
        for i in s:
            if i == "*" and flag == False:
                count += 1
            elif i == "|":
                flag = not flag
        return count
            


            
                

        