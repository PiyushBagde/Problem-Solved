class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        count = 0
        n = len(nums)

        for i in nums:
            count += i
        
        total = (n*(n+1))/2
        

        return  int(total - count)
        
        