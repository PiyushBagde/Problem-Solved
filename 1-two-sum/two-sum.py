class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = {}

        for index, value in enumerate(nums):
            diff = target-value

            if diff not in temp:
                temp[value] = index

            else:
                return [index, temp[diff]]

        