class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        maxx = 0
        count = 0

        for i in range(len(rectangles)):
            # find the min value from each sub list
            minn = min(rectangles[i][0], rectangles[i][1])
            # find the maximum  of minumumssss
            if maxx < minn:
                maxx = minn

        for j in range(len(rectangles)):
            if maxx <= min(rectangles[j][0], rectangles[j][1]):
                count += 1

        return count
            
        
            


        