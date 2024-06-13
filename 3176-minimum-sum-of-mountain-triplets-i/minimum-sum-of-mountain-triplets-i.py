class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        count = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1 , len(nums)):
                    if nums[i] < nums[j] and nums[j] > nums[k]:
                        count.append(nums[i] + nums[j] + nums[k])
        
        if len(count) != 0:
            return min(count)
        return -1


    

            
        
