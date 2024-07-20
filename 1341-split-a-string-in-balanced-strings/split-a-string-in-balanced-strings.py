class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count = 0
        l_count = 0

        for i in s:
            if i == "R":
                l_count -= 1
            else:
                l_count += 1
            
            if l_count == 0:
                count += 1
        return count
        