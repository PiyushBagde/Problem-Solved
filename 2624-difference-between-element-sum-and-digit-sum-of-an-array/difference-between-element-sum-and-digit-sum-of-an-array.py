class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        sum1 = 0
        sum2 = 0
        for i in nums:
            sum1 += i
        for i in nums:
            if i >9:
                while i>0:
                    rem = i%10
                    i = i//10
                    sum2 += rem

            else:
                sum2 += i
        return abs(sum1-sum2)
        