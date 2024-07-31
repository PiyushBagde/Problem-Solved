class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1 = dict()

        for index, val in enumerate(nums):
            diff = target - val

            if diff in dict1:
                return [index, dict1[diff]]
            else:
                dict1[val] = index
        