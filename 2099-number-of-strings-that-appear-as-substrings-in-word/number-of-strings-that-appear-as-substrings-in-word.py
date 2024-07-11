class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        cc = 0
        for i in patterns:
            if i in word:
                cc += 1
        return cc
