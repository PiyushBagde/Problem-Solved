class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        summ = 0
        maxSum = nums[0]


        for num in nums:
            summ += num

            if summ > maxSum: # store the max summ value
                maxSum = summ

            if summ < 0: # if sum -ve reset summ to 0
                summ = 0

            
        return maxSum