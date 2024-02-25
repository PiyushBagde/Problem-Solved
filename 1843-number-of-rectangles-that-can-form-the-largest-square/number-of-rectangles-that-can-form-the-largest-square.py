class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        temp = [min(i) for i in rectangles]

        maxx = max(temp)

        count  = 0

        for i in rectangles:
            if min(i) >= maxx:
                count += 1
        return count


        