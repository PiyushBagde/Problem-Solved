class Solution:
    def reformatNumber(self, number: str) -> str:
        str1 = (number.replace(" ","")).replace("-","")

        if len(str1) == 4:
            return f"{str1[0:2]}-{str1[2:]}"

        rem = len(str1) % 3

        if rem == 1:
            lst =[str1[i:i+3] for i in range(0, len(str1) - 4, 3)]
            res = "-".join(lst)
            res += f"-{str1[-4:-2]}-{str1[-2:]}"
            return res

        lst = [str1[i:i+3] for i in range(0,len(str1), 3)]
        res = "-".join(lst)
        return res
        