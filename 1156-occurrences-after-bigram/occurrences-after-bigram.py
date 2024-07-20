class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        res = []
        lst = text.split()

        for i in range(len(lst) - 2):
            if lst[i] == first and lst[i+1] == second:
                res.append(lst[i+2])
        return res
