class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        str1 = ""
        for i in words:
            str1 += i[0]

        return str1 == s
