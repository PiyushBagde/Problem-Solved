class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        set1 = sum(set(nums))
        summ = sum(nums)
        return set1*2 - summ

        