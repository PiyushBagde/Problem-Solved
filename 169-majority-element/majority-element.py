class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict1 = Counter(nums)

        for index, val in dict1.items():
            if val > len(nums) /2:
                return index
        