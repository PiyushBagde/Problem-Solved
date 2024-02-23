class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        greatest = max(candies)

        candies = [i+ extraCandies for i in candies]

        res = [True if candy >= greatest else False for candy in candies]
        return res

    