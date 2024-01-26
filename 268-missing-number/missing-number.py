class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        n = len(nums)

        for i in nums:
            count += i
        
        total = (n*(n+1))/2

        ans = total - count
        return ans

        