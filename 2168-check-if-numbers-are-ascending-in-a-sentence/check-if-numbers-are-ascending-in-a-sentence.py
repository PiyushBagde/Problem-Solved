class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        count = 0
        for i in s.split():
            if i.isdigit():
                if int(i) > count:
                    count = int(i)
                else:
                    return False
        return True




        