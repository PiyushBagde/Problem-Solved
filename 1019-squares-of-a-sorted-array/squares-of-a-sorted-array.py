class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        new = [i**2 for i in nums]
        new.sort()
        return new
        