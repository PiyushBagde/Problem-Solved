class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ones = 0
        zeros = 0

        for i in nums:
            if i == 0:
                zeros += 1
            elif i == 1:
                ones += 1 
        
        for i in range(zeros):
            nums[i] = 0

        for i in range(zeros, zeros+ones):
            nums[i] = 1
        
        for i in range(zeros+ones, len(nums)):
            nums[i] = 2