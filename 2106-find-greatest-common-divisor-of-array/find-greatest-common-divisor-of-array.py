class Solution:
    def findGCD(self, nums: List[int]) -> int:
        small = min(nums)
        large = max(nums)

        for i in range(large, 0, -1):
            if large % i ==0 and small % i == 0:
                return i
            
        return 1
        