class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        lst = sentence.split()
        res = []

        for index, w in enumerate(lst):
            first = w[0]
            if first in "aeiouAEIOU":
                res.append(f"{w}ma")
            else:
                res.append(f"{w[1:]}{first}ma")
            
            res[-1] += "a" * (index+1)
        return " ".join(res)
        