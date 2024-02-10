class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        summ1 = 0
        summ2 = 0

        if len(nums) == 1:
            return nums[0]

        for num in nums:
            summ1 += num
        
        nums1 = set(nums)

        for num in nums1:
            summ2 += 2*num

        return summ2-summ1


        