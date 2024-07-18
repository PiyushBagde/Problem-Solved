class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        lines = 1
        count = 0

        for i in range(len(s)):
            if count + widths[ord(s[i])-97] > 100:
                lines += 1
                count = 0
            count += widths[ord(s[i])-97]
        return [lines, count]


        