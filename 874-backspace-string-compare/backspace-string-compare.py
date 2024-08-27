class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        new_s = []
        new_t = []
        for i in range(len(s)):
            if s[i] != "#":
                new_s.append(s[i])
            else:
                if len(new_s) > 0:
                    new_s.pop()

        for i in range(len(t)):
            if t[i] != "#":
                new_t.append(t[i])
            else:
                if len(new_t) > 0:
                    new_t.pop()
        return new_s==new_t


        