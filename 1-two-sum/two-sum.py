class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = {}

        for index, value in enumerate(nums):
            diff = target - value

            if diff in temp:
                return [index, temp[diff]]
            else:
                # save the visited number which is not anser yet
                temp[value] = index