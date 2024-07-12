class Solution:
    def countKeyChanges(self, s: str) -> int:
        cc = 0
        s = s.lower()
        for i in range(len(s)-1):
            if s[i]!=s[i+1]:
                cc += 1
        return cc
        