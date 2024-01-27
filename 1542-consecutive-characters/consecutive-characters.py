class Solution(object):
    def maxPower(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 1:
                return 1
        else:
            count = 1
            max_count = 0

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