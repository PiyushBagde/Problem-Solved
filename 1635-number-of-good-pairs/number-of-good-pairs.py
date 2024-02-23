class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        s = len(nums)
        count = 0
        for i in range(s):
            for j in range(s):
                if nums[i] == nums[j] and i < j:
                    count += 1
        return count
        