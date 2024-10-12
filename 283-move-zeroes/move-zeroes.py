class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        prev_idx = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[prev_idx] , nums[i] = nums[i], nums[prev_idx]
                prev_idx += 1
        