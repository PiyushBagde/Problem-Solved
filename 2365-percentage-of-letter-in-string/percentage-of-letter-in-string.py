class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        count = s.count(letter)
        prcnt = (count / len(s)) * 100
        return int(prcnt)

        