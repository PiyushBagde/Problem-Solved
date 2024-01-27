class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if len(nums) == 1:
            if nums[0] == 1:
                return 1
            else:
                return 0
            
        else:
            count = 0
            max_count = 0
            for i in nums:
                if i != 0:
                    count += 1
                    if max_count < count:
                        max_count = count
                else:
                    count = 0
        return max_count
        