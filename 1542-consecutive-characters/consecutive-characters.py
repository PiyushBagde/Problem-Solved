class Solution:
    def maxPower(self, s: str) -> int:
            count = 1
            max_count = 0

            if len(s) == 1:
                return 1
            else:

                for i in range(1, len(s)):
                    if s[i] == s[i-1]:
                        count += 1
                        if count > max_count:
                            max_count = count
                    else:
                        count = 1
                if max_count == 0:
                    return 1

            return max_count   
            
