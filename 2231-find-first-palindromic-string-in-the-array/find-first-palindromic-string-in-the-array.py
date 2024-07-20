class Solution:
    def firstPalindrome(self, words: List[str]) -> str:        

        for s in words:
            i = 0
            j = len(s) -1
            while i <= j:
                if s[i] == s[j]:
                    if i == j or i+1 == j:
                        return s
                    i += 1
                    j -=1
                else:
                    break
        return ""

        