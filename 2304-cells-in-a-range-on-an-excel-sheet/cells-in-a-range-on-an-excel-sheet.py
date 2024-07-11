class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        sl = s[0]
        el = s[-2]
        sn = int(s[1])
        en = int(s[-1])
        lst = []
        for i in range(ord(sl), ord(el)+1):
            for j in range(sn,en+1):
                lst.append(chr(i) + str(j))
        return lst

        