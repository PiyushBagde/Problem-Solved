class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        count = 150
        for i in range(len(nums)-2):
            for j in range(i+1, len(nums)-1):
                for k in range(j+1 , len(nums)):
                    if nums[i] < nums[j] and nums[j] > nums[k]:
                        total = nums[i]+nums[j]+nums[k]
                        if count > total:
                            count = total
        
        if count == 150:
            return -1
        return count


    

            
        
