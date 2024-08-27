class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1 = {}

        for i in range(len(nums)):
            dict1[nums[i]] = i

        for i in range(len(nums)):
            val = target - nums[i]
            if val in dict1 and dict1[val] != i:
                return [i, dict1[val]]




        