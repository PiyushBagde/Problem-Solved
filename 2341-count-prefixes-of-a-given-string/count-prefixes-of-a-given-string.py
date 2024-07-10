class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        count = 0
        for word in words:
            if len(word)<=len(s):
                flag  = 0
                length = min(len(s), len(word))
                for i in range(length):
                    if word[i] != s[i]:
                        flag = 1
                        break
                
                if flag  == 0:
                    count += 1
        return count


            
                    