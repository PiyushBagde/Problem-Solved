class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for i in details:
            lst = i[-4:-2]
            if int(lst)>60:
                count += 1
        return count

        