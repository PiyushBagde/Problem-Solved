class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dict1 = dict()

        for i in nums:
            if i in dict1:
                dict1[i] += 1
            else:
                dict1[i] = 1
        for key, val in dict1.items():
            if val == 1:
                return key