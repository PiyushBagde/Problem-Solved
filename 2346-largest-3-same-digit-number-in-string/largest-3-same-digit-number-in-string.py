class Solution:
    def largestGoodInteger(self, num: str) -> str:
        j = 0
        flag = 0
        counter = 1
        
        for i in range(1, len(num)):
            if num[i-1] == num[i] and counter <3:
                counter += 1
                if counter == 3 and j <= int(num[i]):
                    flag = 1
                    j = int(num[i])
                    counter = 1
            else:
                counter = 1

        if flag == 1:
            return f"{j}"*3
        else:
            return ""



        