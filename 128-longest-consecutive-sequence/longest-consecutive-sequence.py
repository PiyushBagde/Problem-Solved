class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        res = 0

        for i in nums:
            x = i-1
            count = 0

            if x not in numSet:

                # x is start
                while x+1 in numSet:
                    count += 1
                    x += 1
                
            res = max(count, res)

        return res
            
                

        