class Solution:
    def nextPermutation(self, nums: List[int]) -> None:

        from typing import List

        n = len(nums) 

        ind = -1 # break point
        for i in range(n-2, -1, -1):
            if nums[i] < nums[i + 1]:
                ind = i
                break

        if ind == -1:
            # reverse the whole array:
            nums.reverse()
            return A

        # Step 2: Find the next greater element n swap

        for i in range(n - 1, ind, -1):
            if nums[i] > nums[ind]:
                nums[i], nums[ind] = nums[ind], nums[i]
                break

        # Step 3: reverse the right half:
        nums[ind+1:] = reversed(nums[ind+1:])

        return nums
            