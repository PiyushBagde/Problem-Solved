class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        diff = 0
        for i in range(len(s)):
            for j in range(len(s)):
                if s[i] == t[j]:
                    diff += abs(i-j)
                    break
        return diff
        