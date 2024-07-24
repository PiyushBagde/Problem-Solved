class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        sm = 0

        for i in range(len(nums)):
            for j in range(len(nums)):
                sm += len(set(nums[i:j+1]))**2

        return sm